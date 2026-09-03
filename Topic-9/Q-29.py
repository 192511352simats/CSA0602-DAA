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

            cost = 0 if j == n - 1 else (M - length) ** 2

            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


def greedy_wrap_cost(words, M):
    n = len(words)
    i = 0
    total_cost = 0

    while i < n:
        line_length = 0
        start = i

        while i < n:
            new_length = line_length + words[i]

            if i > start:
                new_length += 1

            if new_length > M:
                break

            line_length = new_length
            i += 1

        # No penalty for last line
        if i < n:
            extra = M - line_length
            total_cost += extra ** 2

    return total_cost


words = [3, 2, 2, 5]
M = 6

dp_cost = min_wrap_cost(words, M)
greedy_cost = greedy_wrap_cost(words, M)

print("DP Cost:", dp_cost)
print("Greedy Cost:", greedy_cost)

assert dp_cost <= greedy_cost
assert dp_cost == 19

print("All test cases passed!")
