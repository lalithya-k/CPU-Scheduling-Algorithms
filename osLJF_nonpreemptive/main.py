def ljf_non_preemptive(jobs):
    jobs.sort(key=lambda x: (x['AT'], -x['BT'], x['Job']))

    cur_time = 0

    print("Job  Arrival  Burst  Completion  Turnaround  Waiting")
    while jobs:
        next_index = None
        max_burst = -float('inf')

        for i, job in enumerate(jobs):
            if job['AT'] <= cur_time and job['BT'] > max_burst:
                max_burst = job['BT']
                next_index = i

        if next_index is None:
            cur_time += 1
            continue

        job = jobs.pop(next_index)
        cur_time = max(cur_time, job['AT'])

        ct = cur_time + job['BT']
        tat = ct - job['AT']
        wt = max(0, tat - job['BT'])

        print(f"{job['Job']}\t\t{job['AT']}\t\t{job['BT']}\t\t"
              f"{ct}\t\t\t {tat}\t\t\t{wt}")

        cur_time = ct

jobs = [
    {'Job': 'J1', 'AT': 2, 'BT': 5},
    {'Job': 'J2', 'AT': 3, 'BT': 2},
    {'Job': 'J3', 'AT': 5, 'BT': 4},
    {'Job': 'J4', 'AT': 15, 'BT': 3},
    {'Job': 'J5', 'AT': 15, 'BT': 4},
    {'Job': 'J6', 'AT': 19, 'BT': 5}
]

ljf_non_preemptive(jobs)
