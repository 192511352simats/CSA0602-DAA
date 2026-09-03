def optimal_bst(keys, freq):
    n = len(keys)

    # Create cost table
    cost = [[0 for _ in range(n)] for _ in range(n)]

    # Cost for a single key
    for i in range(n):
        cost[i][i] = freq[i]

    # Calculate cost for different lengths
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            cost[i][j] = float('inf')

            # Sum of frequencies
            total_freq = sum(freq[i:j + 1])

            # Try every key as root
            for r in range(i, j + 1):

                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                cost[i][j] = min(
                    cost[i][j],
                    left + right + total_freq
                )

    return cost[0][n - 1]


# Input
keys = [10, 20, 30]
freq = [34, 8, 50]

# Output
print("Optimal BST Cost:", optimal_bst(keys, freq))
