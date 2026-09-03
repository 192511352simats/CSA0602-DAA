from functools import lru_cache

n = int(input("Enter number of cities: "))

graph = []

print("Enter the distance matrix:")

for i in range(n):
    row = list(map(int, input(f"Enter distances for city {i}: ").split()))
    graph.append(row)


@lru_cache(None)
def tsp(mask, pos):

    if mask == (1 << n) - 1:
        return graph[pos][0]

    ans = float('inf')

    for city in range(n):

        if not mask & (1 << city):

            ans = min(
                ans,
                graph[pos][city] +
                tsp(mask | (1 << city), city)
            )

    return ans


print("Minimum Cost =", tsp(1, 0))
