def can_segment(s, dictionary):

    word_set = set(dictionary)

    n = len(s)

    dp = [False] * (n + 1)

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

print("All test cases passed!")


# User Input
text = input("\nEnter OCR text without spaces: ")

n = int(input("Enter number of dictionary words: "))

dictionary = []

print("Enter dictionary words:")

for i in range(n):

    word = input(f"Word {i + 1}: ")

    dictionary.append(word)


if can_segment(text, dictionary):

    print("\nOCR Text Status: SEGMENTABLE")
    print("The text can be divided into valid dictionary words.")

else:

    print("\nOCR Text Status: NOT SEGMENTABLE")
    print("Manual correction may be required.")
