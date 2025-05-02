import typing

from BaseClasses import Region, CollectionState, Location

from .data.Locations import location_dict, location_groups
from .data.Items import item_groups
from .data.Constants import EPISODES, TREASURES

if typing.TYPE_CHECKING:
    from . import Sly2World
    from .Sly2Options import Sly2Options

def create_access_rule(episode: str, n: int, options: "Sly2Options", player: int):
    """Returns a function that checks if the player has access to a specific region"""
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
    """Creates a region for each chapter of each episode"""
    menu = Region("Menu", world.player, world.multiworld)
    menu.add_locations({
        f"ThiefNet {i+1:02}": location_dict[f"ThiefNet {i+1:02}"].code
        for i in range(24)
    })

    world.multiworld.regions.append(menu)

    for i, episode in enumerate(EPISODES.keys()):
        for n in range(1,5):
            if n == 4 and episode == "Jailbreak":
                break

            region = Region(f"Episode {i+1} ({n})", world.player, world.multiworld)
            region.add_locations({
                f"{episode} - {job}": location_dict[f"{episode} - {job}"].code
                for job in EPISODES[episode][n-1]
            })

            world.multiworld.regions.append(region)
            menu.connect(
                region,
                None,
                create_access_rule(episode, n, world.options, world.player)
            )

    bottle_n = world.options.bottle_location_bundle_size

    def add_bottles(episode: str, region: str, n:int):
        """Adds a location for n bottles collected in a specific episode"""
        location_name = f"{episode} - {n} bottles collected"
        world.get_region(region).add_locations(
            {location_name: location_dict[location_name].code}
        )

    if world.options.bottle_location_bundle_size > 0:
        for i, episode in enumerate(EPISODES.keys()):
            total_bottles = 0
            while total_bottles+bottle_n <= 30:
                total_bottles += bottle_n
                add_bottles(episode, f"Episode {i+1} (1)", total_bottles)

            if total_bottles < 30:
                add_bottles(episode, f"Episode {i+1} (1)", 30)


    def add_vault(episode: str, region: str):
        world.get_region(region).add_locations(
            {f"{episode} - Vault": location_dict[f"{episode} - Vault"].code}
        )

    if world.options.include_vaults:
        add_vault("The Black Chateau", "Episode 1 (2)")
        add_vault("A Starry Eyed Encounter", "Episode 2 (3)")
        add_vault("The Predator Awakens", "Episode 3 (2)")
        add_vault("Jailbreak", "Episode 4 (1)")
        add_vault("A Tangled Web", "Episode 5 (3)")
        add_vault("He Who Tames the Iron Horse", "Episode 6 (1)")
        add_vault("Menace from the North, Eh!", "Episode 7 (2)")
        add_vault("Anatomy for Disaster", "Episode 8 (2)")

    for i, (ep, t) in enumerate(TREASURES.items()):
        for treasure in t:
            location_name = f"{ep} - {treasure[0]}"
            region = f"Episode {i+1} ({treasure[1]})"
            world.get_region(region).add_locations(
                {location_name: location_dict[location_name].code}
            )