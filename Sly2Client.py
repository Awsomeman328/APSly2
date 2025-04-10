import json
import shutil
import zipfile
from typing import Optional, cast, Dict, Any
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

from .Sly2Interface import Sly2Interface, ConnectionState, Sly2Episode
from .Callbacks import init, update

class Sly2CommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class Sly2Context(CommonContext):
    current_episode: Optional[Sly2Episode] = None
    is_pending_death_link_reset = False
    command_processor = Sly2CommandProcessor
    game_interface: Sly2Interface
    # notification_manager
    game = "Sly 2"
    pcsx2_sync_task: Optional[asyncio.Task] = None
    is_connected: bool = False
    is_loading: bool = False
    slot_data: Optional[dict[str, Utils.Any]] = None
    last_error_message: Optional[str] = None
    death_link_enabled = False
    queued_deaths: int = 0

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game_interface = Sly2Interface(logger)
        # self.notification_manager = NotificationManager(HUD_MESSAGE_DURATION)

    def on_deathlink(self, data: Utils.Dict[str, Utils.Any]) -> None:
        super().on_deathlink(data)
        if self.death_link_enabled:
            self.queued_deaths += 1
            cause = data.get("cause", "")
            # if cause:
            #     self.notification_manager.queue_notification(f"DeathLink: {cause}")
            # else:
            #     self.notification_manager.queue_notification(f"DeathLink: Received from {data['source']}")

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

            # Scout all active locations for lookups that may be required later on
            # all_locations = [loc.location_id for loc in get_all_active_locations(self.slot_data)]
            # self.locations_scouted = set(all_locations)
            # Utils.async_start(self.send_msgs([{
            #     "cmd": "LocationScouts",
            #     "locations": list(self.locations_scouted)
            # }]))

    # def run_gui(self):
    #     class Sly2Manager(GameManager):
    #         logging_pairs = [
    #             ("Client", "Archipelago")
    #         ]
    #         base_title = "Archipelago Sly 2 Client"

    #     self.ui = Sly2Manager(self)
    #     self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

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

async def _handle_game_ready(ctx: Sly2Context):
    if ctx.is_loading:
        if not ctx.game_interface.is_loading():
            ctx.is_loading = False
            current_episode = ctx.game_interface.get_current_episode()
            if current_episode is not 0:
                logger.info(f"Loaded episode {current_episode} ({current_episode.name})")
            await asyncio.sleep(1)
        await asyncio.sleep(0.1)
        return
    elif ctx.game_interface.is_loading():
        ctx.game_interface.logger.info("Waiting for planet to load...")
        ctx.is_loading = True
        return

    connected_to_server = (ctx.server is not None) and (ctx.slot is not None)
    if ctx.current_episode != ctx.game_interface.get_current_episode() and connected_to_server:
        ctx.current_episode = ctx.game_interface.get_current_episode()
        init(ctx)
    update(ctx, connected_to_server)

    if ctx.server:
        ctx.last_error_message = None
        if not ctx.slot:
            await asyncio.sleep(1)
            return

        # current_inventory = ctx.game_interface.get_current_inventory()
        # if ctx.current_episode is not None and ctx.current_planet > 0 and ctx.game_interface.get_pause_state() in [0, 5]:
        #     await handle_received_items(ctx, current_inventory)
        # if ctx.current_planet and ctx.current_planet > 0:
        #     await handle_checked_location(ctx)
        # await handle_check_goal_complete(ctx)

        # if ctx.death_link_enabled:
        #     await handle_deathlink(ctx)
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