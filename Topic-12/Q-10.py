def job_sequencing(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    schedule = [None] * max_deadline
    maximum_profit = 0

    for name, deadline, profit in jobs:

        for day in range(deadline - 1, -1, -1):

            if schedule[day] is None:
                schedule[day] = name
                maximum_profit += profit
                break

    return schedule, maximum_profit


n = int(input("Enter number of projects: "))

jobs = []

for i in range(n):
    name = input("Enter project name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter income: "))

    jobs.append((name, deadline, profit))


selected, total = job_sequencing(jobs)

print("Selected projects =", *[x for x in selected if x is not None])
print("Maximum income =", total)
