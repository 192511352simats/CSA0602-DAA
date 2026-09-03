def lps_length_optimized(s):

    n = len(s)

    if n == 0:
        return 0

    previous = [0] * n

    for i in range(n - 1, -1, -1):

        current = [0] * n
        current[i] = 1

        for j in range(i + 1, n):

            if s[i] == s[j]:
                current[j] = previous[j - 1] + 2

            else:
                current[j] = max(previous[j], current[j - 1])

        previous = current

    return previous[n - 1]


def is_weak_password(password, threshold=0.6):

    if len(password) == 0:
        return False

    lps_length = lps_length_optimized(password)

    ratio = lps_length / len(password)

    return ratio >= threshold


# Test cases
assert is_weak_password("bbbab", threshold=0.6) == True
assert is_weak_password("cbbd", threshold=0.6) == False

print("All test cases passed!")


# User input
password = input("\nEnter password: ")
threshold = float(input("Enter weakness threshold (example 0.6): "))

lps = lps_length_optimized(password)
ratio = lps / len(password) if len(password) > 0 else 0

print("\nPassword Length =", len(password))
print("LPS Length =", lps)
print("LPS Ratio =", round(ratio, 2))

if is_weak_password(password, threshold):
    print("Password Status: WEAK - Flagged for Review")
else:
    print("Password Status: ACCEPTABLE")
