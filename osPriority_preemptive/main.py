class Job:
    def __init__(self, id, at, bt, priority):
        self.id = id
        self.at = at
        self.bt = bt
        self.priority = priority
        self.rt = bt
        self.wt = 0
        self.tat = 0
        self.ct = 0


def preemptive_p(jobs):
    cur_time = 0
    finished = 0
    while finished < len(jobs):
        next_index = None
        max_p = float('inf')
        for job in jobs:
            if job.at <= cur_time and job.rt > 0 and job.priority < max_p:
                max_p = job.priority
                next_index = job
        if next_index is not None:
            next_index.rt -= 1
            cur_time += 1
            if next_index.rt == 0:
                next_index.tat = cur_time - next_index.at
                next_index.wt = next_index.tat - next_index.bt
                next_index.ct = cur_time
                finished += 1
        else:
            cur_time += 1


def printing(jobs):
    in_order = sorted(jobs, key=lambda x: x.id)

    print("\nJob\t\tAT\t\tBT\tPriority\tCT\t\tTAT\t\tWT")
    for job in in_order:
        print(
            f"{job.id}\t\t{job.at}\t\t{job.bt}\t\t{job.priority}\t\t{job.ct}\t\t{job.tat}\t\t{job.wt}")


def main():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        print("Enter details for Job", i + 1)
        process_id = i + 1
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        priority = int(input("Priority: "))
        jobs.append(Job(process_id, at, bt, priority))
    preemptive_p(jobs)
    printing(jobs)


if __name__ == "__main__":
    main()

