import typing

from BaseClasses import Region, CollectionState, Location

from .data.Locations import location_dict
from .data.Items import item_groups
from .data.data import episodes, treasures

if typing.TYPE_CHECKING:
    from . import Sly2World
    from .Sly2Options import Sly2Options

def create_access_rule(episode: str, n: int, options: "Sly2Options", player: int):
    def rule(state: CollectionState):
        access = True
        item_name = f"Progressive {episode}"

        if episode == "Anatomy for Disaster" and options.episode_8_keys:
            access = (
                access and
                state.count_group("Clockwerk Part", player) >= options.required_keys and
                state.count(item_name, player) >= n-1
            )
        else:
            access = access and state.count(item_name, player) >= n

        if episode == "He Who Tames the Iron Horse" and n >= 3:
            access = access and state.has("Paraglider", player)

        if episode == "Menace from the North, Eh!" and n == 4:
            access = (
                access and
                state.has("Paraglider", player) and
                state.has("Alarm Clock", player)
            )

        return access

    return rule

def create_regions(world: "Sly2World"):
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    for i, episode in enumerate(episodes.keys()):
        for n in range(1,5):
            if n == 3 and episode == "Jailbreak":
                break

            region = Region(f"Episode {i+1} ({n})", world.player, world.multiworld)
            region.add_locations({
                f"{episode} - {job}": location_dict[f"{episode} - {job}"].code
                for job in episodes[episode][n-1]
            })

            world.multiworld.regions.append(region)
            menu.connect(
                region,
                None,
                create_access_rule(episode, n, world.options, world.player)
            )

    def add_safe(episode: str, region: str):
        world.get_region(region).add_locations(
            {f"{episode} - Safe": location_dict[f"{episode} - Safe"].code}
        )

    add_safe("The Black Chateau", "Episode 1 (2)")
    add_safe("A Starry Eyed Encounter", "Episode 2 (3)")
    add_safe("The Predator Awakens", "Episode 3 (2)")
    add_safe("Jailbreak", "Episode 4 (1)")
    add_safe("A Tangled Web", "Episode 5 (1)")
    add_safe("He Who Tames the Iron Horse", "Episode 6 (1)")
    add_safe("Menace from the North, Eh!", "Episode 7 (2)")
    add_safe("Anatomy for Disaster", "Episode 8 (2)")

    for i, (ep, t) in enumerate(treasures.items()):
        for treasure in t:
            location_name = f"{ep} - {treasure[0]}"
            region = f"Episode {i+1} ({treasure[1]})"
            world.get_region(region).add_locations(
                {location_name: location_dict[location_name].code}
            )