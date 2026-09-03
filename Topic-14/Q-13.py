def approximate_vertex_cover(n, edges):

    remaining_edges = edges[:]
    cover = set()

    while remaining_edges:

        # Count degree of every vertex
        degree = [0] * n

        for u, v in remaining_edges:
            degree[u] += 1
            degree[v] += 1

        # Select vertex with maximum degree
        vertex = max(range(n), key=lambda x: degree[x])

        cover.add(vertex)

        # Remove all edges connected to selected vertex
        remaining_edges = [
            (u, v)
            for u, v in remaining_edges
            if u != vertex and v != vertex
        ]

    return cover


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v):")

for i in range(e):

    u, v = map(int, input().split())

    edges.append((u, v))


cover = approximate_vertex_cover(n, edges)

print("\nApproximate Vertex Cover:")
print("{", ", ".join(map(str, sorted(cover))), "}")

print("Cover Size =", len(cover))
