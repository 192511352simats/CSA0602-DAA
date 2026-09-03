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


text = input("Enter the command/text: ").lower()

dictionary = input(
    "Enter valid vocabulary words separated by spaces: "
).lower().split()


result = can_segment(text, dictionary)


if result:
    print("\nValid command: YES")
else:
    print("\nValid command: NO")
