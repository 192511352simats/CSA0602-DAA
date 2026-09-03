def job_sequencing(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [False] * max_deadline
    result = [None] * max_deadline

    profit = 0

    for name, deadline, value in jobs:

        for j in range(deadline - 1, -1, -1):

            if not slots[j]:
                slots[j] = True
                result[j] = name
                profit += value
                break

    return result, profit


n = int(input("Enter number of papers/jobs: "))

jobs = []

for i in range(n):
    name = input("Enter job name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter reward: "))

    jobs.append((name, deadline, profit))


selected, total = job_sequencing(jobs)

print("Selected jobs =", *[x for x in selected if x])
print("Maximum profit =", total)
