from Options import (
    DeathLink,
    StartInventoryPool,
    PerGameCommonOptions,
    Choice,
    Toggle,
    DefaultOnToggle,
    Range,
    OptionGroup
)
from dataclasses import dataclass

class PermissiveYaml(Toggle):
    """
    If permissive yaml is on, incompatible yaml options will be changed to more
    suitable ones. If turned off, these yaml options will throw an error and
    cause generation to halt.

    This is intended for yamls with random values. If you're not randomizing
    any options, it's recommended that you turn permissive yaml off.
    """
    display_name = "Permissive Yaml"


class StartingEpisode(Choice):
    """
    Select which episode to start with. Starting with Anatomy for disaster
    is not compatible with the "first section" and "whole episode" options for
    "Episode 8 Keys".
    """
    display_name = "Starting Episode"
    option_The_Black_Chateau = 0
    option_A_Starry_Eyed_Encounter = 1
    option_The_Predator_Awakens = 2
    option_Jailbreak = 3
    option_A_Tangled_Web = 4
    option_He_Who_Tames_the_Iron_Horse = 5
    option_Menace_from_the_North_Eh = 6
    option_Anatomy_for_Disaster = 7
    default = 0


# This is an option planned for the future, to be able to control which
# characters are playable and turn them into Items for them to basically act as
# keys to Jobs that require playing as them (Based on the Sly 3 implementation).
#
# One other possible idea is to make these unlocks be Episode specific, so that
# "The Black Chateau - Sky" is different & separate from "A Starry Eyed Encounter - Sly".
# But THIS might be a bit TOO crazy.
#class StartingCharacter(Choice):
#    """
#    Select which character(s) to start with. Starting with Sly or Murray is not
#    compatible with the Jailbreak option for "Starting Episode".
#    """
#    display_name = "Starting Character"
#    option_All = 0
#    option_Sly = 1
#    Option_Bentley = 2
#    option_Murray = 3
#    default = 0


# This is an option planned for the future, to have multiple levels of logic that
# will give either more or less Gadgets to help complete certain locations.
# Higher difficulty levels will also assume that you know how to perform some
# speedrunning tricks, like triple-jumping.
#
# This setting will 100% require the input of the Sly 2 APWorld community to help
# determine where we want to draw the lines for each of these difficulties.
#class LogicDifficultyLevel(Choice):
#    """
#    Select which difficulty level for the logic to use.
#     - Easy: Very forgiving, trying to ensure that you have various Gadgets to help in various locations.
#     - Normal: The default difficulty ensures that you have the bare minimum Gadgets to complete your locations.
#     - Hard: The hardest "regular" difficulty that will expect you to know of non-glitch tricks to compensate for fewer Gadgets.
#     - Glitched: The most unforgiving logic, requiring the use of glitches/speedrunning tricks, like Triple-Jumping.
#    """
#    display_name = "Logic Difficulty Level"
#    option_easy = 0
#    option_normal = 1
#    option_hard = 2
#    option_glitched = 3
#    default = 1


# Other possible goals to consider adding:
# -Collecting all Pickpocket Loot & Pedestal Treasures,
# -Stealing Everything (the previous goal plus the vaults,
#   ... may also include Story-Based Stealing as well),
# -Finishing all Operations (plus Clock-La),
# -and completing all Jobs/Missions (100%).
class Goal(Choice):
    """
    Select which goal will be your game's victory condition. The options are:
     - Defeating a specific boss to goal. (Clockla is the default.)
     - Defeating all bosses to goal.
     - Opening all Secret Vaults to goal by collecting all Clue Bottle items.
     - Collect a certain number of Clockwerk Parts/keys in the Clockwerk Hunt to goal.
    """
    display_name = "Goal"
    option_Dimitri = 0
    option_Rajan = 1
    option_The_Contessa = 2
    option_Jean_Bison = 3
    option_ClockLa = 4
    option_All_Bosses = 5
    option_Clockwerk_Hunt = 6
    option_All_Vaults = 7
    default = 4


class KeysInPool(Range):
    """
    How many Clockwerk parts are added to the pool. This number cannot be
    lower than the required number of keys, for either Clockwerk Hunt or
    Episode 8 unlock. No Clockwerk parts will be added  if Episode 8 Keys
    and Clockwerk Hunt are both off.
    """
    display_name = "Clockwerk Parts in Pool"
    range_start = 1
    range_end = 100
    default = 10

# TODO: Look into all of the Choice based Options here that lists an "option_Off"
#  choice and make all of the "Off" options values equal 0. Then go through the
#  rest of the code to make sure that everything else is still being targeting
#  the correct option(s).

