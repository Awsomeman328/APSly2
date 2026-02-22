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
            "Operation: Thunder Beak",
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
            "Operation: Canada Games"
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
            "Carmelita's Gunner/Defeat Clock-la"
        ],
    ],
}

# Depending on how the implementation goes, the following 2 data structures might
# replace the above section entirely.
TASK_FIELD = {
    "TASK_NUM": 0,
    "TASK_NAME": 1,
    "IS_CHECKPOINT": 2,
    "IS_PHOTOGRAPHY": 3,
    "IS_STEALING": 4,
    "OBJECTIVE": 5
}
# TODO: Remember that the first and last task in most episodes are bugged & fix 'em.
# Besides the Prologue & Ep3's intro, every other episode's DAG isn't loaded
# during the completion of their first and last tasks. Each of these tasks are
# located in each Episode's Day 1's Overworld sections as the first and last
# entries. Should likely look into how other parts of this code handles this
# problem, specifically for Defeating Clock-La.
#
# I also just realized after writing all of this that I could have tried to extract
# the original task names from within the game's memory, but I still feel as
# though about half of those names need to be altered for various reasons.
# (Either too generic, inaccurate, technical, or multiple of these)
#
# The main thing missing from each of these are which characters & vehicles are
# required for each Job, b/c I only came up with those items AFTER already writing
# out all 1k+ lines of this. But I can likely add them in myself.
#
# It is also possible that this data structure could be flattened out to get rid of
# a lot of its nested-ness, with each Task's Episode, Day, & Job info being stored
# within each Task individually, but that would store a lot of redundant data.
# But whichever approach we feel is necessary we can go with.

