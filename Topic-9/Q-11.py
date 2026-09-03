def can_segment(s, dictionary):

    word_set = set(dictionary)
    n = len(s)

    dp = [False] * (n + 1)

    # Empty string can always be segmented
    dp[0] = True

    for i in range(1, n + 1):

        for j in range(i):

            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Test Cases
assert can_segment("leetcode", ["leet", "code"]) == True

assert can_segment(
    "applepenapple",
    ["apple", "pen"]
) == True

assert can_segment(
    "catsandog",
    ["cats", "dog", "sand", "and", "cat"]
) == False

print("All test cases passed!")


# User Input
text = input("\nEnter the search query: ")

n = int(input("Enter number of dictionary words: "))

dictionary = []

print("Enter dictionary words:")

for i in range(n):
    word = input(f"Word {i + 1}: ")
    dictionary.append(word)


if can_segment(text, dictionary):
    print("\nQuery can be segmented into dictionary words.")
else:
    print("\nQuery cannot be segmented into dictionary words.")
