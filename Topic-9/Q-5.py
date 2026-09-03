def lps_length(s):
    n = len(s)

    if n == 0:
        return 0

    prev = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        curr = [0] * (n + 1)

        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev = curr

    return prev[n - 1]

def is_compression_candidate(s):
    lps = lps_length(s)
    score = lps - len(s) / 2

    return score > 0
assert is_compression_candidate("bbbab") == True
assert is_compression_candidate("cbbd") == False
print("All test cases passed!")
s = input("Enter string: ")

lps = lps_length(s)
score = lps - len(s) / 2

print("LPS Length:", lps)
print("Redundancy Score:", score)

if is_compression_candidate(s):
    print("Compression candidate: Yes")
else:
    print("Compression candidate: No")
