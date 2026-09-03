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

answer = -1

for vertex in range(n):

    reachable_from_all = True

    for other in range(n):

        if other != vertex and not reach[other][vertex]:
            reachable_from_all = False
            break

    if reachable_from_all:
        answer = vertex
        break

if answer == -1:
    print("No such vertex exists")
else:
    print("Vertex reachable from every other vertex =", answer)
