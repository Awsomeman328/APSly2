from typing import NamedTuple

from BaseClasses import Item, ItemClassification

from .Constants import EPISODES, EPISODES_DAYS_JOBS_TASKS
from .Locations import is_compound_job

class Sly2Item(Item):
    game: str = "Sly 2: Band of Thieves"

class Sly2ItemData(NamedTuple):
    name: str
    code: int
    category: str
    classification: ItemClassification

# The way I chose to do this is super nice-looking, but it also won't play nice
# with multiworlds generated with a version with a different order of items.

filler_list = [
    ("Coins",   ItemClassification.filler,  "Filler"), # TODO: Change "Filler" to "Coin" once the Health filler item is implemented
    #("Health", ItemClassification.filler,  "Health")
]

# TODO: Once the "Difficulty" yaml Option is made and implemented, examine
#  which of these Gadgets/Power-Ups are required for the easiest difficulty
#  and change their classifications to 'progression'.
powerup_list = [
    ("Smoke Bomb",              ItemClassification.useful,      "Power-Up"),
    ("Combat Dodge",            ItemClassification.useful,      "Power-Up"),
    ("Stealth Slide",           ItemClassification.useful,      "Power-Up"),
    ("Alarm Clock",             ItemClassification.progression, "Power-Up"),
    ("Paraglider",              ItemClassification.progression, "Power-Up"),
    ("Silent Obliteration",     ItemClassification.useful,      "Power-Up"),
    ("Thief Reflexes",          ItemClassification.useful,      "Power-Up"),
    ("Feral Pounce",            ItemClassification.progression, "Power-Up"),

    ("Knockout Dive",           ItemClassification.useful,      "Power-Up"),
    ("Insanity Strike",         ItemClassification.useful,      "Power-Up"),
    ("Voltage Attack",          ItemClassification.useful,      "Power-Up"),
    ("Long Toss",               ItemClassification.useful,      "Power-Up"),
    ("Rage Bomb",               ItemClassification.useful,      "Power-Up"),
    ("Music Box",               ItemClassification.useful,      "Power-Up"),
    ("Lightning Spin",          ItemClassification.useful,      "Power-Up"),
    ("Shadow Power",            ItemClassification.useful,      "Power-Up"),

    ("Mega Jump",               ItemClassification.progression, "Power-Up"),
    ("TOM",                     ItemClassification.useful,      "Power-Up"),
    ("Time Rush",               ItemClassification.useful,      "Power-Up"),

    ("Trigger Bomb",            ItemClassification.useful,      "Power-Up"),
    ("Size Destabilizer",       ItemClassification.useful,      "Power-Up"),
    ("Snooze Bomb",             ItemClassification.useful,      "Power-Up"),
    ("Adrenaline Burst",        ItemClassification.useful,      "Power-Up"),
    ("Health Extractor",        ItemClassification.useful,      "Power-Up"),
    ("Hover Pack",              ItemClassification.progression, "Power-Up"),
    ("Reduction Bomb",          ItemClassification.useful,      "Power-Up"),
    ("Temporal Lock",           ItemClassification.useful,      "Power-Up"),

    ("Fists of Flame",          ItemClassification.useful,      "Power-Up"),
    ("Turnbuckle Launch",       ItemClassification.progression, "Power-Up"),
    ("Juggernaut Throw",        ItemClassification.useful,      "Power-Up"),
    ("Atlas Strength",          ItemClassification.useful,      "Power-Up"),
    ("Raging Inferno Flop",     ItemClassification.useful,      "Power-Up"),
    ("Berserker Charge",        ItemClassification.useful,      "Power-Up"),
    ("Guttural Roar",           ItemClassification.useful,      "Power-Up"),
    ("Diablo Fire Slam",        ItemClassification.useful,      "Power-Up"),
]

clockwerk_parts_list = [
    (f"Clockwerk {s}",           ItemClassification.progression, "Clockwerk Part")
    for s in [
        "Tail Feathers",
        "Wing (Right)",
        "Wing (Left)",
        "Heart (Right Half)",
        "Heart (Left Half)",
        "Eye (Right)",
        "Eye (Left)",
        "Lung (Right)",
        "Lung (Left)",
        "Stomach",
        "Talons",
        "Hate Chip",
        "Brain",

        "Beak",
        "Ribcage",
        "Skull",
        "Leg (Right)",
        "Leg (Left)",
        "Neck",
        "Pelvis",

        "Feather"
    ]
]

bottle_list = [
    (f"Bottle - {e}",           ItemClassification.progression, "Bottles")
    for e in EPISODES.keys()
] + [
    (f"{i} bottles - {e}",      ItemClassification.progression, "Bottles")
    for e in EPISODES.keys() for i in range(2,31)
]

progressive_episode_list = [
    (f"Progressive Episode",        ItemClassification.progression, "Progressive Episode")
    for e in EPISODES.keys()
]

nonprogressive_episode_list = [
    (f"{e}",        ItemClassification.progression, "Nonprogressive Episode")
    for e in EPISODES.keys()
]

