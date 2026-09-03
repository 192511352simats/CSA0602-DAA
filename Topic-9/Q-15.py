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


text = input("Enter the text without spaces: ")

dictionary = input(
    "Enter dictionary words separated by spaces: "
).split()

result = suggest_spacing(text.lower(), [word.lower() for word in dictionary])

if result:
    print("Suggested spacing:", result)
else:
    print("No valid word segmentation found.")
