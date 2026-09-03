def job_sequencing(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    result = [None] * max_deadline
    total_profit = 0

    for name, deadline, profit in jobs:

        for slot in range(deadline - 1, -1, -1):

            if result[slot] is None:
                result[slot] = name
                total_profit += profit
                break

    return result, total_profit


n = int(input("Enter number of orders: "))

jobs = []

for i in range(n):
    name = input("Enter order name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))

    jobs.append((name, deadline, profit))


selected, total = job_sequencing(jobs)

print("Selected jobs =", *[x for x in selected if x is not None])
print("Maximum profit =", total)
