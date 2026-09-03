def min_cost(cost):
    m = len(cost)
    n = len(cost[0])

    dp = [[0] * n for _ in range(m)]

    # Starting position
    dp[0][0] = cost[0][0]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    # Calculate minimum cost path
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost[i][j] + min(
                dp[i - 1][j],
                dp[i][j - 1]
            )

    return dp[m - 1][n - 1]


# User input
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

cost = []

print("Enter the cost matrix values:")

for i in range(m):
    row = []
    for j in range(n):
        value = int(input(f"Enter value at position [{i}][{j}]: "))
        row.append(value)
    cost.append(row)


# Display result
print("Minimum Cost =", min_cost(cost))
