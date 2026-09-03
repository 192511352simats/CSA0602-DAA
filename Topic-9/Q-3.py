def symmetry_ratio(s):
    n = len(s)

    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1] / n
assert round(symmetry_ratio("bbbab"), 2) == 0.8
assert round(symmetry_ratio("cbbd"), 2) == 0.5
message = input("Enter message: ")
ratio = symmetry_ratio(message)
print("Symmetry ratio:", round(ratio, 2))
if ratio > 0.7:
    print("Message flagged as highly symmetric")
else:
    print("Message is normal")
