def matrix_chain(arr):

    n = len(arr)

    dp = [[0] * n for _ in range(n)]

    for L in range(2, n):

        for i in range(1, n - L + 1):

            j = i + L - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                q = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + arr[i - 1] * arr[k] * arr[j]
                )

                dp[i][j] = min(dp[i][j], q)

    return dp[1][n - 1]


n = int(input("Enter number of dimensions: "))

arr = []

for i in range(n):
    value = int(input(f"Enter dimension {i + 1}: "))
    arr.append(value)

print("Minimum Multiplications =", matrix_chain(arr))
