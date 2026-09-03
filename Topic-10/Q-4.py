def knapsack(wt, val, W):
    n = len(wt)

    # Create DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(W + 1):

            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Input
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7

# Output
print("Maximum Profit =", knapsack(wt, val, W))
