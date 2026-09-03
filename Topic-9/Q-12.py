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
    "catsandog",
    ["cats", "dog", "sand", "and", "cat"]
) == False

print("All test cases passed!")


# User Input
slug = input("\nEnter URL slug: ")

# Remove hyphens
clean_slug = slug.replace("-", "")

n = int(input("Enter number of keywords: "))

dictionary = []

print("Enter keywords:")

for i in range(n):
    word = input(f"Keyword {i + 1}: ")
    dictionary.append(word)


print("\nOriginal URL Slug:", slug)
print("Slug without hyphens:", clean_slug)

if can_segment(clean_slug, dictionary):
    print("Status: VALID URL SLUG")
else:
    print("Status: INVALID - Manual Review Required")
