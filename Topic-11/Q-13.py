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

reach = warshall(graph, n)

max_count = -1
answer = 0

for i in range(n):

    count = 0

    for j in range(n):

        if i != j and reach[i][j]:
            count += 1

    if count > max_count:
        max_count = count
        answer = i

print("Vertex with Maximum Reachability =", answer)
print("Number of reachable vertices =", max_count)
