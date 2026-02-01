from typing import NamedTuple, List

from .Constants import EPISODES, TREASURES, LOOT, ADDRESSES, EPISODES_DAYS_JOBS_TASKS

class Sly2LocationData(NamedTuple):
    name: str
    code: int
    category: str

jobs_list = [
    (f"{ep} - {job}",       "Job")
    for ep, chapters in EPISODES.items()
    for jobs in chapters for job in jobs
]

tasks_list = [
    (f"{ep} - Task #{task}", "Task")
    for i, (ep, chapters) in enumerate(EPISODES.items())
    #for jobs in ep for task in jobs
    #int(task) for task in str(ADDRESSES["SCUS-97316"]["tasks"][i])
    #for i, (ep) in enumerate(ADDRESSES["SCUS-97316"]["tasks"])
    #for job in ep for task_num in job
    for job in ADDRESSES["SCUS-97316"]["tasks"][i] for task in job
]

episodes_list = []
days_list = []
jobs_list_2 = []
tasks_list_2 = []
objectives_list = []
checkpoints_list = []
photos_list = []
story_stealing_list = []


def is_compound_job(job_contents):
    """True if job contains sub-jobs instead of tasks"""
    first_entry = job_contents[0]
    return isinstance(first_entry[1], tuple) and isinstance(first_entry[1][0], tuple)

def get_job_and_task_names(ep, job, tasks):
    """Appends Job names to the Jobs list & Task names to the Tasks list"""
    jobs_list_2.append((f"{ep} - {job}", "Job"))

    for task in tasks:
        tasks_list_2.append((f"{ep} - {job} - {task[1]}", "Task"))
        if task[5] != "":
            objectives_list.append((f"{ep} - {job} - {task[5]}", "Objective"))
        if task[2]:
            checkpoints_list.append((f"{ep} - {job} - {task[1]}", "Checkpoint"))
        if task[3]:
            photos_list.append((f"{ep} - {job} - {task[1]}", "Photo"))
        if task[4]:
            story_stealing_list.append((f"{ep} - {job} - {task[1]}", "Story Stealing"))


for episode_name, days in EPISODES_DAYS_JOBS_TASKS.items():
    episodes_list.append((episode_name, "Episode"))

    for day in days:
        days_list.append((f"{episode_name} - Day {day}", "Day"))

        for job_name, job_contents in day:
            # Compound job (sub-jobs)
            if is_compound_job(job_contents):
                for subjob_name, subjob_tasks in job_contents:
                    get_job_and_task_names(episode_name,subjob_name,job_contents)

            # Normal job
            else:
                get_job_and_task_names(episode_name,job_name,job_contents)


vaults_list = [
    (f"{ep} - Vault",        "Vault")
    for ep in EPISODES.keys()
]

treasures_list = [
    (f"{ep} - {treasure[0]}",  "Treasure")
    for ep, t in TREASURES.items()
    for treasure in t
]

bottles_list = [
    (f"{ep} - {i:02} bottles collected", "Bottle")
    for ep in EPISODES.keys()
    for i in range(1,31)
] + [
    (f"{ep} - Bottle #{i:02}", "Bottle")
    for ep in EPISODES.keys()
    for i in range(1,31)
]

purchases_list = [
    (f"ThiefNet {i+1:02}", "Purchase")
    for i in range(24)
]

pickpocket_list = [
    (f"Pickpocket {loot}", "Pickpocket")
    for loot in LOOT.keys()
]

location_list = jobs_list + tasks_list + vaults_list + treasures_list + bottles_list + purchases_list + pickpocket_list

base_code = 321_000

location_dict = {
    name: Sly2LocationData(name, base_code+code, category)
    for code, (name, category) in enumerate(location_list)
}

location_groups = {
    key: {location.name for location in location_dict.values() if location.category == key}
    for key in [
        "Job",
        "Task",
        "Bottle",
        "Vault",
        "Treasure",
        "Purchase",
        "Pickpocket"
    ]
}

def from_id(location_id: int) -> Sly2LocationData:
    matching = [location for location in location_dict.values() if location.code == location_id]
    if len(matching) == 0:
        raise ValueError(f"No location data for location id '{location_id}'")
    assert len(matching) < 2, f"Multiple locations data with id '{location_id}'. Please report."
    return matching[0]