class Episode8Keys(Choice):
    """
    Whether to have Anatomy for Disaster be unlocked with a number of Clockwerk
    parts, rather than with a single item like the other episodes.

    - First section: Unlock only the first section of Anatomy for Disaster with
      the required amount of Clockwerk Parts.
    - Last section: Unlock only the final mission of Anatomy for Disaster with
      the required amount of Clockwerk Parts.
    - Whole episode: Unlock every mission in Anatomy for Disaster with the
      required amount of Clockwerk Parts.
    - Off: Unlock Anatomy for Disaster with progressive episode items, like the
      other episodes.
    """
    display_name = "Episode 8 Keys"
    option_First_section = 0
    option_Last_section = 1
    option_Whole_episode = 2
    option_Off = 3
    default = 0


class RequiredKeys(Range):
    """
    How many Clockwerk parts you need to unlock Anatomy for Disaster, if
    Episode 8 Keys is turned on.
    """
    display_name = "Episode 8 Required Keys"
    range_start = 1
    range_end = 100
    default = 10


class RequiredKeysGoal(Range):
    """
    How many Clockwerk parts you need to goal, if goal objective is Clockwerk Hunt
    """
    display_name = "Goal Required Keys"
    range_start = 1
    range_end = 100
    default = 10


class IncludePrologue(Toggle):
    """
    Whether the Cairo Prologue should be included as checks or skipped.
    Requires at least 1 of either Episodes, Days, Jobs, Objectives, Tasks, or
    Checkpoints to be enabled as checks for this to have any effect.
    """
    display_name = "Include Prologue"


class Episodes4And8NumDays(Choice):
    """
    How many Days will Episodes 4 & 8 have as both Items & Locations.
    *WARNING*: Setting Episode 4 to four days will make it MUCH harder to progress
    past the first Job in Episode 4, especially if it is your starting Episode.
    """
    display_name = "Episodes 4 and 8 Num Days"
    option_Three_Days_Each = 0
    option_Three_Days_Then_Four_Days = 1
    option_Four_Days_Then_Three_Days = 2
    option_Four_Days_Each = 3
    default = 1


# TODO: Finish making this Option
class CompoundJobs():
    """
    Whether to handle "Compound-Jobs" as multiple Jobs or as only a single Job.
    Jobs this affects:
    - Operation: Thunder Beak // Printing Press Duel
    - Operation: Hippo Drop (Bomb the Bridge, Tango with Carmelita, Clear the Way for Murray)
    - Operation: Wet Tiger // Showdown with Rajan
    - Operation: Canada Games // Brains over Brawn
    - Carmelita's Gunner // Showdown with Clock-La
    """


class EpisodesAsItems(Choice):
    """
    Add every Episode to the pool. You can choose if you want to include the
    Prologue or not & if you want your Episode Items to be progressive or not,
    meaning you always unlock each of your Episodes in order.
    """
    display_name = "Episodes As Items"
    option_Progressive_Episodes = 0
    option_Nonprogressive_Episodes = 1
    option_Off = 2
    default = 2


class DaysAsItems(Choice):
    """
    Add every Episode to the pool. You can choose if you want your Day Items to
    be progressive or not, meaning you always unlock each Day in order for that Episode.
    """
    display_name = "Days As Items"
    option_Progressive_Days = 0
    option_Nonprogressive_Days = 1
    option_Off = 2
    default = 0


class JobsAsItems(Choice):
    """
    Add every Job to the pool. You can choose if you want your Job Items to
    be progressive or not, and if so whether they'll progress on a per-Episode
    basis or on a per-Day basis.
    """
    display_name = "Jobs As Items"
    option_Progressive_Jobs_Per_Episode = 0
    option_Progressive_Jobs_Per_Day = 1
    option_Nonprogressive_Jobs = 2
    option_Off = 3
    default = 3


# For the following 2 Options, I'm not sure if it makes more sense to have the
# number entered here to mean how many total checks to add or for it to mean the
# interval between each check; basically should a higher or lower number mean
# fewer or more checks? I'm tempted to treat it the same way as how the Bottles
# work, so lower number means more checks.
class IncludeTotalPercentage(Range):
    """
    Whether to include your game's total% completion as checks. Set to 0 to disable.
    TODO: Add proper description of what higher/lower values do here.
    """
    display_name = "Include Total Percentage"
    range_start = 0
    range_end = 100
    default = 0


class IncludeEpisodesPercentages(Range):
    """
    Whether to include each Episode's % completion as checks. Set to 0 to disable.
    TODO: Add proper description of what higher/lower values do here.
    """
    display_name = "Include Episodes Percentages"
    range_start = 0
    range_end = 100
    default = 0


class EpisodesAsLocations(Toggle):
    """
    Whether to include completing Episodes as checks.
    """
    display_name = "Episodes As Locations"


class DaysAsLocations(Toggle):
    """
    Whether to include completing Days as checks.
    """
    display_name = "Days As Locations"


