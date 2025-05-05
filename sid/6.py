n = int(input("Enter number of jobs: "))
jobs = []

print("Enter Id, deadline, and profit respectively for each job:")

for i in range(n):
    job = input(f"Job {i+1}: ").split()
    jobs.append([job[0], int(job[1]), int(job[2])])


jobs = sorted(jobs, key=lambda job: job[2], reverse=True)

scheduled = []
time_slots = [False] * n  
total_profit = 0

for job in jobs:
    for j in range(min(n, job[1]) - 1, -1, -1):  
        if not time_slots[j]:
            scheduled.append(job[0])
            time_slots[j] = True  
            total_profit += job[2]  
            break

print("Jobs are scheduled as: ", scheduled)
print("Total Profit: ", total_profit)
