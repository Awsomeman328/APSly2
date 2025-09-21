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
    bottlesanity = world.options.bottlesanity
    if bottle_n != 0:
        bundle_count = 30//bottle_n
        remainder = 30%bottle_n
        if world.options.include_vaults:
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

        if world.options.bottle_location_bundle_size.value == 1 and bottlesanity:
            add_rule(
                world.get_location("Menace from the North, Eh! - Bottle #04"),
                lambda state: (
                    state.has("Paraglider", player) or
                    state.has("Mega Jump", player) or
                    state.has("Feral Pounce", player)
                )
            )
            add_rule(
                world.get_location("Anatomy for Disaster - Bottle #03"),
                lambda state: (
                    state.has("Feral Pounce", player) or
                    state.has("Mega Jump", player)
                )
            )
        else:
            add_rule(
                world.get_location("Menace from the North, Eh! - 30 bottles collected"),
                lambda state: (
                    state.has("Paraglider", player) or
                    state.has("Mega Jump", player) or
                    state.has("Feral Pounce", player)
                )
            )
            add_rule(
                world.get_location("Anatomy for Disaster - 30 bottles collected"),
                lambda state: (
                    state.has("Feral Pounce", player) or
                    state.has("Mega Jump", player)
                )
            )

    # TODO: Refactor this (and anywhere else in the code where this logic needs to be 
    # changed) to use the new user defined variables from the yaml file as follows.
    # 
    # thiefnet_groups_size will determine the size of each group (default 3) while 
    # thiefnet_episode_items_required will determine how many additional progressive 
    # episode items are required for each group (default 4, though the original of 2 can 
    # still be fine). If the total number of episodes required goes above 27, then clamp 
    # the episode requirement to 27 for that group and each group afterward.
    # 
    # (Got 27 by [6Eps*4Days + 3Days_for_Ep4] and excluding Ep8's Days as depending on user 
    # settings they can be excluded from being generated.)
    # 
    # Also change the starting group to require either 0 or 1 episode items to be in logic. 
    # (Either way, check the yaml file to ensure the mention of this part of the logic is
    # either accurate, or remove it if it is decided that we won't do this change. Or it's 
    # also possible to make this a user controlled variable too.)

    # Putting ThiefNet stuff out of logic, to make early game less slow.
    # Divides the items into 8 groups of 3. First groups requires 2 episodes
    # items to be in logic, second group requires 4, etc.
    for i in range(1,25):
        episode_items_n = ceil(i/3)*2
        add_rule(
            world.get_location(f"ThiefNet {i:02}"),
            lambda state, n=episode_items_n: (
                state.has_group("Episode", player, n)
            )
        )


    if world.options.goal.value < 5:
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

            return all(
                world.multiworld.get_location(cond,world.player).access_rule(state)
                for cond in victory_conditions
            )

        world.multiworld.completion_condition[world.player] = access_rule

    elif world.options.goal.value == 6:
        world.multiworld.completion_condition[world.player] = lambda state: state.has_group(
            "Clockwerk Part",
            world.player,
            world.options.required_keys_goal.value
        )