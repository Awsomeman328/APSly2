from typing import Dict, Optional, Mapping, Any, List
import typing
import logging
import random

from BaseClasses import Item, ItemClassification
from Options import OptionError
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import (
    Component,
    Type,
    components,
    launch_subprocess,
    icon_paths,
)

from .Sly2Options import Sly2Options, StartingEpisode
from .Regions import create_regions
from .data.Items import item_dict, item_groups, Sly2Item
from .data.Locations import location_dict, location_groups
from .ItemPool import gen_pool
from .Rules import set_rules


## Client stuff
def run_client():
    from .Sly2Client import launch_client
    launch_subprocess(launch_client, name="Sly2Client")

icon_paths["sly2_ico"] = f"ap:{__name__}/icon.png"
components.append(
    Component("Sly 2 Client", func=run_client, component_type=Type.CLIENT, icon="sly2_ico")
)


## The world
class Sly2Web(WebWorld):
    game = "Sly 2: Band of Thieves"


class Sly2World(World):
    """
    Sly 2: Band of Thieves is a 2004 stealth action video game developed by
    Sucker Punch Productions and published by Sony Computer Entertainment for
    the PlayStation 2.
    """

    game = "Sly 2: Band of Thieves"
    web = Sly2Web()

    options_dataclass = Sly2Options
    options: Sly2Options
    topology_present = True

    item_name_to_id = {item.name: item.code for item in item_dict.values()}
    item_name_groups = item_groups
    location_name_to_id = {
        location.name: location.code for location in location_dict.values()
    }
    location_name_groups = location_groups

    thiefnet_costs: List[int] = []

    def generate_early(self) -> None:
        opt = self.options
        if opt.episode_8_keys and opt.required_keys > opt.keys_in_pool:
            raise OptionError(
                f"Episode 8 requires {opt.required_keys} keys but only {opt.keys_in_pool} keys in pool"
            )

        if opt.episode_8_keys and (
            opt.starting_episode == StartingEpisode.option_Anatomy_for_Disaster
        ):
            raise OptionError(
                f"Incompatible options: Episode 8 Keys and Starting Episode: {opt.starting_episode}"
            )

        if (
            (opt.bottle_item_bundle_size == 0 and opt.bottle_location_bundle_size != 0) or
            (opt.bottle_item_bundle_size != 0 and opt.bottle_location_bundle_size == 0)
        ):
            raise OptionError(
                f"Bottle item bundle size and bottle location bundle size should either both be zero or both be non-zero"
            )

        thiefnet_min = self.options.thiefnet_minimum.value
        thiefnet_max = self.options.thiefnet_maximum.value
        self.thiefnet_costs = [
            random.randint(thiefnet_min,thiefnet_max)
        ]


    def get_filler_item_name(self) -> str:
        return random.choice(list(self.item_name_groups["Filler"]))

    def create_regions(self) -> None:
        create_regions(self)

    def create_item(
        self, name: str, override: Optional[ItemClassification] = None
    ) -> Item:
        item = item_dict[name]

        if override is not None:
            return Sly2Item(name, override, item.code, self.player)

        return Sly2Item(name, item.classification, item.code, self.player)

    def create_event(self, name: str):
        return Sly2Item(name, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        items_to_add = gen_pool(self)

        self.multiworld.itempool += items_to_add

    def set_rules(self) -> None:
        set_rules(self)

    def get_options_as_dict(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "starting_episode",
            "goal",
            "episode_8_keys",
            "required_keys",
            "keys_in_pool",
            "include_tom",
            "include_mega_jump",
            "coins_minimum",
            "coins_maximum",
            "thiefnet_minimum",
            "thiefnet_maximum",
            "bottle_location_bundle_size",
            "bottle_item_bundle_size",
            "skip_intro"
        )

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.get_options_as_dict()
        slot_data["thiefnet_costs"] = self.thiefnet_costs

        return slot_data