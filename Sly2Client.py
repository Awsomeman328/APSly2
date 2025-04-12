import json
import shutil
import zipfile
from typing import Optional, cast, Dict, Any, Set
import asyncio
import multiprocessing
import os
import subprocess
import traceback

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from NetUtils import ClientStatus
import Utils
from settings import get_settings
from kvui import GameManager

from .data import Locations
from .Sly2Interface import Sly2Interface, ConnectionState, Sly2Episode, PowerUps
from .Callbacks import init, update, handle_checks, handle_received

class Sly2CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class Sly2Context(CommonContext):
    current_episode: Optional[Sly2Episode] = None
    in_safehouse: bool = False
    is_pending_death_link_reset = False
    command_processor = Sly2CommandProcessor
    game_interface: Sly2Interface
    # notification_manager
    game = "Sly 2: Band of Thieves"
    items_handling = 0b111
    pcsx2_sync_task: Optional[asyncio.Task] = None
    is_connected: bool = False
    is_loading: bool = False
    is_connected_to_server: bool = False
    slot_data: Optional[dict[str, Utils.Any]] = None
    last_error_message: Optional[str] = None
    death_link_enabled = False
    queued_deaths: int = 0

    inventory: Dict[int,int] = {l.code: 0 for l in Locations.location_dict.values()}
    available_episodes: Dict[Sly2Episode,int] = {e: 0 for e in Sly2Episode}
    all_bottles: Dict[Sly2Episode,int] = {e: 0 for e in Sly2Episode}
    thiefnet_items: Optional[list[str]] = None
    powerups: PowerUps = PowerUps()
    thiefnet_purchases: PowerUps = PowerUps()
    notification_queue: list[str] = []

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game_interface = Sly2Interface(logger)

    def notification(self, text: str):
        self.notification_queue.append(text)

    def on_deathlink(self, data: Utils.Dict[str, Utils.Any]) -> None:
        super().on_deathlink(data)
        if self.death_link_enabled:
            self.queued_deaths += 1
            cause = data.get("cause", "")
            if cause:
                self.notification(f"DeathLink: {cause}")
            else:
                self.notification(f"DeathLink: Received from {data['source']}")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Sly2Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]

            # Set death link tag if it was requested in options
            if "death_link" in args["slot_data"]:
                self.death_link_enabled = bool(args["slot_data"]["death_link"])
                Utils.async_start(self.update_death_link(
                    bool(args["slot_data"]["death_link"])))
                Utils.async_start(self.send_msgs([{
                    "cmd": "LocationScouts",
                    "locations": [
                        Locations.location_dict[location].code
                        for location in Locations.location_groups["Purchase"]
                    ]
                }]))

def update_connection_status(ctx: Sly2Context, status: bool):
    if ctx.is_connected == status:
        return

    if status:
        logger.info("Connected to Sly 2")
    else:
        logger.info("Unable to connect to the PCSX2 instance, attempting to reconnect...")

    ctx.is_connected = status

async def pcsx2_sync_task(ctx: Sly2Context):
    logger.info("Starting Sly 2 Connector, attempting to connect to emulator...")
    ctx.game_interface.connect_to_game()
    while not ctx.exit_event.is_set():
        try:
            is_connected = ctx.game_interface.get_connection_state()
            update_connection_status(ctx, is_connected)
            if is_connected:
                await _handle_game_ready(ctx)
            else:
                await _handle_game_not_ready(ctx)
        except ConnectionError:
            ctx.game_interface.disconnect_from_game()
        except Exception as e:
            if isinstance(e, RuntimeError):
                logger.error(str(e))
            else:
                logger.error(traceback.format_exc())
            await asyncio.sleep(3)
            continue

async def _handle_game_ready(ctx: Sly2Context) -> None:
    current_episode = ctx.game_interface.get_current_episode()

    ctx.game_interface.skip_cutscene()

    if ctx.is_loading:
        if not ctx.game_interface.is_loading():
            ctx.is_loading = False
            if current_episode != 0:
                logger.info(f"Loaded episode {current_episode} ({current_episode.name})")
            await asyncio.sleep(1)
        await asyncio.sleep(0.1)
        return
    elif ctx.game_interface.is_loading():
        if current_episode != 0:
            ctx.game_interface.logger.info("Waiting for episode to load...")
        ctx.is_loading = True
        return

    connected_to_server = (ctx.server is not None) and (ctx.slot is not None)
    new_connection = ctx.is_connected_to_server != connected_to_server
    if ctx.current_episode != current_episode or new_connection:
        ctx.current_episode = current_episode
        ctx.is_connected_to_server = connected_to_server
        await init(ctx, connected_to_server)

    await update(ctx, connected_to_server)

    if ctx.server:
        ctx.last_error_message = None
        if not ctx.slot:
            await asyncio.sleep(1)
            return

        await asyncio.sleep(0.1)
    else:
        message = "Waiting for player to connect to server"
        if ctx.last_error_message is not message:
            logger.info("Waiting for player to connect to server")
            ctx.last_error_message = message
        await asyncio.sleep(1)


async def _handle_game_not_ready(ctx: Sly2Context):
    """If the game is not connected, this will attempt to retry connecting to the game."""
    ctx.game_interface.connect_to_game()
    await asyncio.sleep(3)

def launch_client():
    Utils.init_logging("Sly2 Client")

    async def main():
        multiprocessing.freeze_support()
        logger.info("main")
        parser = get_base_parser()
        args = parser.parse_args()
        ctx = Sly2Context(args.connect, args.password)

        logger.info("Connecting to server...")
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        logger.info("Running game...")
        ctx.pcsx2_sync_task = asyncio.create_task(pcsx2_sync_task(ctx), name="PCSX2 Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.pcsx2_sync_task:
            await asyncio.sleep(3)
            await ctx.pcsx2_sync_task

    import colorama

    colorama.init()

    asyncio.run(main())
    colorama.deinit()

if __name__ == "__main__":
    launch_client()