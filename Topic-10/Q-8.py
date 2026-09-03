def tsp_dp(graph):

    n = len(graph)

    dp = [[float('inf')] * n for _ in range(1 << n)]

    dp[1][0] = 0

    for mask in range(1 << n):

        for u in range(n):

            if mask & (1 << u):

                for v in range(n):

                    if not mask & (1 << v):

                        dp[mask | (1 << v)][v] = min(
                            dp[mask | (1 << v)][v],
                            dp[mask][u] + graph[u][v]
                        )

    ans = float('inf')

    for i in range(1, n):

        ans = min(
            ans,
            dp[(1 << n) - 1][i] + graph[i][0]
        )

    return ans


n = int(input("Enter number of cities: "))

graph = []

print("Enter the distance matrix:")

for i in range(n):

    row = list(map(int, input(f"Enter distances for city {i}: ").split()))

    graph.append(row)


print("Minimum Cost =", tsp_dp(graph))
