def min_wrap_cost(words, M):
    n = len(words)
    INF = float('inf')

    # dp[i] stores the minimum cost for arranging words from i onwards
    dp = [INF] * (n + 1)
    dp[n] = 0

    # Fill DP table from right to left
    for i in range(n - 1, -1, -1):
        line_length = 0

        for j in range(i, n):

            # Add current word
            line_length += words[j]

            # Add one space between words
            if j > i:
                line_length += 1

            # Stop if words do not fit
            if line_length > M:
                break

            # Last line has no penalty
            if j == n - 1:
                cost = 0
            else:
                extra_spaces = M - line_length
                cost = extra_spaces ** 2

            # Find minimum cost
            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


# Test Cases
print("Test Case 1:")
words = [3, 2, 2, 5]
M = 6

result = min_wrap_cost(words, M)

print("Word lengths:", words)
print("Maximum line width:", M)
print("Minimum wrap cost:", result)

assert result == 19


print("\nTest Case 2:")
words = [3]
M = 6

result = min_wrap_cost(words, M)

print("Word lengths:", words)
print("Maximum line width:", M)
print("Minimum wrap cost:", result)

assert result == 0


print("\nAll test cases passed!")
