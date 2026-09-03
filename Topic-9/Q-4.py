def base_pair_estimate(s):
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
    return prev[n - 1] // 2
assert base_pair_estimate("bbbab") == 2
assert base_pair_estimate("cbbd") == 1
print("All test cases passed!")
fragment = input("Enter RNA fragment: "
print("Estimated base pairs:", base_pair_estimate(fragment))
