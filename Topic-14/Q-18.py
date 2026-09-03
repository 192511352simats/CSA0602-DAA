def greedy_coloring(vertices, edges):

    graph = [[] for _ in range(vertices)]

    # Create adjacency list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [-1] * vertices

    # First vertex gets first color
    colors[0] = 1

    for vertex in range(1, vertices):

        used_colors = set()

        # Find colors used by adjacent vertices
        for neighbor in graph[vertex]:
            if colors[neighbor] != -1:
                used_colors.add(colors[neighbor])

        # Find smallest available color
        color = 1

        while color in used_colors:
            color += 1

        colors[vertex] = color

    return colors


# User Input
vertices = int(input("Enter number of vertices: "))

edges_count = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v):")

for i in range(edges_count):
    u, v = map(int, input().split())
    edges.append((u, v))


colors = greedy_coloring(vertices, edges)

print("\nGraph Coloring:")

for i in range(vertices):
    print(f"Vertex {i} → Color {colors[i]}")

print("\nTotal Colors Used =", max(colors))
