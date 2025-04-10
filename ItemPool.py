import typing
import random

from BaseClasses import Item

from .data.data import episodes
from .data.Items import item_groups
from .Sly2Options import StartingEpisode

if typing.TYPE_CHECKING:
    from . import Sly2World

def gen_powerups(world: "Sly2World") -> list[Item]:
    return [
        world.create_item(item_name)
        for item_name in item_groups["Power-Up"]
    ]

def gen_episodes(world: "Sly2World") -> list[Item]:
    all_episodes = [
        item_name for item_name in item_groups["Episode"]
        for _ in range(4)
    ]
    all_episodes.remove("Progressive Jailbreak")
    if world.options.episode_8_keys:
        all_episodes.remove("Progressive Anatomy for Disaster")

    starting_episode_n = world.options.starting_episode.value
    if starting_episode_n == 9:
        starting_episode_n = random.randint(1,7)

    starting_episode = f"Progressive {list(episodes.keys())[starting_episode_n]}"

    all_episodes.remove(starting_episode)
    world.multiworld.push_precollected(world.create_item(starting_episode))

    return [world.create_item(e) for e in all_episodes]

def gen_clockwerk(world: "Sly2World") -> list[Item]:
    if world.options.episode_8_keys:
        num_keys = world.options.keys_in_pool.value
    else:
        num_keys = 0

    return [
        world.create_item(p)
        for p in
        random.sample(list(item_groups["Clockwerk Part"]), num_keys)
    ]

def gen_pool(world: "Sly2World") -> list[Item]:
    item_pool = []
    item_pool += gen_powerups(world)
    item_pool += gen_episodes(world)
    item_pool += gen_clockwerk(world)

    remaining = len(world.multiworld.get_unfilled_locations(world.player))-len(item_pool)
    assert remaining > 1, f"There are more items than locations ({len(item_pool)} items)"
    item_pool += [world.create_item(world.get_filler_item_name()) for _ in range(remaining-1)]

    return item_pool
