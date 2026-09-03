def min_wrap_cost(words, M):
    n = len(words)
    INF = float('inf')

    dp = [INF] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        length = 0

        for j in range(i, n):
            length += words[j]

            if j > i:
                length += 1

            if length > M:
                break

            if j == n - 1:
                cost = 0
            else:
                cost = (M - length) ** 2

            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


def wrap_lines(words, M):
    n = len(words)
    INF = float('inf')

    dp = [INF] * (n + 1)
    choice = [-1] * n
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        length = 0

        for j in range(i, n):
            length += words[j]

            if j > i:
                length += 1

            if length > M:
                break

            cost = 0 if j == n - 1 else (M - length) ** 2

            if cost + dp[j + 1] < dp[i]:
                dp[i] = cost + dp[j + 1]
                choice[i] = j

    lines = []
    i = 0

    while i < n:
        j = choice[i]
        lines.append(words[i:j + 1])
        i = j + 1

    return lines


words = [3, 2, 2, 5]
M = 6

cost = min_wrap_cost(words, M)
lines = wrap_lines(words, M)

print("Panel Width:", M)
print("Optimal Reflow Cost:", cost)

for i, line in enumerate(lines, 1):
    print("Line", i, ":", line)

assert cost == 19
assert all(sum(line) + len(line) - 1 <= M for line in lines)

print("All test cases passed!")
