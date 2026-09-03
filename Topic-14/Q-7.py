def is_safe(vertex, graph, colors, color):

    for i in range(len(graph)):

        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


def graph_coloring(graph, m, colors, vertex):

    if vertex == len(graph):
        return True

    for color in range(1, m + 1):

        if is_safe(vertex, graph, colors, color):

            colors[vertex] = color

            if graph_coloring(graph, m, colors, vertex + 1):
                return True

            colors[vertex] = 0

    return False


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of colors: "))

print("Enter adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


colors = [0] * n

if graph_coloring(graph, m, colors, 0):

    print("\nGraph Coloring:")

    for i in range(n):
        print(f"Vertex {i} → Color {colors[i]}")

else:
    print("Graph cannot be colored using", m, "colors")
