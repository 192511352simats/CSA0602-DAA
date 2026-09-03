def is_safe(vertex, graph, path):

    if vertex in path:
        return False

    if len(path) == 0:
        return True

    return graph[path[-1]][vertex] == 1


def find_path(graph, path, n):

    if len(path) == n:
        return True

    for vertex in range(n):

        if is_safe(vertex, graph, path):

            path.append(vertex)

            if find_path(graph, path, n):
                return True

            path.pop()

    return False


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

print("Enter edges (u v):")

for i in range(e):

    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1


path = []

if find_path(graph, path, n):

    print("Hamiltonian Path:")
    print(" → ".join(map(str, path)))

else:
    print("No Hamiltonian Path Exists")
