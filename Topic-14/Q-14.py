from itertools import combinations


def is_vertex_cover(vertices, edges):

    vertex_set = set(vertices)

    for u, v in edges:

        if u not in vertex_set and v not in vertex_set:
            return False

    return True


def exact_vertex_cover(n, edges):

    for size in range(n + 1):

        for combination in combinations(range(n), size):

            if is_vertex_cover(combination, edges):
                return set(combination)


def approximate_vertex_cover(n, edges):

    remaining_edges = edges[:]
    cover = set()

    while remaining_edges:

        degree = [0] * n

        for u, v in remaining_edges:
            degree[u] += 1
            degree[v] += 1

        vertex = max(range(n), key=lambda x: degree[x])

        cover.add(vertex)

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


exact_cover = exact_vertex_cover(n, edges)

approx_cover = approximate_vertex_cover(n, edges)

ratio = len(approx_cover) / len(exact_cover)


print("\nExact Vertex Cover:")
print("{", ", ".join(map(str, sorted(exact_cover))), "}")

print("Exact Vertex Cover Size =", len(exact_cover))


print("\nApproximate Vertex Cover:")
print("{", ", ".join(map(str, sorted(approx_cover))), "}")

print("Approximate Vertex Cover Size =", len(approx_cover))


print("\nApproximation Ratio =", round(ratio, 2))
