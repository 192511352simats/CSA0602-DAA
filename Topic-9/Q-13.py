def min_segments(s, dictionary):

    word_set = set(dictionary)
    n = len(s)

    # Infinity means segmentation is not possible
    dp = [float("inf")] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):

        for j in range(i):

            if dp[j] != float("inf") and s[j:i] in word_set:

                dp[i] = min(
                    dp[i],
                    dp[j] + 1
                )

    if dp[n] == float("inf"):
        return None

    return dp[n]


# Test Cases
# Note: apple + pen + apple = 3 segments
assert min_segments("applepenapple", ["apple", "pen"]) == 3

assert min_segments(
    "catsandog",
    ["cats", "dog", "sand", "and", "cat"]
) is None

print("All test cases passed!")


# User Input
text = input("\nEnter token to check: ")

n = int(input("Enter number of dictionary words: "))

dictionary = []

print("Enter dictionary words:")

for i in range(n):
    word = input(f"Word {i + 1}: ")
    dictionary.append(word)


result = min_segments(text, dictionary)

if result is None:

    print("\nToken cannot be segmented using the dictionary.")

else:

    print("\nMinimum number of segments =", result)

    # Simple spam warning
    if result >= 2:
        print("Status: POSSIBLE KEYWORD STUFFING")
    else:
        print("Status: Normal")
