def optimal_bst(freq):

    n = len(freq)

    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):

        for i in range(n - L + 1):

            j = i + L - 1

            cost[i][j] = float('inf')

            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):

                left = cost[i][r - 1] if r > i else 0

                right = cost[r + 1][j] if r < j else 0

                cost[i][j] = min(
                    cost[i][j],
                    left + right + total
                )

    return cost[0][n - 1]


n = int(input("Enter number of keys: "))

freq = []

for i in range(n):
    f = int(input(f"Enter frequency of key {i + 1}: "))
    freq.append(f)

print("Optimal Cost =", optimal_bst(freq))
