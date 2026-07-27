def bubble_sort_queue(q):
    p = {"ambulance": 3, "bus": 2, "car": 1}

    for i in range(len(q)-1):
        for j in range(len(q)-1-i):
            if p[q[j]] < p[q[j+1]]:
                q[j], q[j+1] = q[j+1], q[j]
    return q

n = int(input("Enter number of vehicles: "))
queue = []

for i in range(n):
    queue.append(input("Enter vehicle: ").lower())

print("Priority Queue:", bubble_sort_queue(queue))
