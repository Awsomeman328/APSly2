from typing import NamedTuple

from .data import episodes, treasures

class Sly2LocationData(NamedTuple):
    name: str
    code: int
    category: str

jobs_list = [
    (f"{ep} - {job}",       "job")
    for ep, chapters in episodes.items()
    for jobs in chapters for job in jobs
]

safes_list = [
    (f"{ep} - Safe",        "Safe")
    for ep in episodes.keys()
]

treasures_list = [
    (f"{ep} - {treasure[0]}",  "Treasure")
    for ep, t in treasures.items()
    for treasure in t
]

bottles_list = [
    (f"{ep} - {i+1} bottles collected")
    for i in range(30)
    for ep in episodes.keys()
]

location_list = jobs_list + safes_list + treasures_list

base_code = 321_000

location_dict = {
    name: Sly2LocationData(name, base_code+code, category)
    for code, (name, category) in enumerate(location_list)
}

location_groups = {
    key: {location.name for location in location_dict.values() if location.category == key}
    for key in [
        "Job",
        "Bottles",
        "Safes",
        "Treasures",
    ]
}