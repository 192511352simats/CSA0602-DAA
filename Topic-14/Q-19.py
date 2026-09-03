def approximate_vertex_cover(edges):

    remaining_edges = edges.copy()

    vertex_cover = set()

    while remaining_edges:

        # Select first uncovered edge
        u, v = remaining_edges[0]

        # Add both vertices
        vertex_cover.add(u)
        vertex_cover.add(v)

        # Remove all edges covered by u or v
        new_edges = []

        for edge in remaining_edges:

            a, b = edge

            if a != u and b != u and a != v and b != v:
                new_edges.append(edge)

        remaining_edges = new_edges

    return vertex_cover


# User Input
vertices = int(input("Enter number of vertices: "))

n = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v):")

for i in range(n):
    u, v = map(int, input().split())
    edges.append((u, v))


cover = approximate_vertex_cover(edges)

print("\nApproximate Vertex Cover:")

print("{", ", ".join(map(str, sorted(cover))), "}")

print("Cover Size =", len(cover))
