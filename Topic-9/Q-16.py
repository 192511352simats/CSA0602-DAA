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


def suggest_spacing(text, dictionary):
    word_set = set(dictionary)
    n = len(text)

    dp = [False] * (n + 1)
    parent = [-1] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_set:
                dp[i] = True
                parent[i] = j
                break

    if not dp[n]:
        return None

    words = []
    current = n

    while current > 0:
        previous = parent[current]
        words.append(text[previous:current])
        current = previous

    words.reverse()

    return " ".join(words)


identifier = input("Enter the identifier: ").lower()

dictionary = input(
    "Enter vocabulary words separated by spaces: "
).lower().split()

if can_segment(identifier, dictionary):
    print("Identifier can be segmented.")

    result = suggest_spacing(identifier, dictionary)
    print("Suggested identifier:", result)

else:
    print("Identifier cannot be segmented.")