progressive_day_list = [
    (f"Progressive Day - {e}",        ItemClassification.progression, "Progressive Day")
    for e in EPISODES.keys()
]

nonprogressive_day_list = [
    (f"{e} - Day {d}",        ItemClassification.progression, "Nonprogressive Day")
    for e in EPISODES.keys() for d in range(1,5)
]

progressive_job_list = [
    (f"Progressive Job List - {e}",        ItemClassification.progression, "Progressive Job by Episode")
    for e in EPISODES.keys()
] + [
    (f"Progressive Job List - {e}, Day {d}",        ItemClassification.progression, "Progressive Job by Day")
    for e in EPISODES.keys() for d in range(1,5)
]

nonprogressive_job_list = []
for e, days in EPISODES_DAYS_JOBS_TASKS.items():
    for day in days:
        for job_name, job_contents in day:
            if is_compound_job(job_contents):
                for subjob_name, subjob in job_contents:
                    nonprogressive_job_list.append((f"{e} - {job_name}", ItemClassification.progression, "Nonprogressive Job"))
            nonprogressive_job_list.append((f"{e} - {job_name}", ItemClassification.progression, "Nonprogressive Job"))

# TODO: Delete all of this when the comments are no longer necessary.
# The following lists are planned items to add in the future, adding characters as Items
# (akin to what Sly 3 is planning), each of their Max Healths & Max Gadget Power as Items,
# and each of the playable Vehicles as Items.
#
# For Max HP & Max Gadget Power, the range of having up to 5 of each of these items per
# character (plus the option for the item to apply to all characters) is based on the default
# Max Health for all playable entities, not just the base characters of Sly, Bentley, & Murray.
# Originally I wanted to use the base characters' entities' Max Healths as the base-line for
# how to divide up each of these items, with the potential to have up to 20 of these Max Health
# increase items, either per character or for the whole gang, but then I found out that a
# single outlying turret entity only has a Max Health of 5, so that shot that idea down.
#
# When implementing this, will need to remember to change both the memory addresses for both
# the actual amount of Health left and for updating the GUI for it to display the correct
# current Health. But other than that, it will simply check if (either the currently controlled
# entity or all playable entities, not sure which yet) are above current allowed Max Health
# amount, and if they are over then their Health will be adjusted to be their currently allowed
# Max Health.
#
# While researching this, I also came up with the idea of making each of the playable Vehicles
# into Items that players will have to unlock in order to access them. This will include:
# - The Turret (Episodes 2, 3, 5, & 8)
# - The RC Chopper (Episodes 2, 4, & 6)
# - The Tank (Episode 5)
# - The RC Car (Episode 7)
character_list = [
    ("Playable Sly", ItemClassification.progression, "Character"),
    ("Playable Bentley", ItemClassification.progression, "Character"),
    ("Playable Murray", ItemClassification.progression, "Character"),
]

vehicle_list = [
    ("Playable Turret", ItemClassification.progression, "Vehicle"),
    ("Playable RC Chopper", ItemClassification.progression, "Vehicle"),
    ("Playable Tank", ItemClassification.progression, "Vehicle"),
    ("Playable RC Car", ItemClassification.progression, "Vehicle")
]

health_list = [
    (f"Progressive Max Health - {c[0][8:]}", ItemClassification.useful, "HP")
    for c in character_list for i in range(1,6)
] + [
    (f"Progressive Max Gadget Power - {c[0][8:]}", ItemClassification.useful, "GP")
    for c in character_list for i in range(1,6)
] + [
    (f"Progressive Max Health", ItemClassification.useful, "HP")
    for i in range(1,6)
] + [
    (f"Progressive Max Gadget Power", ItemClassification.useful, "GP")
    for i in range(1,6)
]

item_list = (
    filler_list+
    powerup_list+
    clockwerk_parts_list+
    bottle_list+
    progressive_episode_list+
    nonprogressive_episode_list+
    progressive_day_list+
    nonprogressive_day_list+
    progressive_job_list+
    nonprogressive_job_list+
    character_list+
    vehicle_list+
    health_list
)

base_code = 123_000

item_dict = {
    name: Sly2ItemData(name, base_code+code, category, classification)
    for code, (name, classification, category) in enumerate(item_list)
}

item_groups = {
    key: {item.name for item in item_dict.values() if item.category == key}
    for key in [
        "Filler",
        "Power-Up",
        "Bottles",
        "Clockwerk Part",
        "Progressive Episode",
        "Nonprogressive Episode",
        "Progressive Day",
        "Nonprogressive Day",
        "Progressive Job by Episode",
        "Progressive Job by Day",
        "Nonprogressive Job",
        "Character",
        "Vehicle",
        "HP",
        "GP"
    ]
}

def from_id(item_id: int) -> Sly2ItemData:
    matching = [item for item in item_dict.values() if item.code == item_id]
    if len(matching) == 0:
        raise ValueError(f"No item data for item id '{item_id}'")
    assert len(matching) < 2, f"Multiple item data with id '{item_id}'. Please report."
    return matching[0]
