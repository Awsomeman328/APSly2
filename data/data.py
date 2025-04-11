EPISODES = {
    "The Black Chateau": [
        [
            "Satellite Sabotage",
            "Breaking and Entering",
        ],
        [
            "Bug Dimitri's Office",
            "Follow Dimitri",
            "Waterpump Destruction",
        ],
        [
            "Silence the Alarms",
            "Theater Pickpocketing",
            "Moonlight Rendezvous",
            "Disco Demolitions",
        ],
        [
            "Operation: Thunder Beak"
        ],

    ],
    "A Starry Eyed Encounter": [
        [
            "Recon the Ballroom",
        ],
        [
            "Lower the Drawbridge",
            "Steal a Tuxedo",
            "Dominate the Dance Floor",
            "Battle the Chopper",
        ],
        [
            "Boardroom Brawl",
            "RC Bombing Run",
            "Elephant Rampage",
        ],
        [
            "Operation: Hippo Drop",
        ],
    ],
    "The Predator Awakens": [
        [
            "Spice Room Recon",
        ],
        [
            "Water Bug Run",
            "Freeing the Elephants",
            "Leading Rajan",
        ],
        [
            "Neyla's Secret",
            "Spice Grinder Destruction",
            "Blow the Dam",
            "Rip-Off the Ruby"
        ],
        [
            "Operation: Wet Tiger"
        ],
    ],
    "Jailbreak": [
        [
            "Eavesdrop on Contessa",
            "Train Hack",
            "Wall Bombing",
        ],
        [
            "Big House Brawl",
            "Lightning Action",
            "Disguise Bridge",
            "Code Capture",
            "Close to Contessa",
        ],
        [
            "Operation: Trojan Tank",
        ],
    ],
    "A Tangled Web": [
        [
            "Know Your Enemy",
        ],
        [
            "Ghost Capture",
            "Mojo Trap Action",
            "Kidnap the General",
        ],
        [
            "Stealing Voices",
            "Tank Showdown",
            "Crypt Hack",
        ],
        [
            "Operation: High Road",
        ],
    ],
    "He Who Tames the Iron Horse": [
        [
            "Cabin Crimes",
        ],
        [
            "Spice in the Sky",
            "A Friend in Need",
            "Ride the Iron Horse",
        ],
        [
            "Aerial Assault",
            "Bear Cub Kidnapping",
            "Theft on the Rails",
        ],
        [
            "Operation: Choo-Choo",
        ],
    ],
    "Menace from the North, Eh!": [
        [
            "Recon the Sawmill",
        ],
        [
            "Bearcave Bugging",
            "RC Combat Club",
            "Laser Redirection",
        ],
        [
            "Lighthouse Break-In",
            "Old Grizzle Face",
            "Boat Hack",
            "Thermal Ride",
        ],
        [
            "Operation: Canada Games",
        ],
    ],
    "Anatomy for Disaster": [
        [
            "Blimp HQ Recon",
        ],
        [
            "Charged TNT Run",
            "Murray/Sly Tag Team",
            "Sly/Bentley Conspire",
            "Bentley/Murray Team Up",
        ],
        [
            "Mega-Jump Job",
        ],
        [
            "Carmelita's Gunner",
        ],
    ],
}

TREASURES = {
    "The Black Chateau": [
        ("Crystal Chalice", 2),
        ("Ivory Jewel Box", 2),
        ("Jade Vase", 2),
    ],
    "A Starry Eyed Encounter": [
        ("Ancestral Kite", 1),
        ("Burial Urn", 1),
        ("Ming Vase", 1),
    ],
    "The Predator Awakens": [
        ("Gilded Scepter", 1),
        ("Crystal Flask", 1),
        ("Golden Scroll Case", 1),
    ],
    "Jailbreak": [
        ("Ceremonial Lantern", 1),
        ("Crystal Ball", 1),
        ("Golden Orb", 1),
    ],
    "A Tangled Web": [
        ("Crystal Vase", 1),
        ("Jeweled Crown", 1),
        ("Royal Tiara", 1),
    ],
    "He Who Tames the Iron Horse": [
        ("Crystal Bell", 1),
        ("Alabaster Chalice", 1),
        ("Golden Plate", 1),
    ],
    "Menace from the North, Eh!": [
        ("Collectible Plate", 1),
        ("Jade Decanter", 1),
        ("Jeweled Chalice", 1),
    ],
    "Anatomy for Disaster": [
        ("Golden Vase", 1),
        ("Jeweled Egg", 1),
        ("Golden Headdress", 1),
    ],
}

