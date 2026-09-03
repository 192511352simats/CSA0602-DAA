def lps_length(s):
    n = len(s)

    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def lcs_length(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Test Cases
assert lps_length("bbbab") == lcs_length("bbbab", "bbbab"[::-1])
assert lps_length("cbbd") == lcs_length("cbbd", "cbbd"[::-1])

print("All test cases passed!")


# User Input
s = input("\nEnter a string: ")

reverse_s = s[::-1]

lps = lps_length(s)
lcs = lcs_length(s, reverse_s)

print("\nOriginal String:", s)
print("Reversed String:", reverse_s)

print("\nLPS Length =", lps)
print("LCS Length =", lcs)

if lps == lcs:
    print("Result: LPS and LCS values are equal.")
else:
    print("Result: Values are not equal.")
