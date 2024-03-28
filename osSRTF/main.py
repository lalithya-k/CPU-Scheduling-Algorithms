def sjf_preemptive(jobs):
    jobs.sort(key=lambda x: (x['AT'], x['BT'], x['Job']))

    cur_time = 0

    print("Job  Arrival  Burst  Completion  Turnaround  Waiting")
    while jobs:
        next_index = None
        min_burst = float('inf')

        for i, job in enumerate(jobs):
            if job['AT'] <= cur_time and job['RT'] < min_burst:
                min_burst = job['RT']
                next_index = i

        if next_index is None:
            cur_time += 1
            continue

        job = jobs[next_index]

        if job['RT'] == 0:
            jobs.pop(next_index)
            continue

        job['RT'] -= 1
        cur_time += 1

        if job['RT'] == 0:
            ct = cur_time
            tat = ct - job['AT']
            wt = tat - job['BT']
            print(f"{job['Job']}\t\t{job['AT']}\t\t{job['BT']}\t\t"
                  f"{ct}\t\t\t {tat}\t\t\t{wt}")

jobs = [
    {'Job': 'J1', 'AT': 2, 'BT': 4, 'RT': 4},
    {'Job': 'J2', 'AT': 3, 'BT': 1, 'RT': 1},
    {'Job': 'J3', 'AT': 3, 'BT': 3, 'RT': 3},
    {'Job': 'J4', 'AT': 5, 'BT': 2, 'RT': 2},
    {'Job': 'J5', 'AT': 14, 'BT': 2, 'RT': 2},
    {'Job': 'J6', 'AT': 14, 'BT': 1, 'RT': 1}
]

sjf_preemptive(jobs)
