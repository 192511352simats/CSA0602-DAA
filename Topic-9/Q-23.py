def min_wrap_cost(words, M):
    n = len(words)
    INF = float('inf')

    dp = [INF] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        line_length = 0

        for j in range(i, n):
            line_length += words[j]

            if j > i:
                line_length += 1

            if line_length > M:
                break

            if j == n - 1:
                cost = 0
            else:
                extra = M - line_length
                cost = extra * extra

            dp[i] = min(dp[i], cost + dp[j + 1])

    return dp[0]


def greedy_wrap_cost(words, M):
    n = len(words)
    total_cost = 0
    i = 0

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

        if i < n:
            extra = M - line_length
            total_cost += extra * extra

    return total_cost


words = [3, 2, 2, 5]
M = 6

dp_cost = min_wrap_cost(words, M)
greedy_cost = greedy_wrap_cost(words, M)

print("DP Word Wrap Cost:", dp_cost)
print("Greedy Word Wrap Cost:", greedy_cost)

assert dp_cost == 19
assert dp_cost <= greedy_cost

print("All test cases passed!")