# TODO: Add in the Character & Vehicle Unlock Item Requirements to each Job.
# TODO: Restructure Eps 4 & 8 to be a full 4 days rather than only 3.
# TODO: Add in more "Overworld" Jobs for each day, not just Day 1,
#  and reorganize all of the appropriate tasks to those Days' new "Overworld" sections.
# TODO: Additionally to the item directly above this, have it so that all "Chalk-Talk" Tasks
#  require being able to beat all other Jobs in the same Day, which with the above change
#  will likely have all of said "Chalk-Talk" Tasks be the last Task listed in every "Overworld"
#  section, but we'll see if that holds true or not.
# (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
EPISODES_DAYS_JOBS_TASKS = {
    "A Shadow from the Past": (
        ( # Day 1
            ("Overworld", (
                (1, "Game Intro Run-up",      False,False,False,""),
                (2, "Game Intro Post-Run-Up", False,False,False,""),
                (3, "Game Start Screen",      False,False,False,""),
                (16,"Prologue Complete",      False,False,False,""),
            ), "Any", "None"), #Character requirements & Vehicle requirements
            ("Museum Break-in", (
                (4, "Job Start",True,False,False,"Power up the elevator"),

                (5, "Wire Work",False,False,False,"Rendezvous with Murray"),

                (6, "Murray Helps",           False,False,False,""),
                (7, "Enter Clockwerk Room",   False,False,False,"Locate Clockwerk Parts"),

                (8, "Hallway Chase Start",    True ,False,False,""),
                (9, "Hallway Chase Complete", False,False,False,""),
                (10,"Rooftop Chase Start",    True ,False,False,""),
                (11,"Cop Car Chase 1",        False,False,False,""),
                (12,"Cop Car Chase 2",        False,False,False,""),
                (13,"Cop Car Chase 3",        False,False,False,""),
                (14,"Van Rescue Attempt",     False,False,False,""),
                (15,"Van Escape",             False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "The Black Chateau": (
        ( # Day 1
            ("Overworld", (
                (1, "Episode Intro",              False,False,False,""),  # Not Working Properly
                (2, "Safehouse Roof Intro",       False,False,False,""),
                (3, "Waypoint Marker Reminder",   False,False,False,""),
                (4, "Abandon Job Reminder",       False,False,False,""),
                (29,"Chalk-talk #1",              False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Satellite Sabotage", (
                (5,"Job Start",True,False,False,"Locate The Job Start Point"),

                (6,"Satellite Dish #1",   False,False,False,""),
                (7,"Satellite Dish #2",   False,False,False,""),
                (8,"Satellite Dish #3",   False,False,False,""),
                (9,"Job Complete",        False,False,False,"Reposition All 3 Dishes"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Breaking and Entering", (
                (10,"Job Start",      False,False,False,""),
                (11,"Inside Intro",   True ,False,False,""),
                (12,"Rat Brawl #1",   False,False,False,"Battle Guards with Murray"),

                (13,"Lower Bars",                 False,False,False,""),
                (14,"Checkpoint #1",              True ,False,False,""),
                (15,"Crawl-table Tutorial",       False,False,False,""),
                (16,"Flashlight Guard Tutorial",  False,False,False,""),
                (17,"Crawl-vent Tutorial #1",     False,False,False,""),
                (18,"Checkpoint #2",              True ,False,False,""),
                (19,"Takedown Tutorial #1",       False,False,False,""),
                (20,"Takedown Tutorial #2",       False,False,False,""),
                (21,"Rat Brawl #2",               False,False,False,""),
                (22,"Crawl-vent Tutorial #2",     False,False,False,""),
                (23,"Break Vent",                 False,False,False,""),
                (24,"Photography Tutorial",       False,False,False,"Locate Tail Feathers"),

                (25,"Photograph Generator",   False,True ,False,""),
                (26,"Photograph Dimitri",     False,True ,False,""),
                (27,"Photograph Tailfeathers",False,True ,False,""),
                (28,"Job Complete",           False,False,False,"Take Reconnaissance Photos"),
            ), "Sly & Murray", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 2
            ("Overworld", (
                (30,"Binocucom Reminder",         False,False,False,""),
                (31,"Booty Reminder",             False,False,False,""),
                (43,"Swapped Painting Reminder",  False,False,False,""),
                (48,"Chalk-talk #2",              False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Bug Dimitri's Office",(
                (37, "Job Start",       True, False,False,""),
                (38, "Interior Intro",  True, False,False,"Enter Nightclub via Balcony"),

                (39, "Break Vent",      False,False,False,""),
                (40, "Drop into Office",False,False,False,"Sneak into Dimitri’s Office"),

                (41, "Bug Swap",    False,False,False,""),
                (42, "Job Complete",False,False,False,"Place Bug/Swap Paintings"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Follow Dimitri",(
                (44,"Job Start",                        True ,False,False,""),
                (45,"Ring the Bell",                    True ,False,False,""),
                (46,"Follow Dimitri on the Streets",    False,False,False,""),
                (47,"Job Complete",                     False,False,False,"Steal Dimitri’s Access Code"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Waterpump Destruction",(
                (76,"Job Start",                True ,False,False,""),
                (77,"Murray Tutorial",          False,False,False,""),
                (78,"Destroy Power Box #1",     False,False,False,""),
                (79,"Destroy Power Box #2",     False,False,False,""),
                (80,"Pickup Guard Tutorial",    False,False,False,"Locate the water pump"),

                (81,"Break Waterpump Tank", False,False,False,""),
                (82,"Photography Tutorial", False,False,False,"Destroy the water pump"),
            ), "Murray", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 3
            ("Overworld", (
                (60,"Pickpocket Reminder",        False,False,False,""),
                (83,"Chalk-talk #3",              False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Silence the Alarms",(
                (32,"Job Start",        True ,False,False,""),
                (33,"Destroy Alarm #1", False,False,False,""),
                (34,"Destroy Alarm #2", False,False,False,""),
                (35,"Destroy Alarm #3", False,False,False,""),
                (36,"Job Complete",     False,False,False,"Locate and Destroy Alarms"),
            ), "Murray", "None"), #Character requirements & Vehicle requirements
            ("Theater Pickpocketing",(
                (49,"Job Start",            True ,False,False,""),
                (50,"Pickpocket Tutorial",  False,False,False,""),
                (51,"Pickpocket Key#1",     True ,False,True ,""),
                (52,"Pickpocket Key#2",     True ,False,True ,""),
                (53,"Pickpocket Key#3",     True ,False,True ,""),
                (54,"Pickpocket Key#4",     True ,False,True ,""),
                (55,"Pickpocket Key#5",     True ,False,True ,""),
                (56,"Pickpocket Key#6",     True ,False,True ,""),
                (57,"Pickpocket All Keys",  False,False,False,"Pickpocket all the guards"),

                (58,"Shut Off Fans",False,False,False,"Use Keys to Shut Down Fans"),

                (59,"Job Complete",False,False,False,"Climb Fans and Kill the Power"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Moonlight Rendezvous",(
                (61,"Job Start",    True ,False,False,""),
                (62,"Chase Neyla",  False,False,False,""),
                (63,"Job Complete", False,False,False,"Chase Neyla"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Disco Demolitions",(
                (64,"Job Start",                True ,False,False,""),
                (65,"Bomb Tutorial",            False,False,False,""),
                (66,"Destroy Laser Fence #1",   False,False,False,""),
                (67,"Sleep Darts Tutorial",     False,False,False,""),
                (68,"Destroy Laser Fence #2",   False,False,False,""),
                (69,"Disco Dialogue",           False,False,False,""),
                (70,"Destroy Laser Fence #3",   False,False,False,""),
                (71,"Bomb Disco Support #1",    False,False,False,""),
                (72,"Bomb Disco Support #2",    False,False,False,""),
                (73,"Bomb Disco Support #3",    False,False,False,""),
                (74,"Bomb Disco Support #4",    False,False,False,""),
                (75,"Job Complete",             False,False,False,"Bomb all 4 support columns"),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 4
            ("Overworld", (
                (99,"Episode Complete",           False,False,False,""),  # Not Working Properly
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("Operation: Thunder Beak",(  # "Compound-Job" #1
                ("Operation: Thunder Beak",(
                    (84,"Heist Start",              True ,False,False,""),
                    (85,"Fight Guards",             False,False,False,""),
                    (86,"Bomb Water-tower Door",    False,False,False,"Get into the water tower"),

                    (87,"Turn the Valves",          False,False,False,""),
                    (88,"Fountain Guard Emerges",   False,False,False,"Shut off water to the fountain"),

                    (89,"Pickpocket Guard",True ,False,True ,"Pickpocket the guard"),

                    (90,"Fountain Rendezvous",False,False,False,"Meet at the fountain"),

                    (91,"Hijack the Truck",False,False,False,"Hijack the repair truck"),

                    (92,"Climb the Peacock",True ,False,False,"Climb the peacock sign"),

                    (93,"Shoot Harpoon",True ,False,False,"Grapple to top of sign"),

                    (94,"Truck Siege",False,False,False,"Defend the truck"),
                ), "All", "None"), #Character requirements & Vehicle requirements
                ("Printing Press Duel",(
                    (95,"Boss Arena Break-In",  True ,False,False,""),
                    (96,"Boss Fight Start",     True ,False,False,""),
                    (97,"Boss Fight",           False,False,False,""),
                    (98,"Boss Fight Complete",  False,False,True ,"Get the Clockwerk Tail Feathers"),
                ), "Sly", "None"), #Character requirements & Vehicle requirements
            ), "All", "None"), #Character requirements & Vehicle requirements
        ),

    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "A Starry Eyed Encounter": (
        ( # Day 1
            ("Overworld", (
# Task # 2 Seems to be bugged and either won’t complete itself or has no trigger to mark it as complete.
# The trigger seems to be near the rocks on the left side coming out of the safehouse.
# Either that, or it just needs to be triggered twice? Still needs more investigation.
                (1, "Episode Intro",        False,False,False,""),  # Not Working Properly
                (2, "Spire Jump Tutorial",  False,False,False,""),  # Not Working Properly
                (16,"Chalk-talk #1",        False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Recon the Ballroom",(
                (3, "Job Start",            True ,False,False,""),
                (4, "Sneak Into Ballroom",  True ,False,False,"Sneak through balcony door"),

                (5, "Photograph Winch",             False,True ,False,""),
                (6, "Photograph Wing Left",         False,True ,False,""),
                (7, "Photograph Wing Right",        False,True ,False,""),
                (8, "Photograph Rajan",             False,True ,False,""),
                (9, "Tier 1 Photographs Complete",  False,False,False,""),
                (10,"Photograph Jean Bison",        False,True ,False,""),
                (11,"Photograph Contessa",          False,True ,False,""),
                (12,"Photograph Neyla",             False,True ,False,""),
                (13,"Photograph Carmelita",         False,True ,False,""),
                (14,"Photograph Arpeggio",          False,True ,False,""),
                (15,"Job Complete",                 False,False,False,"Take needed recon photos"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 2
            ("Overworld", (
                (51,"Chalk-talk #2",        False,False,False,""),
            ), "Sly & Murray", "Turret"), #Character requirements & Vehicle requirements
            ("Lower the Drawbridge",(
                (17,"Job Start",                    True ,False,False,""),
                (18,"Lounge Key Guard Hint",        False,False,False,""),
                (19,"Pickpocket Grass Key",         True ,False,True ,""),
                (20,"Pickpocket Lounge Key",        True ,False,True ,""),
                (21,"Pickpocket Guesthouse Key",    True ,False,True ,""),
                (22,"Pickpocket Cobra Key",         True ,False,True ,""),
                (23,"Pickpocket Bridge Key",        True ,False,True ,""),
                (24,"Pickpocket All Keys",          False,False,False,"Pickpocket guards"),

                (25,"Job Complete",True ,False,True ,"Unlock drawbridge winch"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Battle the Chopper",(
                (26,"Job Start",            True ,False,False,""),
                (27,"Lift Turret Lever",    False,False,False,""),
                (28,"Attack the Chopper",   True ,False,False,""),
                (29,"Job Complete",         False,False,False,"Destroy the chopper"),
            ), "Murray", "Turret"), #Character requirements & Vehicle requirements
            # I originally considered structuring this Job w/ "Dominate the Dance Floor"
            # as a "Compound-Job" like how most of the Heists are actually multiple
            # Jobs stringed directly together, but since these two jobs each have their
            # own Job-Starts & I want to be able to easily control said Job-Starts to
            # allow players to both replay jobs if they missed something &/or play Jobs
            # out of order to skip right to the Operations/Heists/Boss Fights (if they
            # have them unlocked), I'm going to keep these two as separate for now to
            # make the activation of each Job easier to access and simpler to code.
            ("Ballroom Dance Party",(
                (37,"Job Start",True ,False,False,"Knock on the Ballroom Door"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Steal a Tuxedo",(
                (38,"Job Start",                                    True ,False,False,""),
                (39,"Rajan PA",                                     False,False,False,""),
                (40,"Sneak Attack Reminder",                        False,False,False,""),
                (41,"Steal Jean Bison’s Tuxedo Jacket (Room 105)",  True ,False,True ,""),
                (42,"Steal Arpeggio’s Bowtie (Room 101)",           True ,False,True ,""),
                (43,"Steal Rajan’s Dance Shoes (Room 103)",         True ,False,True ,""),
                (44,"Steal Carmelita’s Gloves (Room 102)",          True ,False,True ,""),
                (45,"Steal Contesssa’s Shirt (Room 104)",           True ,False,True ,""),
                (46,"Job Complete",                                 False,False,False,"Find needed tuxedo pieces"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Dominate the Dance Floor",(
                (47,"Job Start",        False,False,False,""),
                (48,"Talk to Neyla",    False,False,False,""),
                (49,"Dance Audition",   True ,False,False,""),
                (50,"Job Complete",     False,False,False,"Complete the dance"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 3
            ("Overworld", (
                (65,"Chalk-talk #3",        False,False,False,""),
            ), "All", "RC Chopper"), #Character requirements & Vehicle requirements
            ("Boardroom Brawl",(
                (30,"Job Start",        True ,False,False,""),
                (31,"Look for the Code",False,False,False,""),
                (32,"Found the Code",   True ,False,False,"Locate code under a table"),

                (33,"Turn Off Laser Door",False,False,False,"Enter code/turn off lasers"),

                (34,"Pull Lever",True ,False,False,"Pull switch to open door"),

                (35,"Brawl Battle", True ,False,False,""),
                (36,"Job Complete", False,False,False,"Protect Bentley while he hacks the computers"),
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("RC Bombing Run",(
                (52,"Job Start",        True ,False,False,""),
                (53,"Destroy the jeep", False,False,False,""),
                (54,"Job Complete",     False,False,False,"Destroy jeep"),
            ), "Bentley", "RC Chopper"), #Character requirements & Vehicle requirements
            ("Elephant Rampage",(
                (55, "Job Start",       True ,False,False,""),
                (56, "Scare Elephants", False,False,False,"Break elephants out of pen"),

                (57, "Begin Part 2",    True ,False,False,""),
                (58, "Collect Gem 1A",  False,False,True ,""),
                (59, "Collect Gem 1B",  False,False,True ,""),
                (60, "Collect Gem 1C",  False,False,True ,""),
                (61, "Collect Gem 2A",  False,False,True ,""),
                (62, "Collect Gem 2B",  False,False,True ,""),
                (63, "Collect Gem 2C",  False,False,True ,""),
                (64, "Job Complete",    False,False,False,"Get gems off the elephants"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 4
            ("Overworld", (
                (93,"Episode Complete",     False,False,False,""),  # Not Working Properly
            ), "All", "RC Chopper"), #Character requirements & Vehicle requirements
            ("Operation: Hippo Drop",(  # "Compound-Job" #2
                ("Bomb the Bridge",(
                    (66, "Heist Start",             True ,False,False,""),
                    (67, "Go to the Bridge",        False,False,False,""),
                    (68, "Bomb Lower Cleat #1",     False,False,False,""),
                    (69, "Bomb Lower Cleat #2",     False,False,False,""),
                    (70, "Bomb Lower Cleat #3",     False,False,False,""),
                    (71, "Bomb Lower Cleat #4",     False,False,False,""),
                    (72, "Bomb Lower Cleat #5",     False,False,False,""),
                    (73, "Bomb Lower Cleat #6",     False,False,False,""),
                    (74, "Bomb Lower Cleat #7",     False,False,False,""),
                    (75, "Bomb Lower Cleat #8",     False,False,False,""),
                    (76, "Bomb Lower Cleat #9",     False,False,False,""),
                    (77, "Bomb All Lower Cleats",   False,False,False,""),
                    (78, "Go to the Upper Cleats",  True ,False,False,""),
                    (79, "Bomb Upper Cleat #1",     False,False,False,""),
                    (80, "Bomb Upper Cleat #2",     False,False,False,""),
                    (81, "Bomb Upper Cleat #3",     False,False,False,""),
                    (82, "Bomb Upper Cleat #4",     False,False,False,""),
                    (83, "Bomb Upper Cleat #5",     False,False,False,""),
                    (84, "Bomb Upper Cleat #6",     False,False,False,""),
                    (85, "Bomb Upper Cleat #7",     False,False,False,""),
                    (86, "Bomb Upper Cleat #8",     False,False,False,""),
                    (87, "Job Complete",            False,False,False,"Bomb and destroy the bridge"),
                ), "Bentley", "None"), #Character requirements & Vehicle requirements
                ("Tango with Carmelita",(
                    (88, "Job Start",           False,False,False,""),
                    (89, "Dance With Carmelita",True ,False,False,""),
                    (90, "Job Complete",        False,False,False,"Complete the dance"),
                ), "Sly & Murray", "None"), #Character requirements & Vehicle requirements
                ("Clear the Way for Murray",(
                    (91, "Job Start/Cover Murray",  True ,False,True ,""),
                    (92, "Job Complete",            False,False,False,"Protect Murray from guards"),
                ), "Bentley & Murray", "RC Chopper"), #Character requirements & Vehicle requirements
             ), "All", "RC Chopper"), #Character requirements & Vehicle requirements
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "The Predator Awakens": (
# Task #1 for this Episode is Part of the cut content for the game, and is now used
# as part of the achievements for the PS4/PS5 releases for this game, as well as
# likely being a part of RetroAchievements. But it is still a part of the DAG’s Task
# List for this game, so I'm including it in this when it is available on Day ?.
        ( # Day 1
            ("Overworld", (
                (2, "Episode Intro",                    False,False,False,""),
                (14,"Chalk-talk #1",                    False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Spice Room Recon",(
                (3, "Job Start",    True ,False,False,""),
                (4, "Enter Pipe",   False,False,False,"Find entrance into temple"),

                (5, "Interior Intro",       True ,False,False,""),
                (6, "Rail Slide Tutorial",  False,False,False,""),
                (7, "Spy Point Entrance",   False,False,False,"Get to the access tube"),

                (8, "Photograph Clockwerk Heart",   False,True ,False,""),
                (9, "Photograph Crane Controls",    False,True ,False,""),
                (10,"Photograph Entrance",          False,True ,False,""),
                (11,"Photograph Rajan",             False,True ,False,""),
                (12,"Temple Recon Complete",        False,False,False,"Take Recon Photos"),

                (13,"Job Complete",False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 2
            ("Overworld", (
                (56,"Chalk-talk #2",                    False,False,False,""),
            ), "Sly & Bentley", "None"), #Character requirements & Vehicle requirements
            ("Water Bug Run",(
                (15,"Job Start",    True ,False,False,""),
                (16,"Plant Bug",    False,False,False,""),
                (17,"Job Complete", False,False,False,"Get the bug in Rajan’s office"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Freeing the Elephants",(
                (18,"Job Start",                True ,False,False,""),
                (19,"Collect Spice #1",         True ,False,True ,""),
                (20,"Collect Spice #2",         True ,False,True ,""),
                (21,"Collect Spice #3",         True ,False,True ,""),
                (22,"Collect Spice #4",         True ,False,True ,""),
                (23,"Collect Spice #5",         True ,False,True ,""),
                (24,"Collect Spice #6",         True ,False,True ,""),
                (25,"Collecting Spice Complete",False,False,False,"Collect all necessary spice"),

                (26,"Deposit Spice",False,False,False,""),
                (27,"Job Complete", False,False,False,"Drop the spice in the basket"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Leading Rajan",(
                (36,"Job Start",            True ,False,False,""),
                (37,"Sleep Rajan #1",       False,False,False,""),
                (38,"Retrieve Blueprint #1",False,False,True ,""),
                (39,"Item #1 Complete",     True ,False,False,""),
                (40,"Sleep Rajan #2",       False,False,False,""),
                (41,"Retrieve Blueprint #2",False,False,True ,""),
                (42,"Item #2 Complete",     True ,False,False,""),
                (43,"Sleep Rajan #3",       False,False,False,""),
                (44,"Retrieve Blueprint #3",False,False,True ,""),
                (45,"Item #3 Complete",     True ,False,False,""),
                (46,"Job Complete",         False,False,False,"Get Rajan’s three blueprints"),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 3
            ("Overworld", (
                (1, "Destroy the Spice Grinder Door",   False,False,False,""), # TODO: Check if only Sly can make it to the Spice Grinder Room or if anyone else can.
                (66,"Chalk-talk #3",                    False,False,False,""),
            ), "All", "Turret"), #Character requirements & Vehicle requirements
            ("Neyla's Secret",(
                (28,"Job Start",    True ,False,False,""),
                (29,"Chase Neyla",  False,False,False,""),
                (30,"Open the Door",False,False,False,"Keep up with Neyla"),

                (31,"Interior Start",           True ,False,False,""),
                (32,"Pickpocket Key #1",        True ,False,True ,""),
                (33,"Pickpocket Key #2",        True ,False,True ,""),
                (34,"Drop the Clockwerk Heart", False,False,False,""),
                (35,"Job Complete",             False,False,True ,"Get half of the Clockwerk heart"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Spice Grinder Destruction",(
                (47,"Job Start",                True ,False,False,""),
                (48,"Destroy Laser Fence #1",   False,False,False,""),
                (49,"Destroy Laser Fence #2",   False,False,False,""),
                (50,"Destroy Laser Fence #3",   False,False,False,""),
                (51,"Destroy Laser Fence #4",   False,False,False,""),
                (52,"Interior Intro",           False,False,False,""),
                (53,"Find the Spice Grinder",   False,False,False,""),
                (54,"TNTBarrel Reminder",       False,False,False,""),
                (55,"Job Complete",             False,False,False,"Destroy the Spice Grinder"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Blow the Dam",(
                (57,"Job Start",    True ,False,False,""),
                (58,"Job Complete", False,False,False,"Take out Rajan’s dam"),
            ), "Bentley", "Turret"), #Character requirements & Vehicle requirements
            ("Rip-Off the Ruby",(
# In this job, the task with the objective "Get Murray to the ruby" appears to either
# be assigned to the wrong task in the game's memory, or one could say that the text
# is just incorrect. Either way, if there is a way for us to change this and have it
# affect the "Job Help" page in-game, then I would love to do that. But, that is such
# a minor, basically visual only error, that I'm not too bothered to leave it be when
# have like 10 other bugs and issues to work on for this APWorld.
                (59,"Job Start",            True ,False,False,""),
                (60,"Break the Ruby Loose", True ,False,False,"Get Murray to the ruby"),
                (61,"Carrying Ruby Tutorial",True ,False,False,""),

                (62,"Carry the Ruby Part #1",False,False,False,"Get ruby to the first buyer"),

                (63,"Talk to the First Buyer",  True ,False,False,""),
                (64,"Carry the Ruby Part #2",   False,False,False,""),
                (65,"Job Complete",             False,False,False,"Get ruby to the final buyer"),
            ), "All", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 4
            ("Overworld", (
                (82,"Episode Complete",                 False,False,False,""),
            ), "All", "Turret"), #Character requirements & Vehicle requirements
            ("Operation: Wet Tiger",(  # "Compound-Job" #3
                ("Operation: Wet Tiger",(
                    (67,"Heist Start",          False,False,False,""),
                    (68,"Talk to Bentley",      True ,False,False,""),
                    (69,"Take out the Guards",  False,False,False,"Get Murray to the lever"),

                    (70,"Start Lifting the Lever",False,False,False,"Begin lifting the lever"),

                    (71,"Switch to Bentley",            True ,False,False,""),
                    (72,"Protect Murray",               False,False,False,""),
                    (73,"Switch to Murray",             True ,False,False,""),
                    (74,"Lifting the Lever Complete",   False,False,False,"Finish lifting the lever"),

                    (75,"Switch to Sly",                True ,False,False,""),
                    (76,"Destroy the Elephant’s Mouth", False,False,False,"Get TNT Barrel into mouth"),
                ), "All", "Turret"), #Character requirements & Vehicle requirements
                ("Showdown with Rajan",(
                    (77,"Boss Fight Start",             True ,False,False,""),
                    (78,"Boss Fight Lightning Phase",   False,False,False,"Get to Rajan"),

                    (79,"Sly’s Capture",        True ,False,False,""),
                    (80,"Boss Fight Pool Phase",False,False,True ,""),
                    (81,"Boss Fight Complete",  False,False,False,"Defeat Rajan"),
                ), "Sly & Murray", "None"), #Character requirements & Vehicle requirements
            )),
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "Jailbreak": (
        ( # Day 1 (Or 1 & 2)
# Both Days 1 & 2 could be combined into a single Day (which is actually how the
# original implementation had it setup), but with me now making it a .yaml option to
# select between this & Ep8 be either 3 Days or 4 Days, it is easier to have each of
# them already set up for 4 Days and then combine the two days later if desired.
            ("Overworld", (
                (1,  "Episode Intro",   False,False,False,""),
            ), "None", "None"), #Character requirements & Vehicle requirements
            ("Eavesdrop on Contessa",(
                (2,  "Job Start",   True ,False,False,""),
                (3,  "Eavesdrop #1",False,False,False,""),
                (4,  "Eavesdrop #2",False,False,False,""),
                (5,  "Eavesdrop #3",False,False,False,""),
                (6,  "Eavesdrop #4",False,False,False,""),
                (7,  "Job Outro",   False,False,False,"Shoot Contessa with darts"),
                (8,  "Job Complete",False,False,False,""),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 2 (Or 1 & 2)
            ("Overworld", (
                (33, "Chalk-talk #1",   False,False,False,""),
            ), "Bentley & Sly", "None"), #Character requirements & Vehicle requirements
            ("Train Hack",(
                (9,  "Job Start",           True ,False,False,""),
                (10, "Hack Station #1",     False,False,False,""),
                (11, "Get to Station #2",   True ,False,False,""),
                (12, "Hack Station #2",     False,False,False,""),
                (13, "Get to Station #3",   True ,False,False,""),
                (14, "Hack Station #3",     False,False,False,""),
                (15, "Get to Station #4",   True ,False,False,""),
                (16, "Hack Station #4",     False,False,False,""),
                (17, "Get to Station #5",   True ,False,False,""),
                (18, "Hack Station #5",     False,False,False,""),
                (19, "Get to Station #6",   True ,False,False,""),
                (20, "Hack Station #6",     False,False,False,""),
                (21, "Job Complete",        False,False,False,"Hack all six stations"),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
            ("Wall Bombing",(
                (22, "Job Start",       True ,False,False,""),
                (23, "Bomb Guard #1",   False,False,False,""),
                (24, "Bomb Guard #2",   False,False,False,""),
                (25, "Bomb Guard #3",   False,False,False,""),
                (26, "Bomb Guard #4",   False,False,False,""),
                (27, "Bomb Guard #5",   False,False,False,""),
                (28, "Bomb Guard #6",   False,False,False,""),
                (29, "Bomb Guard #7",   False,False,False,""),
                (30, "Bomb All Guards", False,False,False,"Take out wall guards"),

                (31, "Sly Escape",  True ,False,False,""),
                (32, "Job Complete",False,False,False,"Escape to the safehouse"),
            ), "Bentley & Sly", "RC Chopper"), #Character requirements & Vehicle requirements
        ),
        ( # Day 3 (Or 2)
            ("Overworld", (
                (77, "Chalk-talk #2",   False,False,False,""),
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("Big House Brawl",(
                (34, "Job Start",   True ,False,False,""),
                (35, "Brawl Intro", True ,False,False,"Find pipe into Murray’s cell"),

                (36, "Brawl Beatdown",  False,False,False,""),
                (37, "Job Complete",    True ,False,False,"Take out 50 prisoners"),
            ), "Sly & Murray", "None"), #Character requirements & Vehicle requirements
            ("Lightning Action",(
                (38, "Job Start",                       True ,False,False,""),
                (39, "Lightning Puzzle #1 Animation",   False,False,False,""),
                (40, "Lightning Puzzle #1 Complete",    True ,False,False,""),
                (41, "Lightning Puzzle #2 Animation",   False,False,False,""),
                (42, "Lightning Puzzle #2 Complete",    True ,False,False,""),
                (43, "Lightning Puzzle #3 Animation",   False,False,False,""),
                (44, "Lightning Puzzle #3 Complete",    True ,False,False,""),
                (45, "Lightning Puzzle #4 Animation",   False,False,False,""),
                (46, "Lightning Puzzle #4 Complete",    True ,False,False,""),
                (47, "Lightning Puzzle #5 Animation",   False,False,False,""),
                (48, "Lightning Puzzle #5 Complete",    True ,False,False,""),
                (49, "Job Complete",                    False,False,False,"Disable all lightning rods"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Disguise Bridge",(
                (50, "Job Start",           True ,False,False,""),
                (51, "Bomb Under Bridge",   False,False,False,""),
                (52, "Bentley Relocate",    False,False,False,""),
                (53, "Bomb On Top",         True ,False,False,""),
                (54, "Job Complete",        True ,False,False,"Protect Bentley from guards"),
            ), "Sly & Bentley", "None"), #Character requirements & Vehicle requirements
            ("Code Capture",(
                (55, "Job Start",                   True ,False,False,""),
                (56, "Pickpocket Key #1",           False,False,True ,""),
                (57, "Photograph Code #1",          False,True ,False,""),
                (58, "Complete Capturing Code #1",  True ,False,False,""),
                (59, "Pickpocket Key #2",           False,False,True ,""),
                (60, "Photograph Code #2",          False,True ,False,""),
                (61, "Complete Capturing Code #2",  True ,False,False,""),
                (62, "Pickpocket Key #3",           False,False,True ,""),
                (63, "Photograph Code #3",          False,True ,False,""),
                (64, "Complete Capturing Code #3",  True ,False,False,""),
                (65, "Pickpocket Key #4",           False,False,True ,""),
                (66, "Photograph Code #4",          False,True ,False,""),
                (67, "Complete Capturing Code #4",  True ,False,False,""),
                (68, "Job Complete",                False,False,False,"Photograph the four codes"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Close to Contessa",(
                (69, "Job Start",               True ,False,False,""),
                (70, "Pickpocket Tank Key #1",  False,False,True ,""),
                (71, "Contessa Relocate #1",    False,False,False,""),
                (72, "Pickpocket Tank Key #2",  True ,False,True ,""),
                (73, "Contessa Relocate #2",    False,False,False,""),
                (74, "Pickpocket Tank Schedule",True ,False,True ,""),
                (75, "Contessa Relocate #2",    False,False,False,""),
                (76, "Job Complete",            False,False,False,"Pickpocket Contessa 3 times"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 4 (Or 4)
            ("Overworld", (
                (110,"Episode Complete",False,False,False,""),
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("Operation: Trojan Tank", (
                (78, "Heist Start",     False,False,False,""),
                (79, "Heist Intro",     True ,False,False,""),
                (80, "Get the Tank",    False,False,False,"Hijack the tank"),

                (81, "Shoot Doors Open",True ,False,False,"Crawl under the tank"),

                (82, "Get in the Building", True ,False,False,""),
                (83, "Use the Elevator",    True,False,False,"Get to the ground floor"),

                (84, "Disable Gate",False,False,False,"Disable gate from tower"),

                (85, "Get to the Gate",True ,False,False,"Rendezvous with Bentley"),

                (86, "Find Murray",             True ,False,False,""),
                (87, "Get to Keypad #1",        False,False,False,""),
                (88, "Hack Keypad #1",          False,False,False,""),
                (89, "Use Keypad #1",           False,False,False,""),
                (90, "Get to Keypad #2",        False,False,False,""),
                (91, "Hack Keypad #2",          False,False,False,""),
                (92, "Use Keypad #2",           False,False,False,""),
                (93, "Get to Keypad #3",        False,False,False,""),
                (94, "Hack Keypad #3",          False,False,False,""),
                (95, "Use Keypad #3",           False,False,False,""),
                (96, "Break/Freak Murray Out",  False,False,False,"Turn on three hypno boxes"),

                (97, "Hypno Box Plan",              True ,False,False,""),
                (98, "Break Hypno Box #1",          False,False,False,""),
                (99, "Break Hypno Box #2",          False,False,False,""),
                (100,"Break Hypno Box #3",          False,False,False,""),
                (101,"Break Hypno Box #4",          False,False,False,""),
                (102,"Break all the Hypno Boxes",   True ,False,False,"Destroy all the hypno boxes"),

                (103,"Chase Plan",      True ,False,False,""),
                (104,"Murray Lift #1",  False,False,False,""),
                (105,"Murray Lift #2",  False,False,False,""),
                (106,"Lift Both Levers",False,False,False,"Lift the levers to get out"),

                (107,"Contessa Chase Start",    True ,False,False,""),
                (108,"Contessa Chase Complete", False,False,False,""),
                (109,"Heist Complete",          True ,False,False,"Chase the Contessa"),
            ), "All", "None"), #Character requirements & Vehicle requirements
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "A Tangled Web": (
        ( # Day 1
            ("Overworld", (
                (1,  "Episode Intro",       False,False,False,""),
                (16, "Chalk-talk #1",       False,False,False,""),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Know Your Enemy",(
                (2,  "Job Start",               True ,False,False,""),
                (3,  "Photograph Neyla’s HQ",   True ,True ,False,""),
                (4,  "Photograph Assault Tank", True ,True ,False,""),
                (5,  "Photograph Blimp",        True ,True ,False,""),
                (6,  "Photograph Boat",         True ,True ,False,""),
                (7,  "Enter the Tower",         True ,False,False,"Take Photos, get into tower"),

                (8,  "Tower Recon Start",           True ,False,False,""),
                (9,  "Photograph Shadow Guard",     False,True ,False,""),
                (10, "Photograph Carmelita",        False,True ,False,""),
                (11, "Photograph Clockwerk Eyes",   False,True ,False,""),
                (12, "Photograph Mind Shuffler",    False,True ,False,""),
                (13, "Photograph Old Terminal",     False,True ,False,""),
                (14, "Tower Recon Complete",        False,False,False,""),
                (15, "Job Complete",                False,False,False,"Take photos in tower"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 2
            ("Overworld", (
                (46, "Chalk-talk #2",       False,False,False,""),
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("Ghost Capture",(
                (17, "Job Start",  True ,False,False,""),
                (18, "Enter Tomb", True ,False,False,"Enter the tomb"),

                (19, "Free all the ghosts",False,False,False,"Break coffin and free ghosts"),

                (20, "Start Taking Pictures",   True ,False,False,""),
                (21, "Photograph Ghost #1",     True ,True ,False,""),
                (22, "Photograph Ghost #2",     True ,True ,False,""),
                (23, "Photograph Ghost #3",     True ,True ,False,""),
                (24, "Photograph Ghost #4",     True ,True ,False,""),
                (25, "Photograph Ghost #5",     True ,True ,False,""),
                (26, "Photograph Ghost #6",     True ,True ,False,""),
                (27, "Photograph Ghost #7",     True ,True ,False,""),
                (28, "Photograph Ghost #8",     True ,True ,False,""),
                (29, "Photograph Ghost #9",     True ,True ,False,""),
                (30, "Photography Complete",    False,False,False,"Photograph the ghosts"),

                (31, "Ghost Drop",              False,False,False,""),
                (32, "Job Complete",            False,False,False,"Deliver ghosts to Neyla’s HQ"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Mojo Trap Action",(
                (33, "Job Start",                      True ,False,False,""),
                (34, "Trap Tutorial",                  False,False,False,""),
                (35, "Open Hall Crypt Door",           True ,False,False,""),
                (36, "Collect Hall Crypt’s Bad Mojo",  True ,False,False,""),
                (37, "Open Tomb Crypt Door",           True ,False,False,""),
                (38, "Collect Tomb Crypt’s Bad Mojo",  True ,False,False,""),
                (39, "Open Water Crypt Door",          True ,False,False,""),
                (40, "Collect Water Crypt’s Bad Mojo", True ,False,False,""),
                (41, "Job Complete",                   False,False,False,"Collect 4 batches of bad mojo"),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
            ("Kidnap the General",(
                (42, "Job Start",           True ,False,False,""),
                (43, "Initial Grab",        False,False,False,""),
                (44, "Carry to Safehouse",  False,False,False,""),
                (45, "Job Complete",        False,False,False,"Bring General to safehouse"),
            ), "Murray", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 3
            ("Overworld", (
                (79, "Chalk-talk #3",       False,False,False,""),
            ), "All", "None"), #Character requirements & Vehicle requirements
            ("Stealing Voices",(
                (47, "Job Start",                   True ,False,False,""),
                (48, "Pickpocket Wire Tap Key #1",  True ,False,True ,""),
                (49, "Pickpocket Wire Tap Key #2",  True ,False,True ,""),
                (50, "Open Wire Tap Door",          False,False,False,""),
                (51, "Steal Wire Tap",              True ,False,True ,"Steal keys then wire tap"),

                (52, "Go Back Outside #1",                  True ,False,False,""),
                (53, "Pickpocket Voice Modulator Key #1",   True ,False,True ,""),
                (54, "Pickpocket Voice Modulator Key #2",   True ,False,True ,""),
                (55, "Open Voice Modulator Door",           False,False,False,""),
                (56, "Steal Voice Modulator",               True ,False,True ,"Keys then voice modulator"),

                (57, "Go Back Outside #2",      True ,False,False,""),
                (58, "Pickpocket Sewer Key #1", True ,False,True ,""),
                (59, "Pickpocket Sewer Key #2", True ,False,True ,""),
                (60, "Open Sewer Door",         False,False,False,""),
                (61, "Tap into the Cable",      True ,False,False,""),
                (62, "Job Complete",            False,False,False,"Keys then tap into cable"),
            ), "Sly", "None"), #Character requirements & Vehicle requirements
            ("Tank Showdown",(
                (63, "Job Start",   True ,False,False,""),
                (64, "Kill Tank #1",False,False,False,""),
                (65, "Kill Tank #2",False,False,False,""),
                (66, "Kill Tank #3",False,False,False,""),
                (67, "Kill Tank #4",False,False,False,""),
                (68, "Kill Tank #5",False,False,False,""),
                (69, "Kill Tank #6",False,False,False,""),
                (70, "Job Complete",False,False,False,"Destroy 6 of Neyla’s tanks"),
            ), "Murray", "Tank"), #Character requirements & Vehicle requirements
            ("Crypt Hack",(
                (71, "Job Start",           True ,False,False,""),
                (72, "Find the Battery",    False,False,False,"Destroy 6 of Neyla’s tanks"),

                (73, "Hack Station #1",     False,False,False,""),
                (74, "Get to Station #2",   True ,False,False,""),
                (75, "Hack Station #2",     False,False,False,""),
                (76, "Get to Station #3",   True ,False,False,""),
                (77, "Hack Station #3",     False,False,False,""),
                (78, "Job Complete",        False,False,False,"Hack all three computers"),
            ), "Bentley", "None"), #Character requirements & Vehicle requirements
        ),
        ( # Day 4
            ("Overworld", (
                (80, "Paraglider Reminder", False,False,False,""),
                (102,"Episode Complete",    False,False,False,""),
            ), "All", "Turret & Tank"), #Character requirements & Vehicle requirements
            ("Operation: High Road",(
                (81, "Heist Start",             True ,False,False,""),
                (82, "Paraglide to the Blimp",  True ,False,False,"Paraglide to blimp"),

                (83, "Get to The Old Terminal", True ,False,False,""),
                (84, "Hack the Terminal",       True ,False,False,""),
                (85, "Free Carmelita",          True ,False,False,""),
                (86, "Exit the Tower",          True ,False,False,"Hack the computer"),

                (87, "Neyla Chase Start",       True ,False,False,""),
                (88, "Keep Up With Neyla",      False,False,False,""),
                (89, "Get Clockwerk Eye #1",    True ,False,True ,"Chase Neyla"),

                (90, "Get to the Blimp’s Turret",   True ,False,False,""),
                (91, "Destroy the Planes",          False,False,False,""),
                (92, "Turret Section Complete",     False,False,False,"Defend the Blimp"),

                (93, "Boss Fight Start",            True ,False,False,""),
                (94, "Boss Fight Phase 1",          False,False,False,""),
                (95, "Boss Fight Phase 1 Complete", True ,False,False,"Battle the Contessa"),

                (96, "Tank Chase Start",        True ,False,False,""),
                (97, "Chase/Follow Carmelita",  False,False,False,""),
                (98, "Tank Chase Complete",     False,False,False,"Disable Carmelita’s Tank"),

                (99, "Boss Fight Phase 2 Start",    True ,False,False,""),
                (100,"Boss Fight Phase 2 Complete", False,False,False,""),
                (101,"Heist Complete",              True ,False,True ,"Retrieve the Clockwerk Eye"),
            ), "All", "Turret & Tank"), #Character requirements & Vehicle requirements
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "He Who Tames the Iron Horse": (
        ( # Day 1
# *Sigh* ... So task #18, the "Jean Bison PA" Task, made me realise some important things.
#
# 1) This specific task only triggers if the Job "Spice in the Sky" is Finished & you pick
# Bentley, which if we are planning on letting players play their jobs in any order, this
# will be a problem since Spice in the Sky will always be set to available and not finished,
# so this task will never trigger.
#
# 2) I finally figured out that the status of each of the Chalk-Talks is what controls
# which characters are playable; primarily the first Chalk-Talks that would unlock the
# respective character. There is likely another specific place that is actually responsible
# for controlling which of the characters are unlocked, and it is just that these Chalk-Talk
# Tasks are just interacting with that section for that functionality, but idk where that
# in the game this section that I'm talking about is (though is it highly possible that
# others have already found where this is considering there are cheats & patches to make
# Murray playable in Ep4).
# ...
# It is through these main 2 discoveries that lead me to make the following decisions on
# this massive update I'm making, each related to the above 2 points:
#
# 1) Either I'm making it such that all Overworld Tasks can no longer be checks OR I'm
# just getting rid of all tasks as checks entirely. Probably will go with the first option,
# since to make Photographs, Stealing Key-Items, & Objectives into checks I will still need
# to use tasks to track if they've been done or not. Plus, if I remember correctly, over 90%
# of the specific tasks that I listed as possibly being problematic are all Overworld Tasks,
# like each of the Episode's Intros & Completions and also the opening sequence in Cairo, so
# just getting rid of the Overworld Tasks themselves will help me solve these issues by simply
# ignoring them! Out of the 800 or 900 Tasks, this would only remove about 40-45, so not a
# huge loss. Plus, to bleed into the 2nd point for a little bit, doing this will allow us to
# more freely use the Chalk-Talk Tasks to unlock all 3 of the Characters for Players so that
# they don't always have to play Sly's 1st Job anymore.
#
# 2) Playable Characters as Items is being dropped as a focus for now. Currently, the only way
# that I know of to control Character unlocks is through the Chalk-Talk Tasks, which is kind
# of janky. There is likely a better way to go about it, but figuring that out would require
# more research, even if other people have already figured it out before me which is highly
# likely. With only 2 characters to unlock, since you need to start with 1 of them (and it
# can almost NEVER be Murray), this just isn't worth it to develop any further for now. Maybe
# sometime in the future we'll work on it more, but for now I'm shelving the idea to be able
# to more easily focus on the rest of this update. Also, I'd want to see how the Sly 3 APWorld
# handles this, both in the sense of the game's memory & the logic in AP.
#
# That all being said, even though we are no longer going to make the Characters into Items
# for now & thus don't really need to record which characters are required for each Job, I'll
# still record these requirements for each of the rest of the Jobs here since I'm already over
# half way done with it, and this data could still be useful to use in the future if we ever
# do implement this feature.
#
# TODO: Remove ALL Overworld Tasks from being possible checks (we don't want to delete them
#  here, since their data is still useful to use for other non-checks related stuff).
# TODO: Comment out EVERYTHING that has to do with making Playable Characters into Item
#  Unlocks (we can still use their names in the items file, but don't let them be included
#  as actual possible items to be found).
            ("Overworld", (
                (1, "Episode Intro",    False,False,False,""),
                (17,"Chalk-talk #1",    False,False,False,""),
                (18,"Jean Bison PA",    False,False,False,""),
                (44,"Chalk-talk #2",    False,False,False,""),
                (60,"Chalk-talk #3",    False,False,False,""),
                (72,"Episode Complete", False,False,False,""),
            )),
# For this Job, apparently the tasks list in the code has each of the Route Map
# Photos in reverse order. It'd be interesting to try to rename these two tasks
# to have them be in regular sequential order, but there'd be no actual benefit
# from doing so other than satisfying OCD b/c of this cursed knowledge.
#
# However, the final task in this job also features a slight mistake in calling a
# satellite dish a satellite. Maybe we can try to fix this by replacing the mistake
# with the proper text? Again, probably not worth it, but at least this mistake is
# one that players could actually see.
            ("Cabin Crimes",(
                (2, "Job Start",                True ,False,False,""),
                (3, "Enter Jean Bison’s Cabin", True ,False,False,"Break into Bison’s cabin"),

                (4, "Photograph Iron Horse 3 Route Map",False,True ,False,""),
                (5, "Photograph Iron Horse 2 Route Map",False,True ,False,""),
                (6, "Photograph Iron Horse 1 Route Map",False,True ,False,""),
                (7, "Photography Complete",             False,False,False,"Photograph Train Routes"),

                (8, "Get Blueprint #1",     True ,False,True ,""),
                (9, "Leave Cabin #1",       True ,False,False,""),
                (10,"Get Blueprint #2",     True ,False,True ,""),
                (11,"Leave Cabin #2",       True ,False,False,""),
                (12,"Get Blueprint #3",     True ,False,True ,""),
                (13,"Leave Cabin #3",       True ,False,False,""),
                (14,"Get All Blueprints",   True ,False,False,"Collect all three blueprints"),

                (15,"Go to the Satellite Dish", False,False,False,""),
                (16,"Job Complete",             False,False,False,"Climb up to the satellite"),
            )),
        ),
        ( # Day 2
            ("Overworld", (
                (1, "Episode Intro",    False,False,False,""),
                (17,"Chalk-talk #1",    False,False,False,""),
                (18,"Jean Bison PA",    False,False,False,""),
                (44,"Chalk-talk #2",    False,False,False,""),
                (60,"Chalk-talk #3",    False,False,False,""),
                (72,"Episode Complete", False,False,False,""),
            )),
            ("Spice in the Sky",(
                (19,"Job Start",        True ,False,False,""),
                (20,"Open Red Train",   False,False,False,""),
                (21,"Open Blue Train",  False,False,False,""),
                (22,"Open Yellow Train",False,False,False,""),
                (23,"Open 1 Train",     True ,False,False,""),
                (24,"Open 2 Trains",    True ,False,False,""),
                (25,"Open 3 Trains",    True ,False,False,""),
                (26,"Job Complete",     False,False,False,"Blow the locks on the trains"),
            )),
            ("Ride the Iron Horse",(
                (27,"Job Start",        True ,False,False,""),
                (28,"Catch the Train",  True ,False,False,""),
                (29,"Job Complete",     False,False,True ,"Steal the Clockwerk Lung"),
            )),
            ("A Friend in Need",(
                (30,"Job Start",        True ,False,False,""),
                (31,"Follow Carmelita", False,False,False,""),
                (32,"Find Murray",      True ,False,False,"Follow Carmelita"),

                (33,"Set Carmelita’s Key #1",       True ,False,False,""),
                (34,"Pickpocket Carmelita’s Key #1",False,False,True ,""),
                (35,"Carmelita Chase #1",           False,False,False,""),
                (36,"Set Carmelita’s Key #2",       True ,False,False,""),
                (37,"Pickpocket Carmelita’s Key #2",False,False,True ,""),
                (38,"Carmelita Chase #2",           False,False,False,""),
                (39,"Set Carmelita’s Key #3",       True ,False,False,""),
                (40,"Pickpocket Carmelita’s Key #3",False,False,True ,"Pickpocket Carmelita’s Keys"),

                (41,"Carmelita Chase #3",   False,False,False,""),
                (42,"Free Murray",          False,False,False,""),
                (43,"Job Complete",         False,False,False,"Free Murray"),
            )),
        ),
        ( # Day 3
            ("Overworld", (
                (1, "Episode Intro",    False,False,False,""),
                (17,"Chalk-talk #1",    False,False,False,""),
                (18,"Jean Bison PA",    False,False,False,""),
                (44,"Chalk-talk #2",    False,False,False,""),
                (60,"Chalk-talk #3",    False,False,False,""),
                (72,"Episode Complete", False,False,False,""),
            )),
            ("Aerial Assault",(
                (45,"Job Start",        True ,False,False,""),
                (46,"Catch the Train",  True ,False,False,""),
                (47,"Chopper Battle",   False,False,False,""),
                (48,"Job Complete",     False,False,False,"Destroy aerial defenses"),
            )),
            ("Theft on the Rails",(
                (49,"Job Start",        True ,False,False,""),
                (50,"Catch the Train",  True ,False,False,""),
                (51,"Job Complete",     False,False,True ,"Steal the Clockwerk Lung"),
            )),
            ("Bear Cub Kidnapping",(
                (52,"Job Start",                    True ,False,False,""),
                (53,"Grab Bear Cub #1",             False,False,False,""),
                (54,"Throw Bear Cub #1 into Cage",  False,False,False,""),
                (55,"Checkpoint",                   True ,False,False,""),
                (56,"Enter Cave",                   False,False,False,""),
                (57,"Grab Bear Cub #2",             False,False,False,""),
                (58,"Throw Bear Cub #1 into Cage",  False,False,False,""),
                (59,"Job Complete",                 False,False,False,"Throw cubs over the fence"),
            )),
        ),
        ( # Day 4
            ("Overworld", (
                (1, "Episode Intro",    False,False,False,""),
                (17,"Chalk-talk #1",    False,False,False,""),
                (18,"Jean Bison PA",    False,False,False,""),
                (44,"Chalk-talk #2",    False,False,False,""),
                (60,"Chalk-talk #3",    False,False,False,""),
                (72,"Episode Complete", False,False,False,""),
            )),
            ("Operation: Choo-Choo",(
                (61,"Heist Start",                      True ,False,False,""),
                (62,"Catch the Train",                  True ,False,False,""),
                (63,"Reach Halfway Through the Train",  False,False,False,"Work your way through the train"),

                (64,"Chopper Battle #1 Start",      True ,False,False,""),
                (65,"Chopper Battle #1",            False,False,False,""),
                (66,"Chopper Battle #1 Complete",   False,False,False,"Protect Sly from Neyla"),

                (67,"Checkpoint ",                  True ,False,False,""),
                (68,"Reach the Clockwerk Stomach",  False,False,False,"Find the Clockwerk Stomach"),

                (69,"Chopper Battle #2 Start",  True ,False,False,""),
                (70,"Chopper Battle #2",        False,False,False,""),
                (71,"Heist Complete",           False,False,True ,"Defeat Neyla"),
            )),
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "Menace from the North, Eh!": (
        ( # Day 1
            ("Overworld", (
                (1,  "Episode Intro",           False,False,False,""),
                (2,  "Ice Wall Tutorial",       False,False,False,""),
                (17, "Chalk-talk #1",           False,False,False,""),
                (55, "Chalk-talk #2",           False,False,False,""),
                (89, "Chalk-talk #3",           False,False,False,""),
                (90, "Alarm Clock Reminder",    False,False,False,""),
                (122,"Episode Complete",        False,False,False,""),
            )),
            ("Recon the Sawmill",(
                (3,  "Job Start",                       True ,False,False,""),
                (4,  "Photograph Jean Bison's House",   True ,True ,False,""),
                (5,  "Photograph Boat",                 True ,True ,False,""),
                (6,  "Photograph Bear",                 True ,True ,False,""),
                (7,  "Photograph Sawmill Blades",       True ,True ,False,""),
                (8,  "Tier 1 Photographs Complete",     True ,False,False,"Take exterior recon photos"),

                (9,  "Begin Recon Inside Lighthouse",   True ,False,False,""),
                (10, "Photograph Battery Charger",      False,True ,False,""),
                (11, "Photograph Door",                 False,True ,False,""),
                (12, "Photograph Spinner",              False,True ,False,""),
                (13, "Tier 2 Photographs Complete",     False,False,False,""),
                (14, "Photograph Jean Bison",           False,True ,False,""),
                (15, "Jean Bison Monologue",            False,False,False,"Take lighthouse photos"),
                (16, "Job Complete",                    False,False,False,""),
            )),
        ),
        ( # Day 2
            ("Bearcave Bugging",(
                (18, "Job Start",               True ,False,False,""),
                (19, "Enter Bearcave",          True ,False,False,""),
                (20, "Collect Radio Tag #1",    False,False,True ,""),
                (21, "Collect Radio Tag #2",    False,False,True ,""),
                (22, "Collect Radio Tag #3",    False,False,True ,""),
                (23, "Collect Radio Tag #4",    False,False,True ,""),
                (24, "Collect Radio Tag #5",    False,False,True ,""),
                (25, "Collect Radio Tag #6",    False,False,True ,""),
                (26, "Collect All Radio Tags",  False,False,False,"Snatch tags from the bears"),

                (27, "Go Back Outside",     True ,False,False,""),
                (28, "Place Radio Tag #1",  False,False,False,""),
                (29, "Place Radio Tag #2",  False,False,False,""),
                (30, "Place Radio Tag #3",  False,False,False,""),
                (31, "Place Radio Tag #4",  False,False,False,""),
                (32, "Place Radio Tag #5",  False,False,False,""),
                (33, "Place Radio Tag #6",  False,False,False,""),
                (34, "Job Complete",        False,False,False,"Place all the tags outside"),
            )),
# This Job features Sly stealing a Moose Head for Murray, but doesn't use the
# normal stealing "You Got an Item!" animation, which is what I am basing the
# "IS_STEALING" value for each of these tuples. If enough people complain about
# this specific task not counting as a "stealing" location, then we COULD change
# this to comply, but :shrug: idk if I'd want to anyway.
            ("RC Combat Club",(
                (35, "Job Start",           True ,False,False,""),
                (36, "Get into the mill",   True ,False,False,"Break inside the mulch mill"),

                (37, "Hide Murray",         False,False,False,""),
                (38, "Sly gets the costume",True ,False,False,"Steal a disguise for Murray"),

                (39, "RC Drone Duel",   True ,False,False,""),
                (40, "Job Complete",    False,False,False,"Win the RC drone duel"),
            )),
            ("Laser Redirection",(
                (41, "Job Start",           True ,False,False,""),
                (42, "Laser Instructions",  False,False,False,""),
                (43, "Jean Bison Laser PA", False,False,False,""),
                (44, "Redirect Laser",      False,False,False,"Point the laser outside"),

                (45, "Go Back Outside", True ,False,False,""),
                (46, "Laser Crystal #1",True ,False,False,""),
                (47, "Break the Ice #1",False,False,False,""),
                (48, "Laser Crystal #2",True ,False,False,""),
                (49, "Laser Crystal #3",True ,False,False,""),
                (50, "Laser Crystal #4",True ,False,False,""),
                (51, "Laser Crystal #5",True ,False,False,""),
                (52, "Break the Ice #2",False,False,False,""),
                (53, "Laser Crystal #6",True ,False,False,""),
                (54, "Job Complete",    False,False,False,"Use crystals to free book"),
            )),
        ),
        ( # Day 3
            ("Lighthouse Break-In",(
                (56, "Job Start",                   True ,False,False,""),
                (57, "Get on Top of the Lighthouse",False,False,False,""),
                (58, "Go into the Hatch",           True ,False,False,"Get inside the lighthouse"),

                (59, "Jean Bison Lighthouse PA",False,False,False,""),
                (60, "Open the Door",           True ,False,False,""),
                (61, "Back up the Lighthouse",  False,False,False,""),
                (62, "Job Complete",            False,False,False,"Shut down power to battery"),
            )),
            ("Old Grizzle Face",(
                (63, "Job Start",       True ,False,False,""),
                (64, "Bear Station #1", True ,False,False,""),
                (65, "Bear Station #2", True ,False,False,""),
                (66, "Bear Station #3", True ,False,False,""),
                (67, "Bear Station #4", True ,False,False,""),
                (68, "Job Complete",    False,False,False,"Use bear to wreck oil mains"),
            )),
            ("Boat Hack",(
                (69, "Job Start",       True ,False,False,""),
                (70, "Throw to Boat #1",False,False,False,""),
                (71, "Hack Boat #1",    False,False,False,""),
                (72, "Grapple Boat #1", False,False,False,""),
                (73, "Complete Boat #1",True ,False,False,""),
                (74, "Throw to Boat #2",False,False,False,""),
                (75, "Hack Boat #2",    False,False,False,""),
                (76, "Grapple Boat #2", False,False,False,""),
                (77, "Complete Boat #2",True ,False,False,""),
                (78, "Throw to Boat #3",False,False,False,""),
                (79, "Hack Boat #3",    False,False,False,""),
                (80, "Grapple Boat #3", False,False,False,""),
                (81, "Complete Boat #3",True ,False,False,""),
                (82, "Job Complete",    False,False,False,"Attach boat grapples to silo"),
            )),
            ("Thermal Ride",(
                (83, "Job Start",   True ,False,False,""),
                (84, "Get Height",  False,False,False,""),
                (85, "Eagle Attack",False,False,False,""),
                (86, "Get Egg",     False,False,True ,"Ride thermals to the Iceberg"),

                (87, "Return to the Safehouse", True ,False,False,""),
                (88, "Job Complete",            False,False,False,"Bring egg to safehouse"),
            )),
        ),
        ( # Day 4
            ("Operation: Canada Games", (  # "Compound-Job" #4
                ("Operation: Canada Games", (
                    (91, "Heist Start",                 True ,False,False,""),
                    (92, "Go to Jean Bison",            False,False,False,""),
                    (93, "Talk to Jean Bison",          False,False,False,""),
                    (94, "Power Chop Start",            True ,False,False,""),
                    (95, "Power Chop",                  False,False,False,""),
                    (96, "Power Chop Complete",         False,False,False,""),
                    (97, "Power Chop Cheat Start",      True ,False,False,""),
                    (98, "Power Chop Cheat",            False,False,False,""),
                    (99, "Power Chop Cheat Complete",   False,False,False,"Win the power chop event"),

                    (100,"Power Climb Start",           True ,False,False,""),
                    (101,"Power Climb",                 False,False,False,""),
                    (102,"Power Climb Complete",        False,False,False,""),
                    (103,"Power Climb Cheat Start",     True ,False,False,""),
                    (104,"Power Climb Cheat",           False,False,False,""),
                    (105,"Power Climb Cheat Complete",  False,False,False,"Win the power climb event"),

                    (106,"Log Rolling Start",           True ,False,False,""),
                    (107,"Log Rolling",                 False,False,False,""),
                    (108,"Log Rolling Complete",        False,False,False,""),
                    (109,"Log Rolling Cheat Start",     True ,False,False,""),
                    (110,"Alarm Clock Reminder",        False,False,False,""),
                    (111,"Log Rolling Cheat",           False,False,False,""),
                    (112,"Log Rolling Cheat Complete",  False,False,False,"Win the log rolling event"),
                )),
                ("Brains over Brawn", (
                    (113,"Job Start",           True ,False,False,""),
                    (114,"Boss Fight Start",    True ,False,False,""),
                    (115,"Boss Fight Phase 1",  False,False,False,""),
                    (116,"Boss Fight Phase 2",  False,False,False,""),
                    (117,"Boss Fight Phase 3",  False,False,False,""),
                    (118,"Boss Fight Phase 4",  False,False,False,""),
                    (119,"Boss Fight Complete", True ,False,False,"Defeat Jean Bison"),

                    (120,"Get to the Battery",  False,False,False,""),
                    (121,"Heist Complete",      False,False,False,"Stow aboard the battery"),
                )),
            )),
        ),
    ),  # (TASK_NUM, TASK_NAME, IS_CHECKPOINT, IS_PHOTOGRAPHY, IS_STEALING, OBJECTIVE)
    "Anatomy for Disaster": (
        ( # Day 1
            ("Overworld", (
                (1, "Episode Intro",    False,False,False,""),
                (25,"Chalk-talk #1",    False,False,False,""),
                (80,"Chalk-talk #1",    False,False,False,""),
                (99,"Episode Complete", False,False,False,""),
            )),
# Believe it or not, this job could be considered a "Compound-Job" due to its unique
# structure of it having a cutscene after completing the mission. That cutscene
# in-of-itself is its own, lone dedicated task that is assigned to an entirely
# separate Job than the rest of the Tasks that came before it.
#
# The thing is though, unlike EVERY OTHER "Compound-Job" in the game, and really
# unlike every other job in the game really, this 2nd Micro-Job doesn't even show
# up in the Job Help menu. Even the Fake Job in Ep2 appears on that screen, it has
# a name and an Objective in the code and everything! So the question now is this:
# Should we count this single Task as its own Job to make this a "Compound-Job",
# or should we just include it w/ the Job before it and make this much simpler and
# not have to worry about covering for this one specific corner-case of a corner-
# case. For the sake of making the code simpler, I'll just include it as a part of
# the previous Job.
            ("Blimp HQ Recon",(  # ALMOST a "Compound-Job"
                (2, "Job Start",        True ,False,False,""),
                (3, "Break the Vent",   False,False,False,""),
                (4, "Enter the Blimp",  True ,False,False,""),
                (5, "Recon Start",      False,False,False,"Break into the blimp HQ"),

                (6, "Photograph Eggs",              False,True ,False,""),
                (7, "Photograph Clockwerk",         False,True ,False,""),
                (8, "Photograph Platform",          False,True ,False,""),
                (9, "Tier 1 Photographs Complete",  True ,False,False,""),
                (10,"Spot Neyla",                   True ,False,False,""),
                (11,"Photograph Neyla",             False,True ,False,""),
                (12,"Photograph Arpeggio",          False,True ,False,""),
                (13,"Photography Complete",         True ,False,False,"Take needed recon photos"),

                (14,"Pickpocket Key #1",True ,False,True ,""),
                (15,"Pickpocket Key #2",True ,False,True ,""),
                (16,"Pickpocket Key #3",True ,False,True ,""),
                (17,"Pickpocket Key #4",True ,False,True ,""),
                (18,"Switch Slowdown",  True ,False,False,"Pickpocket keys, hit switch"),

                (19,"Switch #1",                True ,False,False,""),
                (20,"Switch #2",                True ,False,False,""),
                (21,"Switch #3",                True ,False,False,""),
                (22,"Switch #4",                True ,False,False,""),
                (23,"Job Complete",             False,False,False,"Reverse platforms’ polarity"),
                (24,"Post Recon Confrontation", False,False,False,""),
            )),
        ),
        ( # Day 2
            ("Charged TNT Run",(
                (26,"Job Start",            True ,False,False,""),
                (27,"Collect Charger #1",   True ,False,False,""),
                (28,"Collect Charger #2",   True ,False,False,""),
                (29,"Collect Charger #3",   True ,False,False,""),
                (30,"Collect All Chargers", False,False,False,""),
                (31,"Job Complete",         False,False,False,"Get chargers to blow engine"),
            )),
            ("Murray/Sly Tag Team",(
                (32,"Job Start",                True ,False,False,""),
                (33,"Destroy Power Station #1", True ,False,False,""),
                (34,"Destroy Power Station #2", True ,False,False,""),
                (35,"Destroy Power Station #3", True ,False,False,""),
                (36,"Destroy Power Station #4", True ,False,False,""),
                (37,"Destroy Power Station #5", True ,False,False,""),
                (38,"Open Engine Door",         True ,False,False,"Destroy the power stations"),

                (39,"Enter the Engine Room",    True ,False,False,""),
                (40,"Get to the Upper Floor",   False,False,False,""),
                (41,"Shut Down the Engine",     True ,False,False,""),
                (42,"Job Complete",             False,False,False,"Shutdown the engine room"),
            )),
            ("Sly/Bentley Conspire",(
                (43,"Job Start",                True ,False,False,""),
                (44,"Pickpocket Key #1",        True ,False,True ,""),
                (45,"Pickpocket Key #2",        True ,False,True ,""),
                (46,"Pickpocket Key #3",        True ,False,True ,""),
                (47,"Pickpocket Key #4",        True ,False,True ,""),
                (48,"Pickpocket Key #5",        True ,False,True ,""),
                (49,"Unlock Engine Room Door",  True ,False,False,"Pickpocket the door keys"),

                (50,"Shoot the Bulbs",      False,False,False,""),
                (51,"Bomb the Power Nodes", True ,False,False,""),
                (52,"Job Complete",         False,False,False,"Disable the engine room"),
            )),
            ("Bentley/Murray Team Up",(
                (53,"Job Start",        True ,False,False,""),
                (54,"Hack Station #1",  False,False,False,""),
                (55,"Go to Station #2", True ,False,False,""),
                (56,"Hack Station #2",  False,False,False,""),
                (57,"Go to Station #3", True ,False,False,""),
                (58,"Hack Station #3",  False,False,False,""),
                (59,"Open the Door",    True ,False,False,"Hack the blimp computers"),

                (60,"Go into the Engine Room",  False,False,False,""),
                (61,"Lift Cylinder #1",         False,False,False,""),
                (62,"Lift Cylinder #2",         False,False,False,""),
                (63,"Lift Cylinder #3",         False,False,False,""),
                (64,"Lift Cylinder #4",         False,False,False,""),
                (65,"Lift Cylinder #5",         False,False,False,""),
                (66,"Lift Cylinder #6",         False,False,False,""),
                (67,"Lift Cylinder #7",         False,False,False,""),
                (68,"Lift Cylinder #8",         False,False,False,""),
                (69,"Lift All Cylinders",       True ,False,False,""),
                (70,"Thunderflop Cylinder #1",  False,False,False,""),
                (71,"Thunderflop Cylinder #2",  False,False,False,""),
                (72,"Thunderflop Cylinder #3",  False,False,False,""),
                (73,"Thunderflop Cylinder #4",  False,False,False,""),
                (74,"Thunderflop Cylinder #5",  False,False,False,""),
                (75,"Thunderflop Cylinder #6",  False,False,False,""),
                (76,"Thunderflop Cylinder #7",  False,False,False,""),
                (77,"Thunderflop Cylinder #8",  False,False,False,""),
                (78,"Thunderflop All Cylinders",False,False,False,""),
                (79,"Job Complete",             False,False,False,"Cripple the engine room"),
            )),
        ),
        ( # Day 3 (Or 3 & 4)
# This day could be split into 2 to have this episode be 4 days like the rest, which
# is actually how the original implementation has it setup, but instead I am going
# to make this a .yaml option to have this and Ep4 be either 3 days or 4 days, and
# I am just going to handle that logic elsewhere rather than encode it into this.
            ("Mega-Jump Job",(
                (81,"Job Start",            True ,False,False,""),
                (82,"Mega-Jump Switch #1",  False,False,False,""),
                (83,"Mega-Jump Switch #2",  False,False,False,""),
                (84,"Mega-Jump Switch #3",  False,False,False,""),
                (85,"Mega-Jump Switch #4",  False,False,False,""),
                (86,"Job Complete",         False,False,False,"Get on top of all four towers"),
            )),
            ("Carmelita's Gunner/Showdown with Clock-La", (  # "Compound-Job" #5
                ("Carmelita's Gunner", (
                    (87,"Job Start",                True ,False,False,""),
                    (88,"Boss Fight Turret Phase",  False,False,False,""),
                    (89,"Job Complete",             False,False,False,"Shoot down Clock-La"),
                )),
                ("Showdown with Clock-La", (
                    (90,"Job Start",                            True ,False,False,""),
                    (91,"Chase Clock-La",                       False,False,False,""),
                    (92,"Boss Fight Bash Head Phase Start",     True ,False,False,""),
                    (93,"Boss Fight Bash Head Phase",           False,False,False,""),
                    (94,"Boss Fight Bash Head Phase Complete",  False,False,False,"Catch up to Clock-La"),

                    (95,"Boss Fight Open Head Phase Start", True ,False,False,""),
                    (96,"Murray Open Head",                 False,False,False,""),
                    (97,"Bentley Bomb Head",                False,False,False,""),
                    (98,"Boss Fight Complete",              False,False,True ,"Destroy Clock-La"),
                )),
            )),
        ),
    ),
}

TREASURES = {
    "The Black Chateau": [
        ("Jade Vase", 2),
        ("Ivory Jewel Box", 2),
        ("Crystal Chalice", 2),
    ],
    "A Starry Eyed Encounter": [
        ("Ancestral Kite", 1),
        ("Burial Urn", 1),
        ("Ming Vase", 1),
    ],
    "The Predator Awakens": [
        ("Gilded Scepter", 1),
        ("Golden Scroll Case", 1),
        ("Crystal Flask", 1),
    ],
    "Jailbreak": [
        ("Golden Orb", 1),
        ("Crystal Ball", 1),
        ("Ceremonial Lantern", 1),
    ],
    "A Tangled Web": [
        ("Jeweled Crown", 1),
        ("Royal Tiara", 1),
        ("Crystal Vase", 1),
    ],
    "He Who Tames the Iron Horse": [
        ("Crystal Bell", 1),
        ("Alabaster Chalice", 1),
        ("Golden Plate", 1),
    ],
    "Menace from the North, Eh!": [
        ("Jeweled Chalice", 1),
        ("Collectible Plate", 1),
        ("Jade Decanter", 1),
    ],
    "Anatomy for Disaster": [
        ("Golden Headdress", 1),
        ("Jeweled Egg", 1),
        ("Golden Vase", 1),
    ],
}

# (episode, large guard, table slot)
LOOT = {
    "Bronze Comb": [(1,False,1)],
    "Silver Comb": [(1,False,2),(1,True,2)],
    "Gold Comb": [(1,True,1)],

    "Bronze Ring": [(1,False,5), (2,False,1), (3,False,1)],
    "Silver Ring": [(1,False,6), (1,True,6), (2,False,2), (2,True,2), (3,False,2), (3,True,2)],
    "Gold Ring": [(1,True,5), (2,True,1), (3,True,1)],

    "Bronze Watch": [(1,False,3)],
    "Silver Watch": [(1,False,4),(1,True,4)],
    "Gold Watch": [(1,True,3)],

    "Bronze Pen": [(2,False,3), (3,False,3)],
    "Silver Pen": [(2,False,4), (2,True,4), (3,False,4), (3,True,4)],
    "Gold Pen": [(2,True,3), (3,True,3)],

    "Bronze Medal": [(2,False,5), (3,False,5), (4,False,1), (5,False,1)],
    "Silver Medal": [(2,False,6), (2,True,6), (3,False,6), (3,True,6), (4,False,2), (4,True,2), (5,False,2), (5,True,2)],
    "Gold Medal": [(2,True,5), (3,True,5), (4,True,1), (5,True,1)],

    "Bronze Pocket Watch": [(4,False,3), (5,False,3)],
    "Silver Pocket Watch": [(4,False,4), (4,True,4), (5,False,4), (5,True,4)],
    "Gold Pocket Watch": [(4,True,3), (5,True,3)],

    "Small Nugget": [(6,False,3), (7,False,3), (8,False,1)],
    "Medium Nugget": [(6,False,4), (6,True,4), (7,False,4), (7,True,4), (8,False,2), (8,True,2)],
    "Large Gold Bar": [(6,True,3), (7,True,3), (8,True,1)],

    "Topaz": [(4,False,5), (5,False,5), (6,False,1), (7,False,1)],
    "Sapphire": [(4,False,6), (4,True,6), (5,False,6), (5,True,6), (6,False,2), (6,True,2), (7,False,2), (7,True,2)],
    "Ruby": [(4,True,5), (5,True,5), (6,True,1), (7,True,1)],

    "Small Diamond": [(8,False,5)],
    "Medium Diamond": [(8,False,6),(8,True,6)],
    "Large Diamond": [(8,True,5)],

    "Small Necklace": [(6,False,5), (7,False,5), (8,False,3)],
    "Medium Necklace": [(6,False,6), (6,True,6), (7,False,6), (7,True,6), (8,False,4), (8,True,4)],
    "Large Necklace": [(6,True,5), (7,True,5), (8,True,3)],
}

LOOT_IDS = {loot: 0x45A+i for i, loot in enumerate(LOOT.keys())}

ENEMIES = [
  ("Rats/Frogs", "Boars"),
  ("Monkeys/Goats", "Rhinos"),
  ("Monkeys/Goats", "Rhinos"),
  ("Wolves/Bats", "Vultures"),
  ("Wolves/Bats", "Vultures"),
  ("Geese/Goats/Carmelita", "Moose"),
  ("Geese/Goats", "Moose"),
  ("Swarmer Pelicans", "Pelicans")
]

HUB_MAPS = [
    2,
    8,
    12,
    14,
    17,
    27,
    32,
    38
]

DEATH_TYPES = {
    0x200: "{player} was killed",
    0x400: "{player} was flattened",
    0x800: "{player} was electrocuted",
    0x1000: "{player} was burned to death",
    0x2000: "{player} drowned",
    0x1000: "{player} fell to their death",
}

HEALTH_MULTIPLIERS = {
    "Sly": 8,
    "Bentley": 8,
    "Murray": 12,
    "India1_Turret": 1,
    "India1_RCChopper": 20,
    "India2_Turret": 60,
    "Prague1_RCChopper": 20,
    "Prague2_Tank": 28, # remember that this one is a float
    "Prague2_Turret": 9, # remember that this one is 1 byte
    "Canada1_RCChopper1": 20,
    "Canada1_RCChopper2": 20,
    "Canada2_RCCar": 20,
    "Carmelita_Turret": 60,
}

ADDRESSES = {
    "SCUS-97316": {
        "unload mega jump": 0x20ECD4,
        "loading": 0x3D3980,
        "world id": 0x3D4A60,
        "savefile last world": 0x3D4A64,
        "map id": 0x3E1110,
        "job id": 0x2DEB44,
        "DAG root": 0x3E0B04,
        "episode unlocks": 0x5975E8,
        "thiefnet control": 0x3DA160,
        "reload": 0x3E1080,
        "reload values": 0x3E1088,
        "camera focus": 0x2DE258,
        "fade type": 0x443798,
        "items received": 0x3D57FC,
        "coins": 0x3D4B00,
        "gadgets": 0x3D4AF8,
        "active character": 0x3D4A6C,
        "active character pointer": 0x2DE2F0,
        "string table": 0x3e1ad4,
        "frame counter": 0x2F67D0,
        "input": 0x2E0CB4,
        "skip cutscene": 0x2F6810,
        "infobox": 0x3DA0E8,
        "infobox scrolling": 0x3DA0D0,
        "infobox string": 0x3DA0D8,
        "infobox duration": 0x3DA0DC,
        "hackpack": 0x3E0828,
        "operation completion": [
            0x3D5810, # Operation: Thunder Beak
            0x3D5910, # Operation: Hippo Drop
            0x3D5980, # Operation: Wet Tiger
            0x3D5A50, # Operation: Trojan Tank
            0x3D5AF0, # Operation: High Road
            0x3D5B40, # Operation: Choo-Choo
            0x3D5BE0, # Operation: Canada Games
            0x3D5C50  # Defeat Clock-la
        ],
        "job completion": [
            0x3D5800, # Cairo Museum Break-In

            0x3D58A0, # Satellite Sabotage
            0x3D5890, # Breaking and Entering
            0x3D5850, # Follow Dimitri
            0x3D5830, # Bug Dimitri's Office
            0x3D58B0, # Waterpump Destruction
            0x3D5820, # Silence the Alarms
            0x3D5870, # Theater Pickpocketing
            0x3D5880, # Moonlight Rendezvous
            0x3D5840, # Disco Demolitions
            0x3D5860, # Operation: Thunder Beak
            0x3D5810, # Printing Press Duel

            0x3D5950, # Recon the Ballroom
            0x3D5930, # Lower the Drawbridge
            0x3D58E0, # Ballroom Dance Party
            0x3D5960, # Steal a Tuxedo
            0x3D58D0, # Dominate the Dance Floor
            0x3D5970, # Battle the Chopper
            0x3D58C0, # Boardroom Brawl
            0x3D5940, # RC Bombing Run
            0x3D58F0, # Elephant Rampage
            0x3D5900, # Bomb the Bridge (Operation: Hippo Drop)
            0x3D5920, # Tango with Carmelita
            0x3D5910, # Clear the Way for Murray

            0x3D59D0, # Spice Room Recon
            0x3D5A10, # Water Bug Run
            0x3D5990, # Freeing the Elephant
            0x3D59C0, # Leading Rajan
            0x3D59A0, # Neyla's Secret
            0x3D59F0, # Spice Grinder Destruction
            0x3D5A00, # Blow the Dam
            0x3D59E0, # Rip-Off the Ruby
            0x3D59B0, # Operation: Wet Tiger
            0x3D5980, # Showdown with Rajan

            0x3D5A90, # Eavesdrop on Contessa
            0x3D5A40, # Train Hack
            0x3D5A80, # Wall Bombing
            0x3D5A30, # Big House Brawl
            0x3D5A60, # Lightning Action
            0x3D5A20, # Disguise Bridge
            0x3D5A90, # Code Capture
            0x3D5A70, # Close to Contessa
            0x3D5A50, # Operation: Trojan Tank

            0x3D5B20, # Know your Enemy
            0x3D5AD0, # Ghost Capture
            0x3D5AC0, # Mojo Trap Action
            0x3D5B00, # Kidnap the General
            0x3D5B10, # Stealing Voices
            0x3D5AB0, # Tank Showdown
            0x3D5AE0, # Crypt Hack
            0x3D5AF0, # Operation: High Road

            0x3D5B80, # Cabin Crimes
            0x3D5B60, # Spice in the Sky
            0x3D5B30, # A Friend in Need
            0x3D5BA0, # Ride the Iron Horse
            0x3D5B50, # Bear Cub Kidnapping
            0x3D5B70, # Aerial Assault
            0x3D5B90, # Theft on Rails
            0x3D5B40, # Operation: Choo-Choo

            0x3D5C20, # Recon the Sawmill
            0x3D5BC0, # Bearcave Bugging
            0x3D5C00, # Laser Redirection
            0x3D5C30, # RC Combat Club
            0x3D5C10, # Lighthouse Break-In
            0x3D5BB0, # Old Grizzle Face
            0x3D5C40, # Thermal Ride
            0x3D5BD0, # Boat Hack
            0x3D5BF0, # Operation: Canada Games
            0x3D5BE0, # Brains Over Brawn

            0x3D5CB0, # Blimp HQ Recon
            0x3D5CC0, # Charged TNT Run
            0x3D5C60, # Sly/Bentley Conspire
            0x3D5C70, # Murray/Sly Tag Team
            0x3D5C80, # Bentley/Murray Team Up
            0x3D5C90, # Mega Jump-Job
            0x3D5CD0, # Carmelita's Gunner
            0x3D5C50, # Showdown with Clock-La
        ],
        # TODO: Rename all of the non-gang addresses to be more consistent & easier to understand.
        #  Don't want to rename rn since idk what will break & I don't want to search for these yet.
        "health": {
            "Sly": 0x3d4ab0,
            "Bentley": 0x3d4ac8,
            "Murray": 0x3d4ae0,
            "TurretIndia": 0x5A5BA0, # India1_Turret
            "ChopperIndia": 0x5A68F0, # India1_RCChopper
            "TurretIndia2": 0x525600, # India2_Turret
            "ChopperPrague": 0x52A560, # Prague1_RCChopper
            "Tank": 0x5616C0, # Prague2_Tank
            "Blimp": 0x563F10, # Prague2_Turret
            "ChopperCanada1": 0x5523D0, # Canada1_RCChopper1
            "ChopperCanada2": 0x500618, # Canada1_RCChopper2
            "RCTank": 0xDF0AE0, # Canada2_RCCar
            "ChopperCarmelita": 0x50EE50 # Carmelita_Turret
        },
        "health GUIs": {
          # TODO: Find all of the HP GUIs for each of the above playable entities
          #  so that when we update their HP ourselves we can also update the HUD
          #  to properly & accurately display the correct amount of current HP.
        },
        "guard structs": [
            0x3E0774,  # swarmer 1
            0x3E0778,  # swarmer 2
            0x3E0780,  # flashlight guard
        ],
        "bottle flags": [
            0x3D4CD8,
            0x3D4E78,
            0x3D4F90,
            0x3D5020,
            0x3D50F4,
            0x3D53A4,
            0x3D5500,
            0x3D56A0
        ],
        "bottle count": 0x3E1BF4,
        "thiefnet costs": [0x2BCDE8+i*0x20 for i in range(24)],
        "thiefnet unlock": [0x2BCDF0+i*0x20 for i in range(24)],
        "clock-la defeated": 0x3D9AF0,  # Will want to check if this is still necessary, and if so then also check if
                                        # this is also necessary for the other bosses.
        "jobs": [
            [
                [4,10],
                [36,43,75],
                [31,48,60,63],
                [83]
            ],
            [
                [2],
                [16,37,46,25],
                [29,51,54],
                [65]
            ],
            [
                [2],
                [14,17,35],
                [27,46,56,58],
                [(67,76)]
            ],
            [
                [1,8,21],
                [33,37,49,54,68],
                [78]
            ],
            [
                [1],
                [16,32,41],
                [46,62,70],
                [80]
            ],
            [
                [1],
                [18,29,26],
                [44,51,48],
                [60]
            ],
            [
                [2],
                [17,34,40],
                [55,62,68,82],
                [(90,112)]
            ],
            [
                [1],
                [25,31,42,52],
                [80],
                [86]
            ]
        ],
        # Old implementation of making Tasks Checks. TODO: Delete this when no longer used.
        "tasks": [
            [   # Prologue
                [ 1, 2, 3,16],  # Overworld
                [ 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]  # Museum Break-In
            ],
            [   # Episode 1
                [ 1, 2, 3, 4,29,30,31,43,48,60,83,99],  # Overworld (Need to double-check these b/c of the Chalk-talk #3 Task)
                [ 5, 6, 7, 8, 9],  # OSatellite Sabotage
                [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],  # Breaking and Entering
                [37,38,39,40,41,42],  # Bug Dimitri's Office
                [44,45,46,47],  # Follow Dimitri
                [76,77,78,79,80,81,82],  # Waterpump Destruction
                [32,33,34,35,36],  # Silence the Alarms
                [49,50,51,52,53,54,55,56,57,58,59],  # Theater Pickpocketing
                [61,62,63],  # Moonlight Rendezvous
                [64,65,66,67,68,69,70,71,72,73,74,75],  # Disco Demolitions
                [84,85,86,87,88,89,90,91,92,93,94],  # Operation: Thunder Beak
                [95,96,97,98]  # Printing Press Duel
            ],
            [   # Episode 2
                [ 1, 2,16,51,65,93],  # Overworld
                [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15],  # Recon the Ballroom
                [17,18,19,20,21,22,23,24,25],  # Lower the Drawbridge
                [26,27,28,29],  # Battle the Chopper
                [37],  # Ballroom Dance Party
                [38,39,40,41,42,43,44,45,46],  # Steal a Tuxedo
                [47,48,49,50],  # Dominate the Dance Floor
                [30,31,32,33,34,35,36],  # Boardroom Brawl
                [52,53,54],  # Bombing Run
                [55,56,57,58,59,60,61,62,63,64],  # Elephant Rampage
                [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87],  # Operation: Hippo Drop/Bomb the Bridge
                [88,89,90],  # Tango with Carmelita
                [91,92]  # Clear the Way for Murray
            ],
            [   # Episode 3
                [ 1, 2,14,56,66,82],  # Overworld (Need to double-check these b/c of the Spice Grinder Door Task)
                [ 3, 4, 5, 6, 7, 8, 9,10,11,12,13],  # Spice Room Recon
                [15,16,17],  # Water Bug Run
                [18,19,20,21,22,23,24,25,26,27],  # Freeing the Elephant
                [36,37,38,39,40,41,42,43,44,45,46],  # Leading Rajan
                [28,29,30,31,32,33,34,55],  # Neyla's Secret
                [47,48,49,50,51,52,53,54,55],  # Spice Grinder Destruction
                [57,58],  # Blow the Dam
                [59,60,61,62,63,64,65],  # Rip-off the Ruby
                [67,68,69,70,71,72,73,74,75,76],  # Operation: Wet Tiger
                [77,78,79,80,81]  # Showdown with Rajan
            ],
            [   # Episode 4
                [ 1,33,77,110],  # Overworld
                [ 2, 3, 4, 5, 6, 7, 8],  # Eavesdrop on Contessa
                [ 9,10,11,12,13,14,15,16,17,18,19,20,21],  # Train Hack
                [22,23,24,25,26,27,28,29,30,31,32],  # Wall Bombing
                [34,35,36,37],  # Big House Brawl
                [38,39,40,41,42,43,44,45,46,47,48,49],  # Lightning Action
                [50,51,52,53,54],  # Disguise Bridge
                [55,56,57,58,59,60,61,62,63,64,65,66,67,68],  # Code Capture
                [69,70,71,72,73,74,75,76],  # Close to Contessa
                [78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,
                 100,101,102,103,104,105,106,107,108,109]  # Operation: Trojan Tank
            ],
            [   # Episode 5
                [ 1,16,46,79,80,102],  # Overworld
                [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15],  # Know your Enemy
                [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32],  # Ghost Capture
                [33,34,35,36,37,38,39,40,41],  # Mojo Trap Action
                [42,43,44,45],  # Kidnap the General
                [47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62],  # Stealing Voices
                [63,64,65,66,67,68,69,70],  # Tank Showdown
                [71,72,73,74,75,76,77,78],  # Crypt Hack
                [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101]  # Operation: High Road
            ],
            [   # Episode 6
                [ 1,17,18,44,60,72],  # Overworld
                [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16],  # Cabin Crimes
                [19,20,21,22,23,24,25,26],  # Spice in the Sky
                [27,28,29],  # Ride the Iron Horse
                [30,31,32,33,34,35,36,37,38,39,40,41,42,43],  # A Friend in Need
                [45,46,47,48],  # Aerial Assault
                [49,50,51],  # Theft on the Rails
                [52,53,54,55,56,57,58,59],  # Bear Cub Kidnapping
                [61,62,63,64,65,66,67,68,69,70,71]  # Operation: Choo-Choo
            ],
            [   # Episode 7
                [ 1, 2,17,55,89,90,122],  # Overworld
                [ 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16],  # Recon the Sawmill
                [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],  # Bearcave Bugging
                [35,36,37,38,39,40],  # RC Combat Club
                [41,42,43,44,45,46,47,48,49,50,51,52,53,54],  # Laser Redirection
                [56,57,58,59,60,61,62],  # Lighthouse Break In
                [63,64,65,66,67,68],  # Old Grizzle Face
                [69,70,71,72,73,74,75,76,77,78,79,80,81,82],  # Boat Hack
                [83,84,85,86,87,88],  # Thermal Ride
                [90,91,92,93,94,95,96,97,98,99,
                 100,101,102,103,104,105,106,107,108,109,110,111,112],  # Operation: Canada Games
                [113,114,115,116,117,118,119,120,121]  # Brains over Brawn
            ],
            [   # Episode 8
                [ 1,25,80,99],  # Overworld
                [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],  # Blimp HQ Recon
                [24],  # Post Recon
                [26,27,28,29,30,31],  # Charged TNT Run
                [32,33,34,35,36,37,38,39,40,41,42],  # Murray/Sly Tag Team
                [43,44,45,46,47,48,49,50,51,52],  # Sly/Bentley Conspire
                [53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79],  # Bentley/Murray Team Up
                [81,82,83,84,85,86],  # Mega-Jump Job
                [87,88,89],  # Carmelita's Gunner
                [90,91,92,93,94,95,96,97,98]  # Showdown with Clock-La
            ],
        ],
        "treasures": [
            [
                0x3D4BA8,
                0x3D4BA4,
                0x3D4BA0,
            ],
            [
                0x3D4BB0,
                0x3D4BB4,
                0x3D4BAC
            ],
            [
                0x3D4BC0,
                0x3D4BBC,
                0x3D4BB8,
            ],
            [
                0x3D4BCC,
                0x3D4BC8,
                0x3D4BC4,
            ],
            [
                0x3D4BD8,
                0x3D4BD4,
                0x3D4BD0,
            ],
            [
                0x3D4BDC,
                0x3D4BE0,
                0x3D4BE4,
            ],
            [
                0x3D4BF0,
                0x3D4BEC,
                0x3D4BE8
            ],
            [
                0x3D4BFC,
                0x3D4BF8,
                0x3D4C00,
            ]
        ],
        "treasure pedestals": [
            [
                0x3D4C9C,
                0x3D4CA0,
                0x3D4CA4,
            ],
            [
                0x3D4E3C,
                0x3D4E40,
                0x3D4E44,
            ],
            [
                0x3D4F74,
                0x3D4F78,
                0x3D4F7C,
            ],
            [
                0x3D4FE4,
                0x3D4FE8,
                0x3D4FEC,
            ],
            [
                0x3D50B8,
                0x3D50BC,
                0x3D50C0,
            ],
            [
                0x3D5368,
                0x3D536C,
                0x3D5370,
            ],
            [
                0x3D54C4,
                0x3D54C8,
                0x3D54CC,
            ],
            [
                0x3D5664,
                0x3D5668,
                0x3D566C,
            ]
        ],
        "vaults": [
            0x3D4D64,
            0x3D4F04,
            0x3D4FD8,
            0x3D50AC,
            0x3D51C4,
            0x3D53EC,
            0x3D558C,
            0x3D57B4
        ],
        "loot": [0x3D4B04+i*4 for i in range(len(LOOT))],
        "loot chance": [(0x2C378C+i*0x3c, 0x2C378C+i*0x3c+0x220) for i in range(8)],
        "loot table odds": [
            (
                tuple(0x2C3790+i*0x3c+j*0x8 for j in range(6)),
                tuple(0x2C3790+i*0x3c+0x220+j*0x8 for j in range(6)),
            )
            for i in range(8)
        ],
        "loot table": [
            (
                tuple(0x2C3794+i*0x3c+j*0x8 for j in range(6)),
                tuple(0x2C3794+i*0x3c+0x220+j*0x8 for j in range(6)),
            )
            for i in range(8)
        ],
        "text": {
            "infobox": [0x14,0x14,0x1c,0x24,0x24,0x1c,0x1c,0x14],
            "Press START (new)": 0x4b3970,
            "Press START (resume)": 0x4b39a0,
            "Episode 1": 0x4a3fe0,
            "Episode 2": 0x4a4490,
            "Episode 3": 0x4a4b10,
            "Episode 4": 0x4a5530,
            "Episode 5": 0x4a5b30,
            "Episode 6": 0x4a3040,
            "Episode 7": 0x4a3eb0,
            "Episode 8": 0x4a42e0,
            "this powerup.": [0x5c]*8,
            "right back": [
                0x504,
                0x474,
                0x4e4,
                0x4c4,
                0x62c,
                0x584,
                0x4ec,
                0x3bc,
            ],
            "powerups": [
                {
                    "Trigger Bomb": (0x4cb960,0x4cb9b0),
                    "Size Destabilizer": (0x4cba20,0x4cba90),
                    "Snooze Bomb": (0x4cbb10,0x4cbc10),
                    "Adrenaline Burst": (0x4cbcb0,0x4cbd60),
                    "Health Extractor": (0x4cbec0,0x4cbee0),
                    "Hover Pack": (0x4cbf60,0x4cbfe0),
                    "Reduction Bomb": (0x4cc060,0x4cc070),
                    "Temporal Lock": (0x4cc090,0x4cc0a0),
                    "Fists of Flame": (0x4cc120,0x4cc130),
                    "Turnbuckle Launch": (0x4cc160,0x4cc250),
                    "Juggernaut Throw": (0x4cc2b0,0x4cc310),
                    "Atlas Strength": (0x4cc390,0x4cc450),
                    "Diablo Fire Slam": (0x4cc500,0x4cc580),
                    "Berserker Charge": (0x4cc5d0,0x4cc600),
                    "Guttural Roar": (0x4cc640,0x4cc670),
                    "Raging Inferno Flop": (0x4cc6b0,0x4cc6d0),
                    "Smoke Bomb": (0x4cc710,0x4cc720),
                    "Combat Dodge": (0x4cc760,0x4cc770),
                    "Stealth Slide": (0x4cc790,0x4cc800),
                    "Alarm Clock": (0x4cc860,0x4cc8b0),
                    "Paraglide": (0x4cc990,0x4cc9f0),
                    "Silent Obliteration": (0x4cca40,0x4cca70),
                    "Thief Reflexes": (0x4ccad0,0x4ccb00),
                    "Feral Pounce": (0x4ccb30,0x4ccbb0),
                },
                {
                    "Trigger Bomb": (0x4c1b80,0x4c1cc0),
                    "Size Destabilizer": (0x4c1db0,0x4c1ee0),
                    "Snooze Bomb": (0x4c2000,0x4c20b0),
                    "Adrenaline Burst": (0x4c21a0,0x4c2360),
                    "Health Extractor": (0x4c2440,0x4c24e0),
                    "Hover Pack": (0x4c2590,0x4c25d0),
                    "Reduction Bomb": (0x4c2710,0x4c2780),
                    "Temporal Lock": (0x4c2830,0x4c2850),
                    "Fists of Flame": (0x4c2b90,0x4c2c90),
                    "Turnbuckle Launch": (0x4c2d40,0x4c2da0),
                    "Juggernaut Throw": (0x4c2df0,0x4c2ef0),
                    "Atlas Strength": (0x4c2f60,0x4c2fd0),
                    "Diablo Fire Slam": (0x4c30b0,0x4c3170),
                    "Berserker Charge": (0x4c3250,0x4c3320),
                    "Guttural Roar": (0x4c33a0,0x4c3470),
                    "Raging Inferno Flop": (0x4c34c0,0x4c3510),
                    "Smoke Bomb": (0x4c3580,0x4c35d0),
                    "Combat Dodge": (0x4c3640,0x4c3680),
                    "Stealth Slide": (0x4c36c0,0x4c3740),
                    "Alarm Clock": (0x4c37e0,0x4c3850),
                    "Paraglide": (0x4c38c0,0x4c3920),
                    "Silent Obliteration": (0x4c39e0,0x4c3a30),
                    "Thief Reflexes": (0x4c3aa0,0x4c3af0),
                    "Feral Pounce": (0x4c3b30,0x4c3b90),
                },
                {
                    "Trigger Bomb": (0x4c4f10,0x4c4fb0),
                    "Size Destabilizer": (0x4c5050,0x4c50e0),
                    "Snooze Bomb": (0x4c5140,0x4c5180),
                    "Adrenaline Burst": (0x4c51e0,0x4c5300),
                    "Health Extractor": (0x4c5360,0x4c5380),
                    "Hover Pack": (0x4c53b0,0x4c53c0),
                    "Reduction Bomb": (0x4c53f0,0x4c5400),
                    "Temporal Lock": (0x4c5420,0x4c5430),
                    "Fists of Flame": (0x4c54b0,0x4c54c0),
                    "Turnbuckle Launch": (0x4c54f0,0x4c5510),
                    "Juggernaut Throw": (0x4c5530,0x4c5550),
                    "Atlas Strength": (0x4c5580,0x4c55b0),
                    "Diablo Fire Slam": (0x4c55e0,0x4c5620),
                    "Berserker Charge": (0x4c5670,0x4c56b0),
                    "Guttural Roar": (0x4c5700,0x4c5740),
                    "Raging Inferno Flop": (0x4c57a0,0x4c5830),
                    "Smoke Bomb": (0x4c5890,0x4c58c0),
                    "Combat Dodge": (0x4c5920,0x4c5940),
                    "Stealth Slide": (0x4c59b0,0x4c5a30),
                    "Alarm Clock": (0x4c5ab0,0x4c5b40),
                    "Paraglide": (0x4c5bc0,0x4c5c20),
                    "Silent Obliteration": (0x4c5c80,0x4c5d00),
                    "Thief Reflexes": (0x4c5da0,0x4c5de0),
                    "Feral Pounce": (0x4c5e40,0x4c5ea0),
                },
                {
                    "Trigger Bomb": (0x4c7090,0x4c70e0),
                    "Size Destabilizer": (0x4c7140,0x4c71a0),
                    "Snooze Bomb": (0x4c7210,0x4c7280),
                    "Adrenaline Burst": (0x4c72e0,0x4c7350),
                    "Health Extractor": (0x4c73c0,0x4c73f0),
                    "Hover Pack": (0x4c7430,0x4c7450),
                    "Reduction Bomb": (0x4c74a0,0x4c74c0),
                    "Temporal Lock": (0x4c7520,0x4c7550),
                    "Fists of Flame": (0x4c7660,0x4c7690),
                    "Turnbuckle Launch": (0x4c76e0,0x4c7710),
                    "Juggernaut Throw": (0x4c7750,0x4c7790),
                    "Atlas Strength": (0x4c77f0,0x4c7820),
                    "Diablo Fire Slam": (0x4c7860,0x4c78b0),
                    "Berserker Charge": (0x4c7930,0x4c7980),
                    "Guttural Roar": (0x4c79f0,0x4c7a70),
                    "Raging Inferno Flop": (0x4c7aa0,0x4c7ba0),
                    "Smoke Bomb": (0x4c7c10,0x4c7c30),
                    "Combat Dodge": (0x4c7ca0,0x4c7d30),
                    "Stealth Slide": (0x4c7d80,0x4c7de0),
                    "Alarm Clock": (0x4c7eb0,0x4c7f20),
                    "Paraglide": (0x4c8050,0x4c80c0),
                    "Silent Obliteration": (0x4c8130,0x4c81a0),
                    "Thief Reflexes": (0x4c8250,0x4c8280),
                    "Feral Pounce": (0x4c8340,0x4c83c0),
                },
                {
                    "Trigger Bomb": (0x4cc3d0,0x4cc440),
                    "Size Destabilizer": (0x4cc4c0,0x4cc5f0),
                    "Snooze Bomb": (0x4cc6a0,0x4cc7c0),
                    "Adrenaline Burst": (0x4cc900,0x4cca10),
                    "Health Extractor": (0x4ccad0,0x4ccb70),
                    "Hover Pack": (0x4ccca0,0x4ccd40),
                    "Reduction Bomb": (0x4ccdb0,0x4cce50),
                    "Temporal Lock": (0x4cced0,0x4ccee0),
                    "Fists of Flame": (0x4cd060,0x4cd130),
                    "Turnbuckle Launch": (0x4cd1c0,0x4cd2a0),
                    "Juggernaut Throw": (0x4cd2e0,0x4cd310),
                    "Atlas Strength": (0x4cd350,0x4cd370),
                    "Diablo Fire Slam": (0x4cd3b0,0x4cd4d0),
                    "Berserker Charge": (0x4cd540,0x4cd590),
                    "Guttural Roar": (0x4cd5f0,0x4cd630),
                    "Raging Inferno Flop": (0x4cd670,0x4cd6d0),
                    "Smoke Bomb": (0x4cd730,0x4cd7d0),
                    "Combat Dodge": (0x4cd850,0x4cd890),
                    "Stealth Slide": (0x4cd8d0,0x4cd960),
                    "Alarm Clock": (0x4cda10,0x4cdac0),
                    "Paraglide": (0x4cdb40,0x4cdc00),
                    "Silent Obliteration": (0x4cdc70,0x4cdd60),
                    "Thief Reflexes": (0x4cde30,0x4cdef0),
                    "Feral Pounce": (0x4cdf30,0x4cdf80),
                },
                {
                    "Trigger Bomb": (0x4c2b40,0x4c2b80),
                    "Size Destabilizer": (0x4c2bd0,0x4c2c10),
                    "Snooze Bomb": (0x4c2c70,0x4c2cb0),
                    "Adrenaline Burst": (0x4c2d10,0x4c2d60),
                    "Health Extractor": (0x4c2d90,0x4c2db0),
                    "Hover Pack": (0x4c2de0,0x4c2df0),
                    "Reduction Bomb": (0x4c2e20,0x4c2e30),
                    "Temporal Lock": (0x4c2ea0,0x4c2eb0),
                    "Fists of Flame": (0x4c3060,0x4c30e0),
                    "Turnbuckle Launch": (0x4c31b0,0x4c3220),
                    "Juggernaut Throw": (0x4c32b0,0x4c3320),
                    "Atlas Strength": (0x4c3370,0x4c33b0),
                    "Diablo Fire Slam": (0x4c3470,0x4c34c0),
                    "Berserker Charge": (0x4c3530,0x4c35a0),
                    "Guttural Roar": (0x4c3650,0x4c36d0),
                    "Raging Inferno Flop": (0x4c3770,0x4c37f0),
                    "Smoke Bomb": (0x4c38a0,0x4c3950),
                    "Combat Dodge": (0x4c3aa0,0x4c3c70),
                    "Stealth Slide": (0x4c3d80,0x4c3e40),
                    "Alarm Clock": (0x4c3f70,0x4c3fb0),
                    "Paraglide": (0x4c4060,0x4c4150),
                    "Silent Obliteration": (0x4c41f0,0x4c42a0),
                    "Thief Reflexes": (0x4c4360,0x4c4430),
                    "Feral Pounce": (0x4c4460,0x4c4590),
                },
                {
                    "Trigger Bomb": (0x4d10c0,0x4d1160),
                    "Size Destabilizer": (0x4d11f0,0x4d12d0),
                    "Snooze Bomb": (0x4d1350,0x4d13f0),
                    "Adrenaline Burst": (0x4d14c0,0x4d1510),
                    "Health Extractor": (0x4d1570,0x4d15c0),
                    "Hover Pack": (0x4d1610,0x4d1670),
                    "Reduction Bomb": (0x4d16c0,0x4d1780),
                    "Temporal Lock": (0x4d17e0,0x4d1870),
                    "Fists of Flame": (0x4d1af0,0x4d1cd0),
                    "Turnbuckle Launch": (0x4d1e40,0x4d1ee0),
                    "Juggernaut Throw": (0x4d1fa0,0x4d2010),
                    "Atlas Strength": (0x4d2090,0x4d20a0),
                    "Diablo Fire Slam": (0x4d2110,0x4d2170),
                    "Berserker Charge": (0x4d21c0,0x4d22c0),
                    "Guttural Roar": (0x4d2360,0x4d2480),
                    "Raging Inferno Flop": (0x4d24d0,0x4d2530),
                    "Smoke Bomb": (0x4d26e0,0x4d2740),
                    "Combat Dodge": (0x4d2800,0x4d2910),
                    "Stealth Slide": (0x4d2970,0x4d2a10),
                    "Alarm Clock": (0x4d2ae0,0x4d2b50),
                    "Paraglide": (0x4d2bf0,0x4d2c90),
                    "Silent Obliteration": (0x4d2da0,0x4d2e10),
                    "Thief Reflexes": (0x4d2ee0,0x4d3010),
                    "Feral Pounce": (0x4d30c0,0x4d3120),
                },
                {
                    "Trigger Bomb": (0x4c4e60,0x4c4f00),
                    "Size Destabilizer": (0x4c4fd0,0x4c5170),
                    "Snooze Bomb": (0x4c5230,0x4c52b0),
                    "Adrenaline Burst": (0x4c53d0,0x4c5470),
                    "Health Extractor": (0x4c54f0,0x4c55a0),
                    "Hover Pack": (0x4c5600,0x4c56b0),
                    "Reduction Bomb": (0x4c5750,0x4c57e0),
                    "Temporal Lock": (0x4c58e0,0x4c5960),

                    "Fists of Flame": (0x4c5b70,0x4c5c20),
                    "Turnbuckle Launch": (0x4c5c90,0x4c5e10),
                    "Juggernaut Throw": (0x4c5e70,0x4c5f20),
                    "Atlas Strength": (0x4c5f80,0x4c60d0),
                    "Diablo Fire Slam": (0x4c61e0,0x4c6240),
                    "Berserker Charge": (0x4c6310,0x4c63a0),
                    "Guttural Roar": (0x4c6490,0x4c64f0),
                    "Raging Inferno Flop": (0x4c6630,0x4c6670),

                    "Smoke Bomb": (0x4c66f0,0x4c67d0),
                    "Combat Dodge": (0x4c6860,0x4c68e0),
                    "Stealth Slide": (0x4c6930,0x4c6a10),
                    "Alarm Clock": (0x4c6b20,0x4c6b80),
                    "Paraglide": (0x4c6c10,0x4c6c70),
                    "Silent Obliteration": (0x4c6d40,0x4c6d80),
                    "Thief Reflexes": (0x4c6e00,0x4c6e50),
                    "Feral Pounce": (0x4c6ec0,0x4c6f10),
                }
            ]
        }
    },
}

POWERUP_TEXT = {
    "Trigger Bomb": "Throwable bomb with remote detonation",
    "Size Destabilizer": "Shrink guards by whacking them with your crossbow",
    "Snooze Bomb": "Put enemies in the area to sleep",
    "Adrenaline Burst": "Run like a turtle has never run before",
    "Health Extractor": "Capture guards and extract medicine from them",
    "Hover Pack": "Extend your jumps by hovering in the air",
    "Reduction Bomb": "Shrink enemies in the area",
    "Temporal Lock": "Freeze time around the guards. temporarily, at least",

    "Fists of Flame": "Turn ordinary punches into fiery ones",
    "Turnbuckle Launch": "Jump to heroic heights",
    "Juggernaut Throw": "Thrown objects explode on impact",
    "Atlas Strength": "You can jump while carrying somebody",
    "Diablo Fire Slam": "Use while carrying an enemy to create a deadly firestorm",
    "Berserker Charge": "Scatter enemies with this powerful run",
    "Guttural Roar": "Terrify your foes",
    "Raging Inferno Flop": "Use while jumping to create a wall of flame on impact",

    "Smoke Bomb": "Obscure the vision of your enemies for a hasty getaway",
    "Combat Dodge": "Sidestep enemies in combat",
    "Stealth Slide": "Roll through the level. Silently!",
    "Alarm Clock": "Confuse your enemies with this distracting alarm clock",
    "Paraglide": "Fly through the air with this quick-deploy paraglider",
    "Silent Obliteration": "Finish off juggled enemies without attracting attention",
    "Thief Reflexes": "Slow time to a crawl",
    "Feral Pounce": "Jump over vast distances",
}

OTHER_POWERUPS = [
    "Mega Jump",
    "Tornado Strike",
    "Knockout Dive",
    "Insanity Strike",
    "Voltage Attack",
    "Long Toss",
    "Rage Bomb",
    "Music Box",
    "Lightning Spin",
    "Shadow Power",
    "TOM",
    "Time Rush"
]

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

# I could probably have calculated something like this, but it was easier to
# just write everything manually
PICKPOCKET_LOOT_TABLE_CHANCES = [
    (94,2,1,1,1,1),
    (90,6,1,1,1,1),
    (80,16,1,1,1,1),
    (74,22,1,1,1,1),
    (68,28,1,1,1,1),
    (60,36,1,1,1,1),
    (54,42,1,1,1,1),
    (48,48,1,1,1,1),
    (48,47,2,1,1,1),
    (47,47,2,2,1,1),
    (47,46,3,2,1,1),
    (46,46,3,3,1,1),
    (46,45,4,3,1,1),
    (45,45,4,4,1,1),
    (45,45,4,3,2,1),
    (45,45,3,3,2,2),
    (45,44,4,3,2,2),
    (44,44,4,4,2,2),
    (44,43,5,4,2,2),
    (43,43,5,5,2,2),
    (43,42,6,5,2,2),
    (42,42,6,6,2,2),
    (42,41,7,6,2,2),
    (41,41,7,7,2,2),
    (41,41,7,6,3,2),
    (41,41,6,6,3,3),
    (41,40,7,6,3,3),
    (40,40,7,7,3,3),
    (40,39,8,7,3,3),
    (39,39,8,8,3,3),
    (39,38,9,8,3,3),
    (38,38,9,9,3,3),
    (38,37,10,9,3,3),
    (37,37,10,10,3,3),
    (37,37,10,9,4,3),
    (37,37,9,9,4,4),
    (37,36,10,9,4,4),
    (36,36,10,10,4,4),
    (36,35,11,10,4,4),
    (35,35,11,11,4,4),
    (35,34,12,11,4,4),
    (34,34,12,12,4,4),
    (34,33,13,12,4,4),
    (33,33,13,13,4,4),
    (33,33,13,12,5,4),
    (33,33,12,12,5,5),
    (33,32,13,12,5,5),
    (32,32,13,13,5,5),
    (32,31,14,13,5,5),
    (31,31,14,14,5,5),
    (31,30,15,14,5,5),
    (30,30,15,15,5,5),
    (30,29,16,15,5,5),
    (29,29,16,16,5,5),
    (29,29,16,15,6,5),
    (29,29,15,15,6,6),
    (29,28,16,15,6,6),
    (28,28,16,16,6,6),
    (28,28,16,15,7,6),
    (28,28,15,15,7,7),
    (28,27,16,15,7,7),
    (27,27,16,16,7,7),
    (27,27,16,15,8,7),
    (27,27,15,15,8,8),
    (27,26,16,15,8,8),
    (26,26,16,16,8,8),
    (26,25,17,16,8,8),
    (25,25,17,17,8,8),
    (25,25,17,16,9,8),
    (25,25,16,16,9,9),
    (25,24,17,16,9,9),
    (24,24,17,17,9,9),
    (24,24,17,16,10,9),
    (24,24,16,16,10,10),
    (24,23,17,16,10,10),
    (23,23,17,17,10,10),
    (23,23,17,16,11,10),
    (23,23,16,16,11,11),
    (23,22,17,16,11,11),
    (22,22,17,17,11,11),
    (22,22,17,16,12,11),
    (22,22,16,16,12,12),
    (22,21,17,16,12,12),
    (21,21,17,17,12,12),
    (21,21,17,16,13,12),
    (21,21,16,16,13,13),
    (21,20,17,16,13,13),
    (20,20,17,17,13,13),
    (20,20,17,16,14,13),
    (20,20,16,16,14,14),
    (20,19,17,16,14,14),
    (19,19,17,17,14,14),
    (19,19,17,16,15,14),
    (19,19,16,16,15,15),
    (19,18,17,16,15,15),
    (18,18,17,17,15,15),
    (18,18,17,16,16,15),
    (18,18,16,16,16,16),
    (18,17,17,16,16,16),
    (17,17,17,17,16,16)
]

CAIRO_RETURN_DATA = (
    "4E A8 89 61 7A 56 E3 D1 1C 6C 04 FB 2D 05 A9 A1 B5 7C 6F 59 3A 10 EB FC F7 1B 3C 01 32 5E E4 77 3D 6B 28 BB B8 72 FE 3B 68 2A 84 67 79 9F 7E 0E F3 FF D7 A8 AE B9 8C 61 41 6C 04 FB DC 76 7B D1 89 01 00 00 FF FF FF FF 4E A8 89 61 7A 56 E3 D1 1C 6C 04 FB 2D 05 A9 A1 B5 7C 6F 59 3A 10 EB FC F7 1B 3C 01 32 5E E4 77 3D 6B 28 BB B8 72 FE 3B 68 2A 84 67 79 9F 7E 0E F3 FF D7 A8 AE B9 8C 61 41 6C 04 FB DC 76 7B D1"
).replace(" ","")
