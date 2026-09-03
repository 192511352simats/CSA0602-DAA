def find_city(n, edges, threshold):

    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]

    # Distance from a city to itself
    for i in range(n):
        dist[i][i] = 0

    # Add edges
    for u, v, weight in edges:
        dist[u][v] = weight
        dist[v][u] = weight

    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):

                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    minimum_count = float('inf')
    city = -1

    # Count reachable cities
    for i in range(n):

        count = 0

        for j in range(n):

            if i != j and dist[i][j] <= threshold:
                count += 1

        # >= ensures the larger city number is selected in case of a tie
        if count <= minimum_count:
            minimum_count = count
            city = i

    return city


n = int(input("Enter number of cities: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: city1 city2 distance")

for i in range(e):

    u, v, weight = map(
        int,
        input(f"Edge {i + 1}: ").split()
    )

    edges.append([u, v, weight])


threshold = int(input("Enter distance threshold: "))

result = find_city(n, edges, threshold)

print("City with smallest reachable cities =", result)
