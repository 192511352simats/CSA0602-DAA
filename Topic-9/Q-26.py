def wrap_lines(words, M):
    n = len(words)
    INF = float('inf')

    dp = [INF] * (n + 1)
    choice = [-1] * n
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        line_length = 0

        for j in range(i, n):
            line_length += words[j]

            if j > i:
                line_length += 1

            if line_length > M:
                break

            extra = M - line_length

            if j == n - 1:
                cost = 0
            else:
                cost = extra ** 2

            if cost + dp[j + 1] < dp[i]:
                dp[i] = cost + dp[j + 1]
                choice[i] = j

    lines = []
    i = 0

    while i < n:
        j = choice[i]
        lines.append(words[i:j + 1])
        i = j + 1

    return dp[0], lines


words = [3, 2, 2, 5]
terminal_width = 6

cost, lines = wrap_lines(words, terminal_width)

print("Terminal Width:", terminal_width)
print("Minimum Cost:", cost)

for i, line in enumerate(lines, 1):
    print("Line", i, ":", line)

assert cost == 19
assert all(sum(line) + len(line) - 1 <= terminal_width for line in lines)

print("All test cases passed!")
