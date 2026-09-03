def is_safe(vertex, graph, colors, color, n):

    for i in range(n):

        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


def color_graph(vertex, graph, colors, m, n):

    if vertex == n:
        return True

    for color in range(1, m + 1):

        if is_safe(vertex, graph, colors, color, n):

            colors[vertex] = color

            if color_graph(vertex + 1, graph, colors, m, n):
                return True

            colors[vertex] = 0

    return False


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

print("Enter edges (u v):")

for i in range(e):

    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1


for m in range(1, n + 1):

    colors = [0] * n

    if color_graph(0, graph, colors, m, n):

        print("Minimum Colors Required =", m)

        print("Color Assignment:")

        for i in range(n):
            print(f"Vertex {i} → Color {colors[i]}")

        break
