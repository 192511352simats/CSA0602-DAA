def detect_negative_cycle(vertices, edges):

    # Initialize all distances as 0
    # This allows detection of a negative cycle
    # anywhere in the graph
    distance = [0] * vertices

    # Relax all edges V-1 times
    for i in range(vertices - 1):

        for u, v, weight in edges:

            if distance[u] + weight < distance[v]:

                distance[v] = distance[u] + weight

    # Check one more time for a negative cycle
    for u, v, weight in edges:

        if distance[u] + weight < distance[v]:

            return True

    return False


# User Input
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(edges_count):

    u, v, weight = map(
        int,
        input(f"Edge {i + 1}: ").split()
    )

    edges.append((u, v, weight))


# Check for negative cycle
if detect_negative_cycle(vertices, edges):
    print("Negative Weight Cycle Exists")
else:
    print("No Negative Weight Cycle")