ADDRESSES = {
    "SCUS-97316": {
        "loading": 0x3D3980,
        "world id": 0x3D4A60,
        "job id": 0x2DEB44,
        "reload": 0x3E1080,
        "reload values": 0x3E1088,
        "camera focus": 0x2DE258,
        "coins": 0x3D4B00,
        "gadgets": 0x3D4AF8,
        "active character": 0x3D4A6C,
        "active character pointer": 0x2DE2F0,
        "string table": 0x3e1ad4,
        "infobox": 0x3DA0E8,
        "infobox scrolling": 0x3DA0D0,
        "infobox string": 0x3DA0D8,
        "infobox duration": 0x3DA0DC,
        "infobox text": [
            0x4c5710,
            0x4bd990,
            0x4c11a0,
            0x4c2f50,
            0x4c6e40,
            0x4befd0,
            0x4cb900,
            0x4c10f0
        ],
        "health": [0x3d4ab0,0x3d4ac0,0x3d4ae0],
        "bottle flags": {
            "e4": 0x3D5020
        },
        "bottle count": 0x3E1BF4,
        "thiefnet costs": [0x2BCDE8+i*0x20 for i in range(24)],
        "jobs": {
            "e1": [[],],
            "e4": [[0xb2ec90,0xb34d30,],],
        },
        "text": {
            "Press START (new)": 0x4c5b40,
            "Press START (resume)": 0x4c5bf0,
            "this powerup.": 0x4cdcb8,
            "powerups": {
                "Trigger Bomb": (0x4a4600,0x4cb9b0),
                "Size Destabilizer": (0x4cba20,0x4cba90),
                "Snooze Bomb": (0x4cbb10,0x4cbc10),
                "Adrenaline Burst": (),
                "Health Extractor": (),
                "Hover Pack": (),
                "Reduction Bomb": (),
                "Temporal Lock": (),

                "Fists of Flame": (),
                "Turnbuckle Launch": (),
                "Juggernaut Throw": (),
                "Atlas Strength": (),
                "Diablo Fire Slam": (),
                "Berserker Charge": (),
                "Guttural Roar": (),
                "Raging Inferno Flop": (),

                "Smoke Bomb": (),
                "Combat Dodge": (),
                "Stealth Slide": (),
                "Alarm Clock": (),
                "Paraglide": (),
                "Silent Obliteration": (),
                "Thief Reflexes": (),
                "Feral Pounce": (),
            }
        }
    },
}

POWERUP_TEXT = {
    "Trigger Bomb": "Throwable bomb with remote detonation.",
    "Size Destabilizer": "Shrink Guards by whacking them with your crossbow.",
    "Snooze Bomb": "Put enemies in the area to sleep.",
    "Adrenaline Burst": "",
    "Health Extractor": "",
    "Hover Pack": "",
    "Reduction Bomb": "",
    "Temporal Lock": "",

    "Fists of Flame": "",
    "Turnbuckle Launch": "",
    "Juggernaut Throw": "",
    "Atlas Strength": "",
    "Diablo Fire Slam": "",
    "Berserker Charge": "",
    "Guttural Roar": "",
    "Raging Inferno Flop": "",

    "Smoke Bomb": "",
    "Combat Dodge": "",
    "Stealth Slide": "",
    "Alarm Clock": "",
    "Paraglide": "",
    "Silent Obliteration": "",
    "Thief Reflexes": "",
    "Feral Pounce": "",
}

MENU_RETURN_DATA = (
    "8F1B8DAE"+
    "A19F156B"+
    "C9553493"+
    "EA141CB0"+
    "9DFADC0B"+
    "D9679121"+
    "2CAAB3DF"+
    "F9A50AD0"+
    "82D34135"+
    "ECBF73F2"+
    "38D17CBA"+
    "C1067796"+
    "BD977E22"+
    "AF5088AE"+
    "F0553493"+
    "9E5F086B"+
    "89010000"+
    "FFFFFFFF"+
    "8F1B8DAE"+
    "A19F156B"+
    "C9553493"+
    "EA141CB0"+
    "9DFADC0B"+
    "D9679121"+
    "2CAAB3DF"+
    "F9A50AD0"+
    "82D34135"+
    "ECBF73F2"+
    "38D17CBA"+
    "C1067796"+
    "BD977E22"+
    "AF5088AE"+
    "F0553493"+
    "9E5F086B"
)