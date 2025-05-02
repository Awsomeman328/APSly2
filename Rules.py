import typing
from math import ceil

from BaseClasses import CollectionState

from worlds.generic.Rules import add_rule
from .data.Constants import EPISODES

if typing.TYPE_CHECKING:
    from . import Sly2World

def set_rules(world: "Sly2World"):
    player = world.player

    add_rule(
        world.get_location("A Tangled Web - Crystal Vase"),
        lambda state: (
            state.has("Paraglider", player) or
            state.has("Mega Jump", player)
        )
    )
    add_rule(
        world.get_location("A Tangled Web - Operation: High Road"),
        lambda state: state.has("Paraglider", player)
    )
    add_rule(
        world.get_location("He Who Tames the Iron Horse - Spice in the Sky"),
        lambda state: state.has("Paraglider", player)
    )
    add_rule(
        world.get_location("He Who Tames the Iron Horse - Ride the Iron Horse"),
        lambda state: state.has("Paraglider", player)
    )
    add_rule(
        world.get_location("Menace from the North, Eh! - Jeweled Chalice"),
        lambda state: state.has("Paraglider", player)
    )
    add_rule(
        world.get_location("Menace from the North, Eh! - Thermal Ride"),
        lambda state: state.has("Paraglider", player)
    )

    bottle_n = world.options.bottle_item_bundle_size.value
    if bottle_n != 0:
        bundle_count = 30//bottle_n
        remainder = 30%bottle_n
        for ep in EPISODES.keys():
            if bottle_n == 1:
                bundle_name = f"Bottle - {ep}"
            else:
                bundle_name = f"{bottle_n} bottles - {ep}"
            add_rule(
                world.get_location(f"{ep} - Vault"),
                lambda state, bn=bundle_name: state.has(bn, player, bundle_count)
            )

            if remainder > 0:
                if remainder == 1:
                    bundle_name = f"Bottle - {ep}"
                else:
                    bundle_name = f"{remainder} bottles - {ep}"
                add_rule(
                    world.get_location(f"{ep} - Vault"),
                    lambda state, bn=bundle_name: state.has(bn, player)
                )

        add_rule(
            world.get_location("Menace from the North, Eh! - 30 bottles collected"),
            lambda state: (
                state.has("Paraglider", player) or
                state.has("Feral Pounce", player) or
                state.has("Mega Jump", player)
            )
        )
        add_rule(
            world.get_location("Anatomy for Disaster - 30 bottles collected"),
            lambda state: (
                state.has("Feral Pounce", player) or
                state.has("Mega Jump", player)
            )
        )

    # Putting ThiefNet stuff out of logic, to make early game less slow.
    # Divides the items into 8 groups of 3. First groups requires 2 episodes
    # items to be in logic, second group requires 4, etc.
    for i in range(1,25):
        episode_items_n = ceil(i/3)*2
        add_rule(
            world.get_location(f"ThiefNet {i}"),
            lambda state: (
                state.has_group("Episode", player, episode_items_n)
            )
        )


    if world.options.goal.value > 5:
        victory_condition = [
            "The Black Chateau - Operation: Thunder Beak",
            "The Predator Awakens - Operation: Wet Tiger",
            "A Tangled Web - Operation: High Road",
            "Menace from the North, Eh! - Operation: Canada Games",
            "Anatomy for Disaster - Carmelita's Gunner/Defeat Clock-la"
        ][world.options.goal.value]

        victory_location = world.multiworld.get_location(victory_condition, world.player)
        victory_location.address = None
        victory_location.place_locked_item(world.create_event("Victory"))
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    elif world.options.goal.value == 5:
        def access_rule(state: CollectionState):
            victory_conditions = [
                "The Black Chateau - Operation: Thunder Beak",
                "The Predator Awakens - Operation: Wet Tiger",
                "A Tangled Web - Operation: High Road",
                "Menace from the North, Eh! - Operation: Canada Games",
                "Anatomy for Disaster - Carmelita's Gunner/Defeat Clock-la"
            ]

            checked = state.locations_checked

            return all(
                cond in checked
                for cond in victory_conditions
            )

        world.multiworld.completion_condition[world.player] = access_rule

    elif world.options.goal.value == 6:
        world.multiworld.completion_condition[world.player] = lambda state: state.has_group(
            "Clockwerk Part",
            world.player,
            world.options.required_keys_goal.value
        )