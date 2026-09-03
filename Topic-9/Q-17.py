from functools import lru_cache


def all_segmentations(text, dictionary):
    word_set = set(dictionary)
    n = len(text)

    # DP check to see whether prefixes are possible
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_set:
                dp[i] = True
                break

    if not dp[n]:
        return []

    @lru_cache(None)
    def solve(start):

        if start == n:
            return [""]

        result = []

        for end in range(start + 1, n + 1):
            word = text[start:end]

            if word in word_set:

                remaining = solve(end)

                for sentence in remaining:

                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                        result.append(word)

        return result

    return solve(0)


text = input("Enter the text: ").lower()

dictionary = input(
    "Enter dictionary words separated by spaces: "
).lower().split()

result = all_segmentations(text, dictionary)

if result:
    print("\nAll Possible Segmentations:")

    for i, sentence in enumerate(result, 1):
        print(f"{i}. {sentence}")

    print("\nTotal Segmentations =", len(result))

else:
    print("No valid segmentation found.")
