class WordBreakCache:

    def __init__(self):
        self.cache = {}

    def can_segment(self, text, dictionary):

        key = (text, tuple(sorted(dictionary)))

        if key in self.cache:
            print("Result retrieved from cache.")
            return self.cache[key]

        print("Computing result...")

        word_set = set(dictionary)
        n = len(text)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):

            for j in range(i):

                if dp[j] and text[j:i] in word_set:
                    dp[i] = True
                    break

        self.cache[key] = dp[n]

        return dp[n]


cache = WordBreakCache()

dictionary = input(
    "Enter dictionary words separated by spaces: "
).lower().split()


while True:

    text = input("\nEnter text to check (or type exit): ").lower()

    if text == "exit":
        print("Program ended.")
        break

    result = cache.can_segment(text, dictionary)

    if result:
        print("Valid segmentation: YES")
    else:
        print("Valid segmentation: NO")
