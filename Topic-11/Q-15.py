def warshall(graph, n):
    reach = [row[:] for row in graph]

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

reach = warshall(graph, n)

strongly_connected = True

for i in range(n):
    for j in range(n):

        # Ignore the same vertex
        if i != j and not reach[i][j]:
            strongly_connected = False
            break

    if not strongly_connected:
        break


if strongly_connected:
    print("Strongly Connected")
else:
    print("Not Strongly Connected")
