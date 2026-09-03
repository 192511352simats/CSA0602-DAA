def min_wrap_cost(words, M):
    n = len(words)
    INF = float('inf')

    dp = [INF] * (n + 1)
    choice = [-1] * n
    dp[n] = 0

    # Dynamic Programming
    for i in range(n - 1, -1, -1):
        line_length = 0

        for j in range(i, n):
            line_length += words[j]

            # Add spaces between words
            if j > i:
                line_length += 1

            # If line exceeds maximum width
            if line_length > M:
                break

            # No penalty for the last line
            if j == n - 1:
                cost = 0
            else:
                extra_spaces = M - line_length
                cost = extra_spaces ** 2

            total_cost = cost + dp[j + 1]

            if total_cost < dp[i]:
                dp[i] = total_cost
                choice[i] = j

    return dp[0], choice


def wrap_lines(words, M):
    n = len(words)

    cost, choice = min_wrap_cost(words, M)

    lines = []
    i = 0

    # Reconstruct the optimal lines
    while i < n:
        j = choice[i]
        lines.append(words[i:j + 1])
        i = j + 1

    return lines


# Test Case
words = [3, 2, 2, 5]
M = 6

cost, choice = min_wrap_cost(words, M)
lines = wrap_lines(words, M)

print("Word Lengths:", words)
print("Maximum Width:", M)
print("Minimum Wrap Cost:", cost)

print("\nOptimal Line Arrangement:")
for i, line in enumerate(lines, 1):
    print("Line", i, ":", line)


# Test cases
assert cost == 19
assert sum(len(line) for line in lines) == 4

print("\nAll test cases passed!")
