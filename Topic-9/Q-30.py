def wrap_lines(words, M):
    n = len(words)
    INF = float('inf')

    # dp[i] stores minimum cost from word i onwards
    dp = [INF] * (n + 1)

    # choice[i] stores the last word index of the current line
    choice = [-1] * n

    dp[n] = 0

    # Dynamic Programming
    for i in range(n - 1, -1, -1):
        line_length = 0

        for j in range(i, n):

            line_length += words[j]

            if j > i:
                line_length += 1

            if line_length > M:
                break

            # Last line has no penalty
            if j == n - 1:
                cost = 0
            else:
                extra = M - line_length
                cost = extra ** 2

            total_cost = cost + dp[j + 1]

            if total_cost < dp[i]:
                dp[i] = total_cost
                choice[i] = j

    # Reconstruct the lines
    lines = []
    i = 0

    while i < n:
        j = choice[i]
        lines.append(words[i:j + 1])
        i = j + 1

    return lines


# Test Case
words = [3, 2, 2, 5]
M = 6

lines = wrap_lines(words, M)

print("Reconstructed Lines:")

for i, line in enumerate(lines, 1):
    print("Line", i, ":", line)


# Verify every line fits
assert all(sum(line) + len(line) - 1 <= M for line in lines)

# Verify all words are included
assert sum(len(line) for line in lines) == 4

print("All test cases passed!")