class JobsAsLocations(DefaultOnToggle):
    """
    Whether to include completing Jobs as checks.
    """
    display_name = "Jobs As Locations"


class TasksAsLocations(Toggle):
    """
    Whether to include completing Tasks as checks.
    *WARNING*: These locations are impossible to see in-game, thus it is HIGHLY
    recommended that you use a tracker to display what these are to you.
    """
    display_name = "Tasks As Locations"


class ObjectivesAsLocations(Toggle):
    """
    Whether to include completing Objectives as checks.
    """
    display_name = "Objectives As Locations"


class CheckpointsAsLocations(Toggle):
    """
    Whether to include reaching Checkpoints as checks.
    """
    display_name = "Checkpoints As Locations"


class IncludeMegaJump(Choice):
    """
    Add the Mega Jump ability/gadget to the pool. If set to "Required", then the
    "Mega-Jump Job" Mission in Episode 8 will require you to have this Gadget to
    unlock it rather than it being provided to you for the Mission.
    """
    display_name = "Include Mega Jump"
    option_False = 0
    option_True = 1
    option_Required = 2
    default = 0


class IncludeTOM(Toggle):
    """
    Add the TOM ability/gadget to the pool.
    """
    display_name = "Include TOM"


class IncludeTimeRush(Toggle):
    """
    Add the Time Rush ability/gadget to the pool.
    """
    display_name = "Include Time Rush"


class CoinsMinimum(Range):
    """
    The minimum number of coins you'll receive when you get a "Coins" filler
    item.
    """
    display_name = "Coins Minimum"
    range_start = 0
    range_end = 1000
    default = 50


class CoinsMaximum(Range):
    """
    The maximum number of coins you'll receive when you get a "Coins" filler
    item.
    """
    display_name = "Coins Maximum"
    range_start = 0
    range_end = 1000
    default = 200


class ThiefNetCostMinimum(Range):
    """
    The minimum number of coins items on ThiefNet will cost.
    """
    display_name = "ThiefNet Cost Minimum"
    range_start = 0
    range_end = 9999
    default = 200


class ThiefNetCostMaximum(Range):
    """
    The maximum number of coins items on ThiefNet will cost.
    """
    display_name = "ThiefNet Cost Maximum"
    range_start = 0
    range_end = 9999
    default = 2000


class IncludeTreasures(DefaultOnToggle):
    """
    Whether to include Pedestal Treasures as checks.
    """
    display_name = "Include Pedestal Treasures"


class IncludeVaults(DefaultOnToggle):
    """
    Whether to include vaults as checks.
    """
    display_name = "Include Vaults"


class IncludePhotography(Toggle):
    """
    Whether to include taking pictures as checks.
    """
    display_name = "Include Photography"


class IncludePickpocketing(Choice):
    """
    Whether to include pickpocketing as checks. This can include either
    - stealing loot from guards,
    - stealing Key-Items in Jobs,
    - or both.
    """
    display_name = "Include Pickpocketing"
    option_Only_Loot = 0
    option_Only_KeyItem = 1
    option_Both = 2
    option_Off = 3
    default = 3


class SmallGuardLootChance(Range):
    """
    The chance that any given small guard will have pick-pocketable loot.
    """
    display_name = "Small Guard Loot Chance"
    range_start = 1
    range_end = 100
    default = 20


class LargeGuardLootChance(Range):
    """
    The chance that any given large guard will have pick-pocketable loot.
    """
    display_name = "Large Guard Loot Chance"
    range_start = 1
    range_end = 100
    default = 40


class LootTableDistribution(Range):
    """
    How "evenly" the loot table chances will be distributed. By default, the 6
    pieces of loot a guard can carry will be distributed with the chances
    (30%/30%/15%/15%/5%/5%). A lower value will make first pieces of loot even
    more likely, and a higher value will flatten out the chances.
    """
    display_name = "Loot Table Distribution"
    range_start = 1
    range_end = 100
    default = 50


class RandomizeLoot(Toggle):
    """
    Whether to shuffle all pickpocketing loot locations. A guard could have the
    same piece of loot multiple times on their table, so there is no
    guaranteeing that each guard will have exactly 6 different pieces of loot.
    """
    display_name = "Randomize Loot"


class BottleLocationBundleSize(Range):
    """
    How many bottles you need to collect for each check. Set to 0 to disable
    bottles as checks.
    """
    display_name = "Bottle Location Bundle Sizes"
    range_start = 0
    range_end = 30
    default = 0


class BottleItemBundleSize(Range):
    """
    How many bottles you receive from an item. Set to 0 to disable bottles
    as items.
    """
    display_name = "Bottle Item Bundle Sizes"
    range_start = 0
    range_end = 30
    default = 0


class BottleSanity(DefaultOnToggle):
    """
    Each bottle is its own check, rather than counting the number of bottles
    collected. Only takes effect if bottle_location_bundle_size is 1.
    """
    display_name = "Bottlesanity"

