def cheapest_flight(n, flights, src, dst, k):

    # Initialize distances
    dist = [float('inf')] * n
    dist[src] = 0

    # At most K stops means at most K + 1 edges
    for i in range(k + 1):

        # Copy previous distances
        temp = dist.copy()

        for u, v, cost in flights:

            if dist[u] != float('inf'):

                temp[v] = min(
                    temp[v],
                    dist[u] + cost
                )

        dist = temp

    if dist[dst] == float('inf'):
        return -1

    return dist[dst]


# User Input
n = int(input("Enter number of cities: "))
m = int(input("Enter number of flights: "))

flights = []

print("Enter flights as: source destination cost")

for i in range(m):
    u, v, cost = map(
        int,
        input(f"Flight {i + 1}: ").split()
    )

    flights.append([u, v, cost])


src = int(input("Enter source city: "))
dst = int(input("Enter destination city: "))
k = int(input("Enter maximum number of stops: "))


result = cheapest_flight(n, flights, src, dst, k)

print("Cheapest Flight Cost =", result)
