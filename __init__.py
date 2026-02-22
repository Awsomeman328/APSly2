from typing import Dict, Optional, Mapping, Any, List, ClassVar, TextIO
import logging
from math import ceil
import inspect

from BaseClasses import Item, ItemClassification
from Options import OptionError
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import (
    Component,
    Type,
    components,
    launch_subprocess,
    launch,
    icon_paths,
)

from .Sly2Options import Sly2Options, StartingEpisode, sly2_option_groups
from .Regions import create_regions
from .data.Items import item_dict, item_groups, Sly2Item
from .data.Locations import location_dict, location_groups
from .data.Constants import EPISODES, LOOT, ENEMIES, PICKPOCKET_LOOT_TABLE_CHANCES
from .ItemPool import gen_pool
from .Rules import set_rules


## Client stuff
def run_client():
    from .Sly2Client import launch_client
    launch(launch_client, name="Sly2Client")

icon_paths["sly2_ico"] = f"ap:{__name__}/icon.png"
components.append(
    Component("Sly 2 Client", func=run_client, component_type=Type.CLIENT, icon="sly2_ico")
)


## UT Stuff
def map_page_index(episode: str) -> int:
    mapping = {k: i for i,k in enumerate(EPISODES.keys())}

    return mapping.get(episode,0)

