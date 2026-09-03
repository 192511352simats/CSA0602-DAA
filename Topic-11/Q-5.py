def network_delay_time(times, n, k):

    # Initialize distances
    distance = [float('inf')] * (n + 1)

    distance[k] = 0

    # Bellman-Ford relaxation
    for i in range(n - 1):

        for u, v, time in times:

            if distance[u] != float('inf'):

                if distance[u] + time < distance[v]:

                    distance[v] = distance[u] + time

    # Find maximum time
    maximum_time = max(distance[1:])

    # Check unreachable nodes
    if maximum_time == float('inf'):
        return -1

    return maximum_time


n = int(input("Enter number of nodes: "))
e = int(input("Enter number of connections: "))

times = []

print("Enter connections as: source destination time")

for i in range(e):

    u, v, time = map(
        int,
        input(f"Connection {i + 1}: ").split()
    )

    times.append([u, v, time])


k = int(input("Enter source node: "))

result = network_delay_time(times, n, k)

print("Network Delay Time =", result)
