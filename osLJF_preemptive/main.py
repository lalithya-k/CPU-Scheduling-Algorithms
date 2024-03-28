class Job:
    pass

def ljf_preemptive():
    n = int(input("Enter the number of processes: "))
    jobs = []

    print("Enter arrival time for each process:")
    for i in range(n):
        job = Job()
        job.id = i + 1
        job.at = int(input())
        jobs.append(job)

    print("Enter CPU burst time for each process:")
    for job in jobs:
        job.bt = int(input())
        job.rt = job.bt

    jobs.sort(key=lambda x: x.at)

    complete = 0
    curr_time = 0
    max_rt = float('-inf')
    next_index = 0
    flag = False

    while complete != n:
        for j, job in enumerate(jobs):
            if job.at <= curr_time and job.rt > max_rt and job.rt > 0:
                max_rt = job.rt
                next_index = j
                flag = True

        if not flag:
            curr_time += 1
            continue

        jobs[next_index].rt -= 1
        max_rt = jobs[next_index].rt

        if max_rt == 0:
            max_rt = float('-inf')

        if jobs[next_index].rt == 0:
            complete += 1
            flag = False

            jobs[next_index].ct = curr_time + 1
            jobs[next_index].complete = True
            jobs[next_index].tat = (curr_time + 1) - jobs[next_index].at
            jobs[next_index].wt = jobs[next_index].tat - jobs[next_index].bt

            if jobs[next_index].wt < 0:
                jobs[next_index].wt = 0

        curr_time += 1

    jobs.sort(key=lambda x: x.id)

    print("Job\t\tAT\t\tBT\t\tCT\t\tTAT\t\tWT")
    for job in jobs:
        print(f"{job.id}\t\t{job.at}\t\t{job.bt}\t\t{job.ct}\t\t{job.tat}\t\t{job.wt}")

ljf_preemptive()

