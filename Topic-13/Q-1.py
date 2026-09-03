import heapq

def dijkstra(n, edges, source):
    graph = [[] for _ in range(n)]

    for u, v, weight in edges:
        graph[u].append((v, weight))

    distance = [float('inf')] * n
    parent = [-1] * n

    distance[source] = 0

    pq = [(0, source)]

    while pq:
        dist, u = heapq.heappop(pq)

        if dist > distance[u]:
            continue

        for v, weight in graph[u]:
            new_distance = distance[u] + weight

            if new_distance < distance[v]:
                distance[v] = new_distance
                parent[v] = u
                heapq.heappush(pq, (new_distance, v))

    return distance, parent


def get_path(parent, source, destination):
    path = []

    current = destination

    while current != -1:
        path.append(current)

        if current == source:
            break

        current = parent[current]

    path.reverse()

    return path


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(m):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))

source = int(input("Enter source vertex: "))

distance, parent = dijkstra(n, edges, source)

print("\nDistances from", source, ":", distance)

for i in range(n):
    if i != source and distance[i] != float('inf'):
        path = get_path(parent, source, i)
        print(f"Path to {i}:", " → ".join(map(str, path)))
