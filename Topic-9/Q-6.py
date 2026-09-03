def reconstruct_lps(s):
    n = len(s)

    if n == 0:
        return ""

    # Create DP table
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill DP table
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

    # Backtrack to reconstruct the palindrome
    left = []
    right = []

    i = 0
    j = n - 1

    while i <= j:

        if i == j:
            left.append(s[i])
            break

        if s[i] == s[j]:
            left.append(s[i])
            right.append(s[j])

            i += 1
            j -= 1

        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1

        else:
            j -= 1

    return "".join(left + right[::-1])


# Test cases
assert reconstruct_lps("bbbab") == "bbbb"
assert reconstruct_lps("cbbd") == "bb"

print("All test cases passed!")

# User input
text = input("\nEnter a string: ")

result = reconstruct_lps(text)

print("Longest Palindromic Subsequence:", result)
print("Length:", len(result))
