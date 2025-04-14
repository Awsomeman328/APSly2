from typing import TYPE_CHECKING
from time import sleep, time
from random import randint

from .data import Items, Locations
from .data.data import EPISODES
from .Sly2Interface import Sly2Episode

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
    ctx.thiefnet_purchases = ctx.game_interface.read_powerups()
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

        if ctx.current_episode != 0:
            set_jobs(ctx)

        if (
            ctx.current_episode != Sly2Episode.Title_Screen and
            not in_safehouse
        ):
            await handle_notifications(ctx)
            await handle_deathlink(ctx)


        await handle_received(ctx)
        await handle_checks(ctx)

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
    """
    Sets jobs to available/unavailable
    """
    if ctx.current_episode is None:
        return

    episode_jobs = ctx.game_interface.addresses["jobs"][ctx.current_episode.value-1]
    available = ctx.available_episodes[ctx.current_episode]
    for i, chapter in enumerate(episode_jobs):
        for job in chapter:
            if available > i:
                ctx.game_interface.activate_job(job)
            else:
                ctx.game_interface.deactivate_job(job)

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

async def handle_notifications(ctx: 'Sly2Context') -> None:
    if (
        (ctx.showing_notification and time() - ctx.notification_timestamp < 5) or
        ((not ctx.showing_notification) and ctx.game_interface.is_infobox())
    ):
        return

    ctx.game_interface.disable_infobox()
    ctx.showing_notification = False
    if len(ctx.notification_queue) > 0:
        new_notification = ctx.notification_queue.pop(0)
        ctx.notification_timestamp = time()
        ctx.showing_notification = True
        ctx.game_interface.set_infobox(new_notification)


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

        if i >= items_n:
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
    if ctx.slot_data is None:
        return

    locations = set()

    # ThiefNet purchases
    purchases = list(ctx.thiefnet_purchases)[:24]
    for i, purchased in enumerate(purchases):
        if purchased:
            location_name = f"ThiefNet {i+1}"
            location_code = Locations.location_dict[location_name].code
            locations.add(location_code)

    # Bottles
    bottle_n = ctx.slot_data["bottle_location_bundle_size"]
    for ep in Sly2Episode:
        bottles = ctx.game_interface.get_bottles(ep)
        for i in range(1,bottles+1):
            if i%bottle_n == 0 or i == 30:
                location_name = f"{str(ep).replace('_',' ')} - {i} bottles collected"
                location_code = Locations.location_dict[location_name].code
                locations.add(location_code)

    # Jobs
    for i, episode in enumerate(ctx.game_interface.addresses["jobs"]):
        for j, chapter in enumerate(episode):
            for k, job in enumerate(chapter):
                completed = ctx.game_interface.job_completed(job)
                if completed:
                    episode_name = list(EPISODES.keys())[i]
                    job_name = EPISODES[episode_name][j][k]
                    location_name = f"{episode_name} - {job_name}"
                    location_code = Locations.location_dict[location_name].code
                    locations.add(location_code)


    await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": ctx.locations_checked}])


async def handle_deathlink(ctx: 'Sly2Context') -> None:
    if time()-ctx.deathlink_timestamp > 10:
        if ctx.game_interface.alive():
            if ctx.queued_deaths > 0:
                ctx.game_interface.kill_player()
                ctx.queued_deaths -= 1
                ctx.deathlink_timestamp = time()
        else:
            # Maybe add something that writes a cause
            await ctx.send_death()
            ctx.deathlink_timestamp = time()
