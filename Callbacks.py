from typing import TYPE_CHECKING
from time import sleep
from random import randint

import Utils

from .data import Items, Locations
from .Sly2Interface import Sly2Episode, PowerUps

if TYPE_CHECKING:
    from .Sly2Client import Sly2Context

def set_bottles(ctx: 'Sly2Context'):
    if ctx.current_episode is None:
        return

    bottles = ctx.all_bottles[ctx.current_episode]
    ctx.game_interface.set_bottles(bottles)

def set_thiefnet(ctx: 'Sly2Context'):
    if ctx.slot_data is None:
        return

    if ctx.thiefnet_items is None:
        info = ctx.locations_info
        ctx.thiefnet_items = []
        for i, location in enumerate(Locations.location_groups["Purchase"]):
            location_info = info[Locations.location_dict[location].code]

            player_name = ctx.player_names[location_info.player]
            item_name = ctx.item_names.lookup_in_slot(location_info.item,location_info.player)
            string = f"{player_name}'s {item_name}"

            ctx.thiefnet_items.append(string)

    ctx.game_interface.load_powerups(ctx.thiefnet_purchases)
    ctx.game_interface.set_thiefnet_unlock()

    print(ctx.slot_data["thiefnet_costs"])
    print(len(ctx.slot_data["thiefnet_costs"]))
    print(len(ctx.thiefnet_items))

    for i, item in enumerate(ctx.thiefnet_items):
        ctx.game_interface.set_thiefnet_cost(i,ctx.slot_data["thiefnet_costs"][i])
        ctx.game_interface.set_thiefnet(i,(f"Check #{i+1}",item))

def unset_thiefnet(ctx: 'Sly2Context'):
    set_powerups(ctx)
    ctx.game_interface.reset_thiefnet()

async def update(ctx: 'Sly2Context', ap_connected: bool) -> None:
    """Called continuously"""

    ctx.game_interface.unlock_episodes()
    boot_from_invalid_episode(ctx, ap_connected)

    if ap_connected:
        set_bottles(ctx)
        in_safehouse = ctx.game_interface.in_safehouse()
        if in_safehouse and not ctx.in_safehouse:
            ctx.in_safehouse = True
            set_thiefnet(ctx)
        elif ctx.in_safehouse and not in_safehouse:
            ctx.in_safehouse = False
            unset_thiefnet(ctx)

        await handle_received(ctx)
        await handle_checks(ctx)
        await handle_death_link(ctx)

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
    locked_episode = (
        ap_connected and
        current_episode != 0 and
        ctx.available_episodes[current_episode] == 0
    )
    skip_intro = (
        ap_connected and
        current_episode == 0 and
        current_job == 1583 and
        ctx.slot_data is not None and
        ctx.slot_data["skip_intro"]
    )

    if not_connected or locked_episode or skip_intro:
        ctx.game_interface.to_episode_menu()
        sleep(1)

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
    # boot_from_invalid_episode(ctx, ap_connected)
    if ap_connected:
        # ctx.game_interface.logger.info("Initializing")
        set_powerups(ctx)
        set_thiefnet_costs(ctx)
        replace_text(ctx)
        set_jobs(ctx)

async def handle_received(ctx: 'Sly2Context') -> None:
    if ctx.slot_data is None:
        return

    items_n = ctx.game_interface.read_items_received()

    available_episodes = {e: 0 for e in Sly2Episode}
    bottles = {e: 0 for e in Sly2Episode}
    network_items = ctx.items_received
    if ctx.slot_data["episode_8_keys"]:
        clockwerk_parts = [i for i in ctx.items_received if Items.from_id(i.item).category == "Clockwerk Part"]
        if clockwerk_parts >= ctx.slot_data["required_keys"]:
            available_episodes[Sly2Episode.Anatomy_for_Disaster] = 1

    for i, network_item in enumerate(network_items):
        item = Items.from_id(network_item.item)
        player = ctx.player_names[network_item.player]

        new_count = len([i for i in ctx.items_received if i.item == network_item.item])

        if new_count > ctx.inventory[network_item.item]:
            ctx.inventory[network_item.item] += 1
            ctx.notification(f"Received {item} from {player}")

        if item.category == "Episode":
            episode = Sly2Episode[item.name[12:].replace(" ","_")]

            if (
                not episode != Sly2Episode.Anatomy_for_Disaster or
                not ctx.slot_data["episode_8_keys"] or
                available_episodes[episode] > 0
            ):
                available_episodes[episode] += 1
        elif item.category == "Power-Up":
            setattr(ctx.powerups,item.name.lower().replace(" ","_"),True)
        elif item.category == "Bottles":
            split = item.name.index("-")
            episode_name = item.name[split+2:]
            episode = Sly2Episode[episode_name.replace(" ","_")]
            amount = int(item.name[:split-1])
            bottles[episode] += amount
        elif item.name == "Coins" and i >= items_n:
            amount = randint(
                ctx.slot_data["coins minimum"],
                ctx.slot_data["coins maximum"]
            )
            ctx.game_interface.add_coins(amount)

    ctx.game_interface.set_items_received(len(network_items))
    ctx.available_episodes = available_episodes


async def handle_checks(ctx: 'Sly2Context') -> None:
    pass

async def handle_death_link(ctx: 'Sly2Context') -> None:
    pass