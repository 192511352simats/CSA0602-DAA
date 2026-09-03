def warshall(graph, n):
    reach = [row[:] for row in graph]

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

u = int(input("Enter source vertex (u): "))
v = int(input("Enter destination vertex (v): "))

reach = warshall(graph, n)

if reach[u][v]:
    print("Path Exists")
else:
    print("Path Does Not Exist")
