from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Sly2Client import Sly2Context

def set_bottles(ctx: 'Sly2Context'):
    if ctx.current_episode is None:
        return

    bottles = ctx.all_bottles[ctx.current_episode]

def set_thiefnet(ctx: 'Sly2Context'):
    pass

def unset_thiefnet(ctx: 'Sly2Context'):
    set_powerups(ctx)
    ctx.game_interface.reset_thiefnet()

async def update(ctx: 'Sly2Context', ap_connected: bool) -> None:
    """Called continuously"""

    if ap_connected:
        set_bottles(ctx)
        in_safehouse = ctx.game_interface.in_safehouse()
        if in_safehouse and not ctx.in_safehouse:
            ctx.in_safehouse = True
            set_thiefnet(ctx)
        elif ctx.in_safehouse and not in_safehouse:
            ctx.in_safehouse = False
            unset_thiefnet(ctx)

        if ctx.current_episode is not None and ctx.current_episode > 0:
            await handle_received(ctx)
            await handle_checks(ctx)
            await handle_death_link(ctx)

    # else:
    #     if ctx.notification_manager.queue_size() == 0:
    #         ctx.notification_manager.queue_notification("\14Warning!\10 Not connected to Archipelago server", 1.0)
    #     return

def replace_text(ctx: 'Sly2Context') -> None:
    ctx.game_interface.set_text(
        "Press START (new)",
        "Press START for new Archipelago"
    )
    ctx.game_interface.set_text(
        "Press START (resume)",
        "Press START to resume Archipelago"
    )
    ctx.game_interface.set_text(
        "this powerup.",
        "this check."
    )

def boot_from_invalid_episode(ctx: 'Sly2Context', ap_connected: bool) -> None:
    current_episode = ctx.current_episode
    current_job = ctx.game_interface.get_current_job()

    if current_episode is None:
        return

    not_connected = current_episode != 0 and not ap_connected
    locked_episode = ap_connected and ctx.available_episodes[current_episode] == 0
    skip_intro = (
        ap_connected and
        current_episode == 0 and
        current_job == 1583 and
        ctx.slot_data is not None and
        ctx.slot_data["skip_intro"]
    )

    if not_connected or locked_episode or skip_intro:
        ctx.game_interface.to_episode_menu()

def set_jobs(ctx: 'Sly2Context') -> None:
    pass

def set_thiefnet_costs(ctx: 'Sly2Context') -> None:
    if ctx.slot_data is None:
        return

    costs = ctx.slot_data["thiefnet_costs"]
    for i, price in enumerate(costs):
        ctx.game_interface.set_thiefnet_cost(i, price)

def set_powerups(ctx: 'Sly2Context'):
    ctx.game_interface.load_powerups(ctx.powerups)

async def init(ctx: 'Sly2Context', ap_connected: bool) -> None:
    """Called when the player connects to the AP server or enters a new episode"""
    boot_from_invalid_episode(ctx, ap_connected)
    if ap_connected:
        set_powerups(ctx)
        set_thiefnet_costs(ctx)
        replace_text(ctx)
        set_jobs(ctx)

async def handle_received(ctx: 'Sly2Context') -> None:
    pass

async def handle_checks(ctx: 'Sly2Context') -> None:
    pass

async def handle_death_link(ctx: 'Sly2Context') -> None:
    pass