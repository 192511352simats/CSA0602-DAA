from functools import lru_cache


def can_segment(text, dictionary):

    word_set = set(dictionary)
    n = len(text)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):

        for j in range(i):

            if dp[j] and text[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


def all_segmentations(text, dictionary):

    word_set = set(dictionary)
    n = len(text)

    @lru_cache(None)
    def solve(start):

        if start == n:
            return [""]

        result = []

        for end in range(start + 1, n + 1):

            word = text[start:end]

            if word in word_set:

                for sentence in solve(end):

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


if can_segment(text, dictionary):

    print("\nText can be segmented.")
    print("\nGenerating all possible segmentations:\n")

    result = all_segmentations(text, dictionary)

    for i, sentence in enumerate(result, 1):
        print(f"{i}. {sentence}")

else:

    print("Text cannot be segmented.")
    print("Enumeration skipped to save computation.")
