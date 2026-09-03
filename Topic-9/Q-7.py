def lps_length_optimized(s):

    n = len(s)

    if n == 0:
        return 0

    previous = [0] * n

    # Process characters from right to left
    for i in range(n - 1, -1, -1):

        current = [0] * n
        current[i] = 1

        for j in range(i + 1, n):

            if s[i] == s[j]:
                current[j] = previous[j - 1] + 2

            else:
                current[j] = max(previous[j], current[j - 1])

        previous = current

    return previous[n - 1]


# Test cases
assert lps_length_optimized("bbbab") == 4
assert lps_length_optimized("cbbd") == 2

print("All test cases passed!")

# User input
text = input("\nEnter a string: ")

result = lps_length_optimized(text)

print("Length of Longest Palindromic Subsequence =", result)
