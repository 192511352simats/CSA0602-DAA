def is_safe(vertex, graph, colors, color, n):

    for i in range(n):

        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


def solve(vertex, graph, colors, m, n):

    if vertex == n:
        return True

    for color in range(1, m + 1):

        if is_safe(vertex, graph, colors, color, n):

            colors[vertex] = color

            if solve(vertex + 1, graph, colors, m, n):
                return True

            colors[vertex] = 0

    return False


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of colors: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

print("Enter edges (u v):")

for i in range(e):

    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1


colors = [0] * n

if solve(0, graph, colors, m, n):
    print(f"Graph can be colored using {m} colors.")
else:
    print(f"Graph cannot be colored using {m} colors.")