## The world
class Sly2Web(WebWorld):
    game = "Sly 2: Band of Thieves"
    option_groups = sly2_option_groups


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
    loot_table: dict[str, list[tuple[int,bool,int]]] = {}

    # this is how we tell the Universal Tracker we want to use re_gen_passthrough
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    # and this is how we tell Universal Tracker we don't need the yaml
    ut_can_gen_without_yaml = True

    # For setting up the maps for UT
    tracker_world: ClassVar = {
        "map_page_folder" : "tracker",
        "map_page_maps" : "maps.json",
        "map_page_locations" : [
            "locations/the_black_chateau.json",
            "locations/a_starry_eyed_encounter.json",
            "locations/the_predator_awakes.json",
            "locations/jailbreak.json",
            "locations/a_tangled_web.json",
            "locations/he_who_tames_the_iron_horse.json",
            "locations/anatomy_for_disaster.json",
            "locations/menace_from_the_north_eh.json"
        ],
        "map_page_setting_key": "Slot:{player}:Episode",
        "map_page_index": map_page_index
    }

    def validate_options(self, opt: Sly2Options):
        # This part is in order to get a better, more representative sample
        # from the fuzzer. Any yaml with a bunch of random values _should_ be
        # called with permissive_yaml on.
        generation_caller = inspect.stack()[6]
        if generation_caller.function == "call_generate":
            opt.permissive_yaml.value = True

        if opt.goal.value == 7 and not opt.include_vaults.value:
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    "The \"All Vaults\" goal requires that include_vaults be turned on. "+
                    "Turning on include_vaults"
                )
                opt.include_vaults.value = True
            else:
                raise OptionError(
                    "The \"All Vaults\" goal requires that include_vaults be turned on. "
                )

        if opt.episode_8_keys.value != 3 and opt.required_keys_episode_8 > opt.keys_in_pool:
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Episode 8 requires {opt.required_keys_episode_8} keys but only {opt.keys_in_pool} keys in pool. "+
                    "Increasing number of keys in pool."
                )
                opt.keys_in_pool.value = opt.required_keys_episode_8.value
            else:
                raise OptionError(
                    f"Episode 8 requires {opt.required_keys_episode_8} keys but only {opt.keys_in_pool} keys in pool."
                )

        if opt.goal == 6 and opt.required_keys_goal > opt.keys_in_pool:
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Clockwerk Hunt goal requires {opt.required_keys_goal} keys but only {opt.keys_in_pool} keys in pool. "+
                    "Increasing number of keys in pool."
                )
                opt.keys_in_pool.value = opt.required_keys_goal.value
            else:
                raise OptionError(
                    f"Clockwerk Hunt goal requires {opt.required_keys_goal} keys but only {opt.keys_in_pool} keys in pool"
                )

        if opt.episode_8_keys.value in [0,2] and (
            opt.starting_episode == StartingEpisode.option_Anatomy_for_Disaster
        ):
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Incompatible options: Episode 8 Keys: ({opt.episode_8_keys}) and Starting Episode: ({opt.starting_episode}). "+
                    "Changing Episode 8 Keys to \"Last Section\"."
                )
                opt.episode_8_keys.value = 1
            else:
                raise OptionError(
                    f"Incompatible options: Episode 8 Keys: ({opt.episode_8_keys}) and Starting Episode: ({opt.starting_episode})"
                )

        if (
            (opt.bottle_item_bundle_size == 0 and opt.bottle_location_bundle_size != 0) or
            (opt.bottle_item_bundle_size != 0 and opt.bottle_location_bundle_size == 0)
        ):
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Bottle item bundle size and bottle location bundle size should either both be zero or both be non-zero. "+
                    "Setting both to 0."
                )
                opt.bottle_item_bundle_size.value = 0
                opt.bottle_location_bundle_size.value = 0
            else:
                raise OptionError(
                    f"Bottle item bundle size and bottle location bundle size should either both be zero or both be non-zero"
                )

        if opt.coins_maximum < opt.coins_minimum:
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Coins minimum cannot be larger than maximum (min: {opt.coins_minimum}, max: {opt.coins_maximum}). "+
                    "Swapping values."
                )
                temp = opt.coins_minimum.value
                opt.coins_minimum.value = opt.coins_maximum.value
                opt.coins_maximum.value = temp
            else:
                raise OptionError(
                    f"Coins minimum cannot be larger than maximum (min: {opt.coins_minimum}, max: {opt.coins_maximum})"
                )

        if opt.thiefnet_maximum < opt.thiefnet_minimum:
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    f"Thiefnet minimum cannot be larger than maximum (min: {opt.thiefnet_minimum}, max: {opt.thiefnet_maximum}). "+
                    "Swapping values."
                )
                temp = opt.thiefnet_minimum.value
                opt.thiefnet_minimum.value = opt.thiefnet_maximum.value
                opt.thiefnet_maximum.value = temp
            else:
                raise OptionError(
                    f"Thiefnet minimum cannot be larger than maximum (min: {opt.thiefnet_minimum}, max: {opt.thiefnet_maximum})"
                )

        if (opt.include_total_percentage.value == 0 and opt.include_episodes_percentage.value == 0 and
            not opt.episodes_as_locations and not opt.days_as_locations and not opt.jobs_as_locations and
            not opt.objectives_as_locations and not opt.tasks_as_locations):
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    "At least 1 of Episodes, Days, Jobs, Tasks, Objectives, Episode %, or Total % must be enabled as Locations. "+
                    "Enabling Jobs as Locations as the default"
                )
                opt.jobs_as_locations.value = True
            else:
                raise OptionError(
                    "At least 1 of Episodes, Days, Jobs, Tasks, Objectives, Episode %, or Total % must be enabled as Locations."
                )

        if (opt.episodes_as_items.value == 2 and opt.days_as_items.value == 2 and opt.jobs_as_items.value == 3
                #and opt.StartingCharacter.value == 0
            ):
            if opt.permissive_yaml:
                logging.warning(
                    f"{self.player_name}: " +
                    "At least 1 of Episodes, Days, Jobs, or Characters must be enabled as Items. (Characters not yet supported) "+
                    "Enabling Progressive Days as Items as the default"
                )
                opt.days_as_items.value = 0
            else:
                raise OptionError(
                    "At least 1 of Episodes, Days, Jobs, or Characters must be enabled as Items. (Characters not yet supported)"
                )

        # TODO: Validate that at least 1 of the options for Episodes, Days, Jobs, Tasks, Objectives, Episode%, or
        #  Total% as Locations is 'On', & that at least 1 of the options for Episodes, Days, Jobs, or Characters as
        #  Items is 'On'. If Permissive if 'On' then just turn on Jobs as Locations & Days as Items as the default.
        #  (Episode%, Total%, & Characters might not be implemented yet.)

        # TODO: Count the number of episodes, days, jobs, tasks, checkpoints, photographs, & story stealings there are
        #  and include them in the count below. Don't forget to account for the various yaml options for all of these,
        #  both the generic options of if they're enabled or not & the more specific ones about:
        #  -If Prologue is being counted or not
        #  -If Eps 4 & 8 will have 3 Days or 4
        #  -If Compound-Jobs will count as multiple Jobs or not
        #  -etc.

        # Checking number of locations and items
        n_locations = (
            24 + # ThiefNet
            (24 if opt.include_treasures else 0) +
            (8 if opt.include_vaults else 0)
        )
        if opt.episodes_as_locations:
            n_locations += (9 if opt.include_prologue else 8)
        if opt.days_as_locations:
            n_locations += (1 if opt.include_prologue else 0)
            match opt.episodes_4_and_8_num_days:
                case 0:
                    n_locations += 30
                case 1 | 2:
                    n_locations += 31
                case 3:
                    n_locations += 32
        if opt.jobs_as_locations:
            n_locations += (70 if opt.include_prologue else 69)
            if (opt.compound_jobs_as_multiple_jobs == 1 or
                opt.compound_jobs_as_multiple_jobs) == 2:
                n_locations += 6
        if opt.objectives_as_locations:
            n_locations += (158 if opt.include_prologue else 155)
        if opt.tasks_as_locations:
            n_locations += (795 if opt.include_prologue else 779)
        if opt.checkpoints_as_locations:
            n_locations += (307 if opt.include_prologue else 304)
        n_locations += (54 if opt.include_photography else 0)
        match opt.include_pickpocketing:
            case 0:
                n_locations += 30
            case 1:
                n_locations += 82
            case 2:
                n_locations += 30 + 82
        if opt.bottle_location_bundle_size != 0:
            n_locations += ceil(30/opt.bottle_location_bundle_size)*8
        if opt.goal < 5:
            n_locations -= 1 # If the goal is a check, there can't be an item there

        using_parts = opt.episode_8_keys.value != 3 or opt.goal.value == 6
        n_items = (
            32 + # Power-ups
            int(opt.include_tom.value) +
            int(opt.include_time_rush.value) +
            int(opt.include_mega_jump.value) +
            #26 + # Episodes (27 without ep8, minus the one you start with)
            (opt.keys_in_pool.value if using_parts else 0)
        )

        if opt.include_gadget_buttons == 0:
            n_items += 3
        elif opt.include_gadget_buttons == 1:
            n_items += 9

        if opt.episode_8_keys.value in [0,1]:
            n_items += 3
        elif opt.episode_8_keys.value == 3:
            n_items += 4

        # For each of these, we minus 1 to exclude the one you start with. We also don't count Prologue.
        match opt.episodes_as_items:
            case 0 | 1:
                n_items += 7
        match opt.days_as_items:
            case 0 | 1:
                match opt.episodes_4_and_8_num_days:
                    case 0:
                        n_items += 29
                    case 1 | 2:
                        n_items += 30
                    case 3:
                        n_items += 31
        match opt.jobs_as_items:
            case 0 | 1 | 2:
                match opt.compound_jobs_as_multiple_jobs:
                    case 0 | 2:
                        n_items += 74
                    case 1 | 3:
                        n_items += 68


        if opt.bottle_item_bundle_size.value != 0:
            n_items += ceil(30/opt.bottle_item_bundle_size.value)*8

        # TODO: Utilize the 'YamlItemsAndLocationsHandling' Option to choose if we should
        #  try removing Items from our Item Pool, add more Locations for our world to check,
        #  or both.
        if n_items > n_locations:
            if not opt.permissive_yaml:
                raise OptionError(
                    f"More items than locations ({n_items} items; {n_locations} locations)"
                )
            logging.warning(
                f"{self.player_name}: " +
                f"More items than locations ({n_items} items; {n_locations} locations)\n"+
                "Adjusting Clockwerk part amounts."
            )
            overflow = n_items - n_locations
            if (opt.keys_in_pool.value - overflow < 1) or not using_parts:
                logging.warning(
                    f"{self.player_name}: " +
                    "Too many items, even when reducing Clockwerk part amounts."
                )
                n_items = n_items - opt.keys_in_pool.value + 1
                raise OptionError(
                    "There are more items than locations"+
                    f"({n_items} items; {n_locations} locations)"
                )
            opt.keys_in_pool.value = opt.keys_in_pool.value - overflow
            opt.required_keys_episode_8.value = min(
                opt.required_keys_episode_8.value,
                opt.keys_in_pool.value
            )
            opt.required_keys_goal.value = min(
                opt.required_keys_goal.value,
                opt.keys_in_pool.value
            )

    def randomize_loot_table(self) -> dict[str, list[tuple[int,bool,int]]]:
        all_locations = [loc for locations in LOOT.values() for loc in locations]
        loot_table = {loot: [] for loot in LOOT.keys()}

        # First make sure each item is at least one place
        for loot in loot_table.keys():
            loc_index = self.random.randint(0,len(all_locations)-1)
            loc = all_locations.pop(loc_index)
            loot_table[loot].append(loc)

        # Then randomly distribute the others
        for loc in all_locations:
            loot = self.random.choice(list(loot_table.keys()))
            loot_table[loot].append(loc)

        return loot_table

    def generate_early(self) -> None:

        # implement .yaml-less Universal Tracker support
        if hasattr(self.multiworld, "generation_is_fake"):
            if hasattr(self.multiworld, "re_gen_passthrough"):
                # I'm doing getattr purely so pylance stops being mad at me
                re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough")

                if "Sly 2: Band of Thieves" in re_gen_passthrough:
                    slot_data = re_gen_passthrough["Sly 2: Band of Thieves"]
                    self.options.permissive_yaml.value = slot_data["permissive_yaml"]
                    self.options.logic_difficulty_level = slot_data["logic_difficulty_level"]

                    self.options.starting_episode.value = slot_data["starting_episode"]
                    self.options.starting_day.value = slot_data["starting_day"]
                    self.options.starting_job.value = slot_data["starting_job"]
                    #self.options.starting_character.value = slot_data["starting_character"]

                    self.options.goal.value = slot_data["goal"]

                    self.options.keys_in_pool.value = slot_data["keys_in_pool"]
                    self.options.episode_8_keys.value = slot_data["episode_8_keys"]
                    self.options.required_keys_episode_8.value = slot_data["required_keys_episode_8"]
                    self.options.required_keys_goal.value = slot_data["required_keys_goal"]

                    self.options.include_prologue = slot_data["include_prologue"]
                    self.options.episodes_4_and_8_num_days.value = slot_data["episodes_4_and_8_num_days"]
                    self.options.compound_jobs_as_multiple_jobs = slot_data["compound_jobs_as_multiple_jobs"]

                    self.options.episodes_as_items = slot_data["episodes_as_items"]
                    self.options.days_as_items = slot_data["days_as_items"]
                    self.options.jobs_as_items = slot_data["jobs_as_items"]

                    self.options.include_total_percentage = slot_data["include_total_percentage"]
                    self.options.include_episodes_percentage = slot_data["include_episodes_percentage"]
                    self.options.episodes_as_locations = slot_data["episodes_as_locations"]
                    self.options.days_as_locations = slot_data["days_as_locations"]
                    self.options.jobs_as_locations = slot_data["jobs_as_locations"]
                    self.options.objectives_as_locations = slot_data["objectives_as_locations"]
                    self.options.tasks_as_locations = slot_data["tasks_as_locations"]
                    self.options.checkpoints_as_locations = slot_data["checkpoints_as_locations"]

                    self.options.include_prologue = slot_data["include_gadget_buttons"]
                    self.options.include_mega_jump.value = slot_data["include_mega_jump"]
                    self.options.include_tom.value = slot_data["include_tom"]
                    self.options.include_time_rush.value = slot_data["include_time_rush"]

                    self.options.coins_minimum.value = slot_data["coins_minimum"]
                    self.options.coins_maximum.value = slot_data["coins_maximum"]

                    self.options.include_treasures = slot_data["include_treasures"]
                    self.options.include_vaults.value = slot_data["include_vaults"]
                    self.options.include_photography = slot_data["include_photography"]
                    self.options.include_pickpocketing.value = slot_data["include_pickpocketing"]

                    self.options.small_guard_loot_chance.value = slot_data["small_guard_loot_chance"]
                    self.options.large_guard_loot_chance.value = slot_data["large_guard_loot_chance"]
                    self.options.loot_table_distribution.value = slot_data["loot_table_distribution"]
                    self.options.randomize_loot.value = slot_data["randomize_loot"]
                    self.loot_table = slot_data["loot_table"]

                    self.options.thiefnet_minimum.value = slot_data["thiefnet_minimum"]
                    self.options.thiefnet_maximum.value = slot_data["thiefnet_maximum"]
                    self.thiefnet_costs = slot_data["thiefnet_costs"]
                    self.options.scout_thiefnet.value = slot_data["scout_thiefnet"]

                    self.options.bottle_item_bundle_size.value = slot_data["bottle_item_bundle_size"]
                    self.options.bottle_location_bundle_size.value = slot_data["bottle_location_bundle_size"]
                    self.options.bottlesanity.value = slot_data["bottlesanity"]
            return

        self.validate_options(self.options)

        thiefnet_min = self.options.thiefnet_minimum.value
        thiefnet_max = self.options.thiefnet_maximum.value
        self.thiefnet_costs = sorted([
            self.random.randint(thiefnet_min,thiefnet_max)
            for _ in range(24)
        ])

        if self.options.randomize_loot:
            self.loot_table = self.randomize_loot_table()
        else:
            self.loot_table = LOOT

    def get_filler_item_name(self) -> str:
        # Currently just coins
        # TODO: Eventually make this compatible w/ HP as Filler items to0
        return self.random.choice(list(self.item_name_groups["Filler"]))

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
            "permissive_yaml",
            "yaml_items_and_locations_handling",
            "logic_difficulty_level",

            "starting_episode",
            "starting_day",
            "starting_job",

            "goal",

            "keys_in_pool",
            "episode_8_keys",
            "required_keys_episode_8",
            "required_keys_goal",

            "include_prologue",
            "episodes_4_and_8_num_days",
            "compound_jobs_as_multiple_jobs",

            "episodes_as_items",
            "days_as_items",
            "jobs_as_items",

            "include_total_percentage",
            "include_episodes_percentage",
            "episodes_as_locations",
            "days_as_locations",
            "jobs_as_locations",
            "objectives_as_locations",
            "tasks_as_locations",
            "checkpoints_as_locations",

            "include_gadgets_buttons",
            "include_mega_jump",
            "include_tom",
            "include_time_rush",

            "coins_minimum",
            "coins_maximum",

            "include_treasures",
            "include_vaults",
            "include_photography",
            "include_pickpocketing",

            "small_guard_loot_chance",
            "large_guard_loot_chance",
            "loot_table_distribution",
            "randomize_loot",

            "thiefnet_minimum",
            "thiefnet_maximum",
            "scout_thiefnet",

            "bottle_location_bundle_size",
            "bottle_item_bundle_size",
            "bottlesanity",

            # "skip_intro"
        )

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.get_options_as_dict()
        slot_data["thiefnet_costs"] = self.thiefnet_costs
        slot_data["loot_table"] = self.loot_table
        slot_data["skip_intro"] = True
        slot_data["world_version"] = self.world_version

        return slot_data

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        spoiler_text = "\n====== Sly 2 ThiefNet Costs ======"
        thiefnet_cost_text = "\n".join(
            f"- ThiefNet {i+1:02}: {cost} coins"
            for i, cost in enumerate(self.thiefnet_costs)
        )
        spoiler_text += "\n"+thiefnet_cost_text
        spoiler_text += "\n======== Sly 2 Loot Table ========"
        for i in range(8):
            spoiler_text += f"\n== Episode {i+1} =="
            for j in range(2):
                enemy = ENEMIES[i][j]
                loot = []
                for k in range(1,7):
                    for loot_name, loot_locations in self.loot_table.items():
                        if (i+1,bool(j),k) in loot_locations:
                            loot.append(loot_name)
                            break
                loot_odds = PICKPOCKET_LOOT_TABLE_CHANCES[self.options.loot_table_distribution-1]
                loot_text = ", ".join(f"{l} ({loot_odds[i]}%)" for i, l in enumerate(loot))
                spoiler_text += f"\n- {enemy}: {loot_text}"

        spoiler_text += "\n=================================="

        spoiler_handle.write(spoiler_text)
