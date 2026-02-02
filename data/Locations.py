from typing import NamedTuple, List

from .Constants import EPISODES, TREASURES, LOOT, ADDRESSES, TASK_FIELD, EPISODES_DAYS_JOBS_TASKS

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

def get_job_and_task_names(ep, job, sub_job, tasks):
    """Appends Job names to the Jobs list & Task names to the Tasks list
    TODO: Delete all of the print() calls in this file and refactor this def's comment"""
    for task in tasks:
        if job != sub_job:
            job = sub_job
        if job == "Overworld":
            job = ep
        tasks_list_2.append((f"{job} - {task[1]}", "Task"))
        #print(tasks_list_2[-1])
        if task[5] != "":
            objectives_list.append((f"{job} - {task[5]}", "Objective"))
            #print(objectives_list[-1])
        if task[2]:
            checkpoints_list.append((f"{job} - {task[1]} (Checkpoint)", "Checkpoint"))
            #print(checkpoints_list[-1])
        if task[3]:
            photos_list.append((f"{job} - {task[1]} (Photo)", "Photo"))
            #print(photos_list[-1])
        if task[4]:
            story_stealing_list.append((f"{job} - {task[1]} (Stealing)", "Story Stealing"))
            #print(story_stealing_list[-1])

    num_cp_jobs = 0
    for episode_name, days in EPISODES_DAYS_JOBS_TASKS.items():
        episodes_list.append((episode_name, "Episode"))
        #print(episodes_list[-1])

        # TODO: Account for different number of Days in Eps 4 & 8 depending on user's settings.
        #  (May need to do this elsewhere)
        num_days = 0
        for day in days:
            num_days += 1
            days_list.append((f"{episode_name} - All Day {num_days} Jobs", "Day"))
            #print(days_list[-1])

            # TODO: Account for Compound-Jobs being treated as either 1 Job or multiple
            #  depending on user's settings. (May need to do this elsewhere)
            for job_name, job_contents in day:
                # Compound job (sub-jobs)
                if is_compound_job(job_contents):
                    num_cp_jobs += 1
                    #print(f"COMPOUND JOB #{num_cp_jobs}!")
                    for subjob_name, subjob in job_contents:
                        if job_name != "Overworld":
                            jobs_list_2.append((f"{episode_name} - {job_name}", "Job"))
                            #print(jobs_list_2[-1])
                        get_job_and_task_names(episode_name, job_name, subjob_name, subjob)

                # Normal job
                else:
                    if job_name != "Overworld":
                        jobs_list_2.append((f"{episode_name} - {job_name}", "Job"))
                        #print(jobs_list_2[-1])
                    get_job_and_task_names(episode_name, job_name, job_name, job_contents)


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
