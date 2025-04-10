import typing

from worlds.generic.Rules import add_rule

if typing.TYPE_CHECKING:
    from . import Sly2World

def set_rules(world: "Sly2World"):
    player = world.player

    add_rule(
        world.get_location("A Tangled Web - Crystal Vase"),
        lambda state: state.has("Paraglider", player)
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

    victory_condition = [
        "The Black Chateau - Operation: Thunder Beak",
        "The Predator Awakens - Operation: Wet Tiger",
        "A Tangled Web - Operation: High Road",
        "Menace from the North, Eh! - Operation: Canada Games",
        "Anatomy for Disaster - Carmelita's Gunner"
    ][world.options.goal.value]

    victory_location = world.multiworld.get_location(victory_condition, world.player)
    victory_location.address = None
    victory_location.place_locked_item(world.create_event("Victory"))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)