def graph_diameter(graph, n):

    dist = []

    # Convert -1 to infinity
    for i in range(n):
        row = []

        for j in range(n):
            if graph[i][j] == -1:
                row.append(float('inf'))
            else:
                row.append(graph[i][j])

        dist.append(row)

    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):

                if dist[i][k] != float('inf') and \
                   dist[k][j] != float('inf'):

                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    diameter = 0

    for i in range(n):
        for j in range(n):

            if dist[i][j] != float('inf'):
                diameter = max(diameter, dist[i][j])

    return diameter


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix.")
print("Use -1 for INF (no connection):")

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    graph.append(row)

print("Diameter of Graph =", graph_diameter(graph, n))
