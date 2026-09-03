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

        dist, u = heapq.heappop(pq)

        if dist > distance[u]:
            continue

        for v, weight in graph[u]:

            new_distance = dist + weight

            if new_distance < distance[v]:

                distance[v] = new_distance
                parent[v] = u

                heapq.heappush(pq, (new_distance, v))

    return distance, parent


def build_path(parent, source, destination):

    path = []

    current = destination

    while current != -1:

        path.append(current)

        if current == source:
            path.reverse()
            return path

        current = parent[current]

    return []


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(m):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))

source = int(input("Enter source vertex: "))
destination = int(input("Enter vertex to check: "))

distance, parent = shortest_path(n, edges, source, destination)

if distance[destination] == float('inf'):
    print(f"Node {destination} is not reachable from node {source}")
else:
    path = build_path(parent, source, destination)

    print(f"Node {destination} is reachable")
    print("Shortest distance =", distance[destination])
    print("Path:", " → ".join(map(str, path)))
