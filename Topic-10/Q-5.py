def knapsack(W, wt, val, n, memo):
    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1:
        return memo[n][W]

    if wt[n - 1] <= W:
        memo[n][W] = max(
            val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1, memo),
            knapsack(W, wt, val, n - 1, memo)
        )
    else:
        memo[n][W] = knapsack(W, wt, val, n - 1, memo)

    return memo[n][W]


n = int(input("Enter number of items: "))

wt = []
val = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))
    wt.append(weight)
    val.append(value)

W = int(input("Enter maximum capacity of knapsack: "))

memo = [[-1] * (W + 1) for _ in range(n + 1)]

print("Maximum Profit =", knapsack(W, wt, val, n, memo))