# This is an option planned for the future, to be able to turn off LootSanity and
# to have loot be counted using one of a few other options: either as an overall
# total, or as total unique loot. However, for the initial implementation,
# LootSanity will just be on by default, along with the option of turning loot as
# locations off, similar to vaults.
#
# To see OTHER possible options related to loot being considered, check out what
# has been writen in pull request #3 for this game's AP on GitHub.
#class LootSanity(Choice):
#    """
#    Each piece of loot is its own check, rather than counting the number of
#    total loot collected.
#    """
#    display_name = "Lootsanity"

class ScoutThiefnet(DefaultOnToggle):
    """
    Whether to scout/hint ThiefNet checks. They will still be displayed in game.
    """
    display_name = "Scout Thiefnet"


class SkipIntro(DefaultOnToggle):
    """
    Whether the Cairo intro should be skipped.
    """
    display_name = "Skip Intro"


@dataclass
class Sly2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
    permissive_yaml: PermissiveYaml
    starting_episode: StartingEpisode
    # starting_character: StartingCharacter
    # logic_difficulty_level: LogicDifficultyLevel
    goal: Goal
    keys_in_pool: KeysInPool
    episode_8_keys: Episode8Keys
    required_keys_episode_8: RequiredKeys
    required_keys_goal: RequiredKeysGoal
    include_prologue: IncludePrologue
    episodes_4_and_8_num_days: Episodes4And8NumDays
    episodes_as_items: EpisodesAsItems
    days_as_items: DaysAsItems
    jobs_as_items: JobsAsItems
    include_total_percentage: IncludeTotalPercentage
    include_episodes_percentage: IncludeEpisodesPercentages
    episodes_as_locations: EpisodesAsLocations
    days_as_locations: DaysAsLocations
    jobs_as_locations: JobsAsLocations
    objectives_as_locations: ObjectivesAsLocations
    tasks_as_locations: TasksAsLocations
    checkpoints_as_locations: CheckpointsAsLocations
    include_mega_jump: IncludeMegaJump
    include_tom: IncludeTOM
    include_time_rush: IncludeTimeRush
    coins_minimum: CoinsMinimum
    coins_maximum: CoinsMaximum
    include_treasures: IncludeTreasures
    include_vaults: IncludeVaults
    include_photography: IncludePhotography
    include_pickpocketing: IncludePickpocketing
    small_guard_loot_chance: SmallGuardLootChance
    large_guard_loot_chance: LargeGuardLootChance
    loot_table_distribution: LootTableDistribution
    randomize_loot: RandomizeLoot
    thiefnet_minimum: ThiefNetCostMinimum
    thiefnet_maximum: ThiefNetCostMaximum
    bottle_location_bundle_size: BottleLocationBundleSize
    bottle_item_bundle_size: BottleItemBundleSize
    bottlesanity: BottleSanity
    # lootsanity:LootSanity
    scout_thiefnet: ScoutThiefnet
    # skip_intro: SkipIntro

sly2_option_groups = [
    OptionGroup("Goal",[
        Goal
    ]),
    OptionGroup("Clockwerk parts",[
        KeysInPool,
        Episode8Keys,
        RequiredKeys,
        RequiredKeysGoal
    ]),
    # It COULD be possible to combine the Episodes, Days, and Jobs options as a single choice that would control them
    #  as both Items and Locations (and just call them Include{X}), but I felt that doing so would likely be confusing.
    OptionGroup("Story Progression",[
        IncludePrologue,
        Episodes4And8NumDays,
        EpisodesAsItems,
        DaysAsItems,
        JobsAsItems,
        IncludeTotalPercentage,
        IncludeEpisodesPercentages,
        EpisodesAsLocations,
        DaysAsLocations,
        JobsAsLocations,
        TasksAsLocations,
        ObjectivesAsLocations,
        CheckpointsAsLocations
    ]),
    OptionGroup("Items",[
        IncludeTOM,
        IncludeMegaJump, # TODO: Add in the additional choice for requiring this Gadget for its specific Job.
        IncludeTimeRush,
        CoinsMinimum,
        CoinsMaximum,
        BottleItemBundleSize
    ]),
    OptionGroup("Locations",[
        ThiefNetCostMinimum,
        ThiefNetCostMaximum,
        IncludeTreasures,
        IncludeVaults,
        IncludePickpocketing, # TODO: Add in the additional choice for Story-Based Stealing.
        IncludePhotography,
        BottleLocationBundleSize,
        BottleSanity,
        ScoutThiefnet
    ]),
    OptionGroup("Pick-pocketing",[
        RandomizeLoot,
        SmallGuardLootChance,
        LargeGuardLootChance,
        LootTableDistribution
    ])
]
