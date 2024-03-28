def calculate(jobs, n):
    tat, wt, ct = [0]*n, [0]*n, [0]*n
    ct[0] = jobs[0][1]
    tat[0] = ct[0] - jobs[0][0]

    for i in range(1, n):
        ct[i] = ct[i-1] + jobs[i][1]
        tat[i] = ct[i] - jobs[i][0]
        wt[i] = tat[i] - jobs[i][1]

    return tat, wt, ct

n = int(input("Enter number of jobs "))
jobs = []
for i in range(n):
    arrival_time = int(input("Enter arrival time for job "))
    burst_time = int(input("Enter burst time for job "))
    jobs.append((arrival_time, burst_time))

jobs.sort(key = lambda x: x[0])
tat, wt, ct = calculate(jobs, n)

print("Turn around time | Waiting time | Completion time")
for i in range(n):
    print("\t\t",tat[i],"\t\t\t",wt[i],"\t\t\t\t",ct[i])
