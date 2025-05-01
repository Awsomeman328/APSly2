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


class StartingEpisode(Choice):
    """
    Select Which episode to start with. Starting with Anatomy for disaster
    is not compatible with "Episode 8 Keys".
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


class Goal(Choice):
    """
    Which boss you must defeat to goal.
    """

    display_name = "Goal"
    option_Dimitri = 0
    option_Rajan = 1
    option_The_Contessa = 2
    option_Jean_Bison = 3
    option_ClockLa = 4
    # option_All_Bosses = 6
    default = 4


class Episode8Keys(DefaultOnToggle):
    """
    Whether to have Anatomy for Disaster be unlocked with a number of Clockwerk
    parts, rather than with a single item like the other episodes.
    """

    display_name = "Episode 8 Keys"


class RequiredKeys(Range):
    """
    How many Clockwerk parts you need to unlock Anatomy for Disaster, if
    Episode 8 Keys is turned on.
    """

    display_name = "Episode 8 Required Keys"
    range_start = 1
    range_end = 100
    default = 10


class KeysInPool(Range):
    """
    How many Clockwerk parts are added to the pool. This number cannot be
    lower than the required number of keys. No Clockwerk parts will be added
    if Episode 8 Keys is off.
    """

    display_name = "Clockwerk Parts in Pool"
    range_start = 1
    range_end = 100
    default = 10


class IncludeTOM(Toggle):
    """
    Add the TOM ability to the pool.
    """

    display_name = "Include TOM"


class IncludeMegaJump(Toggle):
    """
    Add the Mega Jump ability to the pool.
    """

    display_name = "Include Mega Jump"


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
    range_end = 10_000
    default = 200


class ThiefNetCostMaximum(Range):
    """
    The maximum number of coins items on ThiefNet will cost.
    """

    display_name = "ThiefNet Cost Maximum"
    range_start = 0
    range_end = 10_000
    default = 2000


class BottleLocationBundleSize(Range):
    """
    How many bottles you need to collect for each check. Set to 0 to disable
    bottles as checks.
    """

    display_name = "Bottle Location Bundle Sizes"
    range_start = 0
    range_end = 10
    default = 0


class BottleItemBundleSize(Range):
    """
    How many bottles you receive from an item. Set to 0 to disable bottles
    as items.
    """

    display_name = "Bottle Item Bundle Sizes"
    range_start = 0
    range_end = 10
    default = 0


class SkipIntro(DefaultOnToggle):
    """
    Whether the Cairo intro should be skipped.
    """

    display_name = "Skip Intro"


@dataclass
class Sly2Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
    starting_episode: StartingEpisode
    goal: Goal
    episode_8_keys: Episode8Keys
    required_keys: RequiredKeys
    keys_in_pool: KeysInPool
    include_tom: IncludeTOM
    include_mega_jump: IncludeMegaJump
    coins_minimum: CoinsMinimum
    coins_maximum: CoinsMaximum
    thiefnet_minimum: ThiefNetCostMinimum
    thiefnet_maximum: ThiefNetCostMaximum
    bottle_location_bundle_size: BottleLocationBundleSize
    bottle_item_bundle_size: BottleItemBundleSize
    # skip_intro: SkipIntro

sly2_option_groups = [
    OptionGroup("Goal",[
        Goal
    ]),
    OptionGroup("Clockwerk parts",[
        Episode8Keys,
        RequiredKeys,
        KeysInPool
    ]),
    OptionGroup("Items",[
        IncludeTOM,
        IncludeMegaJump,
        CoinsMinimum,
        CoinsMaximum,
        BottleItemBundleSize
    ]),
    OptionGroup("Locations",[
        ThiefNetCostMinimum,
        ThiefNetCostMaximum,
        BottleLocationBundleSize
    ])
]
