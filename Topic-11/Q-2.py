def floyd_warshall(graph, n):

    # Convert -1 to infinity
    dist = []

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

                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):

                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix.")
print("Use -1 for INF (no connection).")

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    graph.append(row)


result = floyd_warshall(graph, n)

print("\nShortest Distance Matrix:")

for row in result:
    for value in row:

        if value == float('inf'):
            print("INF", end="\t")
        else:
            print(value, end="\t")

    print()
