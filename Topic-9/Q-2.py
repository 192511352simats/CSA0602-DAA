def palindrome_score(s):
    n = len(s)

    if n == 0:
        return 0

    prev = [0] * n

    for i in range(n - 1, -1, -1):
        curr = [0] * n
        curr[i] = 1

        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev = curr

    return prev[n - 1]



assert palindrome_score("bbbab") > palindrome_score("cbbd")
assert palindrome_score("a") == 1



word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

score1 = palindrome_score(word1)
score2 = palindrome_score(word2)

print(word1, "Score:", score1)
print(word2, "Score:", score2)

if score1 > score2:
    print("Winner:", word1)
elif score2 > score1:
    print("Winner:", word2)
else:
    print("Both words have the same score")
