from Options import (
    DeathLink,
    StartInventoryPool,
    PerGameCommonOptions,
    Choice,
    Toggle,
    DefaultOnToggle,
    Range,
    OptionSet,
    OptionGroup,
    Visibility
)
from dataclasses import dataclass

from .data.Constants import EPISODES

class PermissiveYaml(Toggle):
    """
    If permissive yaml is on, incompatible yaml options will be changed to more
    suitable ones. If turned off, these yaml options will throw an error and
    cause generation to halt.

    This is intended for yamls with random values. If you're not randomizing
    any options, it's recommended that you turn permissive yaml off.
    """
    display_name = "Permissive Yaml"


class YamlItemsAndLocationsHandling(Choice):
    """
    Hidden option.
    If 'Permissive Yaml' is on, then this option will determine how this world
    will attempt to resolve having more Items than Locations (if such a
    situation occurs).

    The main two choices are to either remove Items from the Item Pool or to
    add more Locations to this world, and it could be possible to attempt to
    do both. There are also likely other possible implementations that could
    be made and turned into choices to be placed here.
    """
    visibility = Visibility.none
    display_name = "Yaml Items and Locations Handling"
    option_Items = 0
    option_Locations = 1
    option_Items_And_Locations = 2
    default = 0


class StartingEpisode(Choice):
    """
    Select which episode to start with. Starting with Anatomy for disaster
    is not compatible with the "first section" and "whole episode" options for
    "Episode 8 Keys".

    Requires "Episodes As Items" to be set to "Nonprogressive Episodes" for this
    to have any effect.
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


# These are potential options planned for the future, to be able to control
# where exactly in the story the player gets to start their run, which would
# also allow for these options to be randomized.
#
# Each of these will require that we get playing Jobs in any order within Episodes
# to be up and running first, and would ideally want us to have added Days & Jobs
# as items as well.
#
# I did have a thought though, that these could just be excluded and that we would
# use the built-in "Start Inventory" Option instead. However, I would want these
# to be able to be randomized and to only have them randomize with each other,
# which would not be easy to do with the regular "Start Inventory" or "Start
# Inventory from Pool", if not simply impossible, if other non-Day or non-Job
# items were included in either of those as well.
class StartingDay(Choice):
    """
    Hidden option.
    Select which day to start with. Starting with an episode's final day
    is not compatible with any of the boss "goal" options. Also, starting with
    Day 4 is not compatible with the "Jailbreak" and "Anatomy for Disaster"
    options for "Starting Episode" if those episodes are set to only have a total
    of 3 days for  "Episodes 4 and 8 Num Days".

    Requires "Days As Items" to be set to "Nonprogressive Days" for this to have
    any effect.
    """
    visibility = Visibility.none
    display_name = "Starting Day"
    option_Day_1 = 0
    option_Day_2 = 1
    option_Day_3 = 2
    option_Day_4 = 3
    default = 0


class StartingJob(OptionSet):
    """
    Hidden option
    Select which job to start with. Starting with an episode's final job
    is not compatible with any of the boss "goal" options.

    Requires "Jobs as Items" to be set to "Nonprogressive Jobs" for this to have
    any effect. Also requires your chosen job to be available in your starting
    episode & day to have any effect. If multiple valid Job names are entered,
    then a random one from among those entered will be chosen. You can also set
    this to ['Random'] to add all possible valid Jobs to this pool.
    """
    visibility = Visibility.none
    display_name = "Starting Job"
    valid_keys = [str(job) for ep in EPISODES for job in ep] + ["Random"]
    default = ["Satellite Sabotage"]


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
# The harder difficulties could also adjust the times on each of the Pedestal Treasures
# to have less time to bring them back to the Safehouse, thus actually requiring
# movement-based Gadgets to be able to collect. There is even a whole dedicated mod for
# this on the Weed Sheet Google Doc that I remember seeing that could be used as a
# reference for this idea. That being said, I am thinking that controlling this might
# be better located and controlled by the "Include Treasures" Option below, but this
# difficulty option can still interact with that setting depending on our desired
# implementation for all of this.
#
# This can also interact with the "Include Max HP" Option also planned later, so that
# easier difficulties will start with more Max HP Items & "require" more Max HP Items
# in logic for players to beat certain parts of the game, while the harder difficulties
# will not gate any logic behind these Max HP Items at all (Except for the Ep7 Operation
# which requires using the Alarm Clock Gadget, so we'll have to determine how little GP
# you absolutely require for that Job). Though if having so little HP & GP ends up being
# TOO difficult, then we could  create an additional difficulty for this Brutal setting.
#
# This setting will 100% require the input of the Sly 2 APWorld community to help
# determine where we want to draw the lines for each of these difficulties.
class LogicDifficultyLevel(Choice):
    """
    Hidden option.
    Select which difficulty level for the logic to use.
     - Easy: Very forgiving, trying to ensure that you have various Gadgets to help in various locations.
     - Normal: The default difficulty ensures that you have the bare minimum Gadgets to complete your locations.
     - Hard: The hardest "regular" difficulty that will expect you to know of non-glitch tricks to compensate for fewer Gadgets.
     - Glitched: The most unforgiving logic, requiring the use of glitches/speedrunning tricks, like Triple-Jumping.
    """
    visibility = Visibility.none
    display_name = "Logic Difficulty Level"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    option_glitched = 3
    default = 1


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


# TODO: Determine whether this new class should be used, or if it would be ok &
#  to use the old SkipPrologue class.
#
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


# TODO: Either here in a new option or in the JobsAsLocations option below,
#  allow players to choose if "Sequential Jobs" (that normally only get unlocked
#  after completing another Job in the same Day) will still require completing
#  other Jobs in the same Day to be accessible or if their accessibility should
#  be independent of completing other Jobs.
#  Likely will make this its own Option since this might also affect how the
#  "Progressive Job" Items for each Episode might behave.
class SequentialJobsDependencies(Toggle):
    """
    Whether to handle if "Sequential Jobs" (that normally only get unlocked
    after completing another Job in the same Day) will still require completing
    other Jobs in the same Day to be accessible or if their accessibility should
    be independent of completing other Jobs.
    Jobs this affects:
    - Satellite Sabotage -> Breaking and Entering
    - Follow Dimitri -> Waterpump Destruction
    - Moonlight Rendezvous -> Disco Demolitions
    - Lower the Drawbridge -> Battle the Chopper
    - Eavesdrop on Contessa -> Train Hack (If Ep4 set to only 3 days)
    - Train Hack -> Wall Bombing
    - Spice in the Sky -> Ride the Iron Horse
    - Aerial Assault -> Theft on the Rails
    - Old Grizzle Face -> Thermal Ride
    - Mega-Jump Job -> Carmelita's Gunner (If Ep8 set to only 3 days)
    """
    visibility = Visibility.none
    display_name = "Sequential Jobs Dependencies"


# TODO: Finish making this Option
class CompoundJobsAsMultipleJobs(Choice):
    """
    Whether to handle "Compound-Jobs" as multiple Jobs or as only a single Job,
    both in terms of Jobs being Items or Locations.
    Jobs this affects:
    - Operation: Thunder Beak // Printing Press Duel
    - Operation: Hippo Drop (Bomb the Bridge, Tango with Carmelita, Clear the Way for Murray)
    - Operation: Wet Tiger // Showdown with Rajan
    - Operation: Canada Games // Brains over Brawn
    - Carmelita's Gunner // Showdown with Clock-La
    """
    display_name = "Compound-Jobs As Multiple Jobs"
    option_As_Items_Only = 0
    option_As_Locations_Only = 1
    Option_Both = 2
    Option_Off = 3
    default = 0


# TODO: Look into the possibility of combining all of these Story-Based Options
#  into a single Option (1 Option for Items & 1 Option for Locations. Look at
#  Luigi's Mansion and its Furnisanity Option for possible inspiration. Other
#  examples could include: Yacht Dice (that's all I got so far, would want to
#  ask others for what they might know about related possibilities from other APWorlds).)
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


# TODO: Add an option to pick if each day sends out only 1 check or multiple checks,
#  either here or in a separate option. If multiple checks is chosen, the number of
#  checks for each day is determined by how many jobs are in the next day. The
#  final day of each episode is still only 1 check.
class DaysAsLocations(Choice):
    """
    Whether to include completing Days as checks, and if completing days will send
    out only a single check or multiple checks.
    """
    display_name = "Days As Locations"
    option_Single_Check = 0
    option_Multiple_Checks = 1
    option_Off = 2
    default = 2


class JobsAsLocations(DefaultOnToggle):
    """
    Whether to include completing Jobs as checks.
    """
    display_name = "Jobs As Locations"


# TODO: Decide whether this Option should be hidden or not.
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


class IncludeGadgetButtons(Choice):
    """
    Add the Assignable Gadget Powerup buttons on the controller to the pool.
    """
    visibility = Visibility.none
    display_name = "Include Gadget Buttons"
    option_All_Characters = 0
    option_Per_Character = 1
    option_Off = 2
    default = 2


# TODO: Implement the choice here to make the Mega-Jump Gadget required for the
#  "Mega-Jump Job" in Episode 8
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


# TODO: Once being able to play any Job in any order is implemented, change this
#  from a Toggle to a Choice that includes an extra option for the Gold Painting
#  you get from the Bug Dimitri's Office job.
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


# TODO: Determine if it is possible to "piggy-back" off of the RetroAchievements'
#  website calls to use as locations. Otherwise, we'll have to use the memory
#  address lists that they use for determining trophy completion and reimplement
#  it ourselves.
class IncludeTrophies(Choice):
    """
    Whether to include trophies as checks. These trophies are originally based
    off of the ones made for the PS3, PS4, & PS5 versions of Sly 2, however
    there are choices for this option to include fan-made trophies from the
    RetroAchievements website.
    """
    visibility = Visibility.none
    display_name = "Include Trophies"
    option_On = 0
    option_Include_Fanmade = 1
    option_Include_Missable = 2
    option_Off = 3
    default = 3


class SkipIntro(DefaultOnToggle):
    """
    Whether the Cairo intro should be skipped.
    """
    display_name = "Skip Intro"


# TODO: Determine the desired order & Groupings for these Options. Rearrange the
#  above file & the OptionGroups below, as well as the 'generate_early' function
#  & the 'get_options_as_dict' function in the __init__.py file to more accurately
#  reflect this chosen order.
@dataclass
class Sly2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
    permissive_yaml: PermissiveYaml
    yaml_items_and_locations_handling: YamlItemsAndLocationsHandling
    logic_difficulty_level: LogicDifficultyLevel

    starting_episode: StartingEpisode
    starting_day: StartingDay
    starting_job: StartingJob
    # starting_character: StartingCharacter

    goal: Goal

    keys_in_pool: KeysInPool
    episode_8_keys: Episode8Keys
    required_keys_episode_8: RequiredKeys
    required_keys_goal: RequiredKeysGoal

    include_prologue: IncludePrologue
    episodes_4_and_8_num_days: Episodes4And8NumDays
    sequential_jobs_dependencies: SequentialJobsDependencies
    compound_jobs_as_multiple_jobs: CompoundJobsAsMultipleJobs

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

    include_gadget_buttons: IncludeGadgetButtons
    include_mega_jump: IncludeMegaJump
    include_tom: IncludeTOM
    include_time_rush: IncludeTimeRush

    coins_minimum: CoinsMinimum
    coins_maximum: CoinsMaximum

    include_treasures: IncludeTreasures
    include_vaults: IncludeVaults
    include_photography: IncludePhotography
    include_pickpocketing: IncludePickpocketing

    # lootsanity:LootSanity
    small_guard_loot_chance: SmallGuardLootChance
    large_guard_loot_chance: LargeGuardLootChance
    loot_table_distribution: LootTableDistribution
    randomize_loot: RandomizeLoot

    thiefnet_minimum: ThiefNetCostMinimum
    thiefnet_maximum: ThiefNetCostMaximum
    scout_thiefnet: ScoutThiefnet

    bottle_location_bundle_size: BottleLocationBundleSize
    bottle_item_bundle_size: BottleItemBundleSize
    bottlesanity: BottleSanity

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
        StartingEpisode,
        StartingDay,
        StartingJob,
        #StartingCharacter,
        IncludePrologue,
        Episodes4And8NumDays,
        SequentialJobsDependencies,
        CompoundJobsAsMultipleJobs,
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
        IncludeGadgetButtons,
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
        ScoutThiefnet # TODO: Determine if this is needed in this OptionGroup or not.
    ]),
    OptionGroup("Pick-pocketing",[
        RandomizeLoot,
        SmallGuardLootChance,
        LargeGuardLootChance,
        LootTableDistribution
    ])
]
