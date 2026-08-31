def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True


def hamiltonian(graph, path, pos):
    n = len(graph)

    if pos == n:
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, n):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            if hamiltonian(graph, path, pos + 1):
                return True

            path[pos] = -1

    return False


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

path = [-1] * n
path[0] = 0

if hamiltonian(graph, path, 1):
    print("Hamiltonian Cycle:")
    print(*[x + 1 for x in path], path[0] + 1)
else:
    print("No Hamiltonian Cycle exists")
