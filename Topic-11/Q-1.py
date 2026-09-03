def bellman_ford(vertices, edges, source):

    # Initialize distances
    distance = [float('inf')] * vertices
    distance[source] = 0

    # Relax all edges V-1 times
    for i in range(vertices - 1):
        for u, v, weight in edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    # Check for negative weight cycle
    for u, v, weight in edges:
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Negative Weight Cycle Detected")
            return

    # Print shortest distances
    print("\nVertex\tDistance")

    for i in range(vertices):
        print(i, "\t", distance[i])


vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(edges_count):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))

source = int(input("Enter source vertex: "))

bellman_ford(vertices, edges, source)
