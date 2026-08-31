def is_safe(v, graph, color, c, n):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring(graph, m, color, v, n):
    if v == n:
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c, n):
            color[v] = c

            if graph_coloring(graph, m, color, v + 1, n):
                return True

            color[v] = 0

    return False


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n

if graph_coloring(graph, m, color, 0, n):
    print("Color assigned to each vertex:")
    for i in range(n):
        print("Vertex", i + 1, "-> Color", color[i])
else:
    print("Coloring is not possible")
