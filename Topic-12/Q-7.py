def job_sequencing(jobs):

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [False] * max_deadline
    selected = [None] * max_deadline

    total_profit = 0

    for job_id, deadline, profit in jobs:

        for j in range(min(max_deadline, deadline) - 1, -1, -1):

            if not slots[j]:
                slots[j] = True
                selected[j] = job_id
                total_profit += profit
                break

    return selected, total_profit


n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    job_id = input(f"Enter job name {i + 1}: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))

    jobs.append((job_id, deadline, profit))


selected, maximum_profit = job_sequencing(jobs)

print("Selected jobs =", *[x for x in selected if x is not None])
print("Maximum profit =", maximum_profit)
