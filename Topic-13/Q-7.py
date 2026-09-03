import heapq

def prim(n, edges, start):

    graph = [[] for _ in range(n)]

    # Undirected graph
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    visited = [False] * n

    pq = [(0, start, -1)]

    mst = []
    total_weight = 0

    while pq:

        weight, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight

        for edge_weight, v in graph[u]:

            if not visited[v]:
                heapq.heappush(
                    pq,
                    (edge_weight, v, u)
                )

    return mst, total_weight


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(m):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))

start = int(input("Enter starting vertex: "))

mst, total = prim(n, edges, start)

print("MST edges:")

for edge in mst:
    print(edge)

print("Total weight:", total)
