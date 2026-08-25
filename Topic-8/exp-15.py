n = int(input("Enter n: "))
r = int(input("Enter r: "))

dp = [[0] * (r + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, min(i, r) + 1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print("C({}, {}) = {}".format(n, r, dp[n][r]))
