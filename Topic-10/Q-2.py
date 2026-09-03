from functools import lru_cache

def tsp(graph):
    n = len(graph)

    @lru_cache(None)
    def visit(mask, pos):

        # All cities visited
        if mask == (1 << n) - 1:
            return graph[pos][0]

        ans = float('inf')

        # Visit unvisited cities
        for city in range(n):
            if mask & (1 << city) == 0:
                ans = min(
                    ans,
                    graph[pos][city] +
                    visit(mask | (1 << city), city)
                )

        return ans

    # Start from city 0
    return visit(1, 0)


# Graph representing distances between cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Output
print("Minimum Cost:", tsp(graph))
