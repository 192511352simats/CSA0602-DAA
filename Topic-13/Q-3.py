import heapq

def shortest_path(n, edges, source, destination):

    graph = [[] for _ in range(n)]

    for u, v, weight in edges:
        graph[u].append((v, weight))

    distance = [float('inf')] * n
    parent = [-1] * n

    distance[source] = 0

    pq = [(0, source)]

    while pq:

        current_distance, u = heapq.heappop(pq)

        if current_distance > distance[u]:
            continue

        for v, weight in graph[u]:

            new_distance = current_distance + weight

            if new_distance < distance[v]:

                distance[v] = new_distance
                parent[v] = u

                heapq.heappush(pq, (new_distance, v))

    if distance[destination] == float('inf'):
        print("No Path Exists")
        return

    path = []

    current = destination

    while current != -1:
        path.append(current)

        if current == source:
            break

        current = parent[current]

    path.reverse()

    print("Shortest distance from", source, "to", destination, "=",
          distance[destination])

    print("Path:", " → ".join(map(str, path)))


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(m):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))

source = int(input("Enter source vertex: "))
destination = int(input("Enter destination vertex: "))

shortest_path(n, edges, source, destination)
