def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, rank, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    return True


def boruvka(n, edges):

    parent = list(range(n))
    rank = [0] * n

    components = n
    mst = []
    total_weight = 0

    phase = 1

    while components > 1:

        cheapest = [-1] * n

        # Find cheapest edge for each component
        for i, (u, v, weight) in enumerate(edges):

            set_u = find(parent, u)
            set_v = find(parent, v)

            if set_u == set_v:
                continue

            if cheapest[set_u] == -1 or \
               edges[cheapest[set_u]][2] > weight:

                cheapest[set_u] = i

            if cheapest[set_v] == -1 or \
               edges[cheapest[set_v]][2] > weight:

                cheapest[set_v] = i

        print(f"\nPhase {phase}:")

        added = 0

        for i in range(n):

            if cheapest[i] != -1:

                u, v, weight = edges[cheapest[i]]

                if union(parent, rank, u, v):

                    print("Added edge:", (u, v, weight))

                    mst.append((u, v, weight))
                    total_weight += weight

                    components -= 1
                    added += 1

        if added == 0:
            break

        phase += 1

    return mst, total_weight


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: source destination weight")

for i in range(m):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v, weight))


mst, total = boruvka(n, edges)

print("\nMST edges:", mst)
print("Total weight:", total)
