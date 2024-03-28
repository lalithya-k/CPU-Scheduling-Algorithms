def priority_np(jobs):
    print("Job\tCompletion\tTurnaround\tWaiting")
    n = len(jobs)
    ct = [0] * n
    tat = [0] * n
    wt = [0] * n
    cur_time = 0

    jobs.sort(key=lambda x: (x['AT'], x['P'], x['ID']))

    while jobs:
        max_p = float('-inf')
        next_index = None

        for i, job in enumerate(jobs):
            if job['AT'] <= cur_time and job['P'] > max_p:
                max_p = job['P']
                next_index = i

        if next_index is None:
            cur_time += 1
            continue

        job = jobs.pop(next_index)
        cur_time += job['BT']
        ct[job['ID']] = cur_time
        tat[job['ID']] = cur_time - job['AT']
        wt[job['ID']] = tat[job['ID']] - job['BT']
        print(job['ID'], "\t\t", ct[job['ID']], "\t\t", tat[job['ID']], "\t\t", wt[job['ID']])

if __name__ == "__main__":
    jobs = [
        {'ID': 0, 'AT': 1, 'BT': 3, 'P': 3},
        {'ID': 1, 'AT': 1, 'BT': 2, 'P': 4},
        {'ID': 2, 'AT': 4, 'BT': 5, 'P': 5},
        {'ID': 3, 'AT': 5, 'BT': 3, 'P': 2},
        {'ID': 4, 'AT': 7, 'BT': 2, 'P': 6},
        {'ID': 5, 'AT': 7, 'BT': 4, 'P': 1}
    ]

    priority_np(jobs)
