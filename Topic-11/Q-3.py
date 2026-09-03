def warshall(graph, n):

    # Create a copy of the graph
    reach = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(graph[i][j])

        reach.append(row)

    # Warshall's Algorithm
    for k in range(n):

        for i in range(n):

            for j in range(n):

                reach[i][j] = reach[i][j] or (
                    reach[i][k] and reach[k][j]
                )

    return reach


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix using 0 and 1:")

for i in range(n):

    row = list(map(int, input(f"Enter row {i + 1}: ").split()))

    graph.append(row)


result = warshall(graph, n)

print("\nTransitive Closure Matrix:")

for row in result:

    for value in row:
        print(int(value), end=" ")

    print()
