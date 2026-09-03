def lps_length(s):

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


def audit_log_windows(log_stream, window_size):

    results = []

    for i in range(len(log_stream) - window_size + 1):

        window = log_stream[i:i + window_size]

        length = lps_length(window)

        results.append((window, length))

    return results


# Test cases
assert lps_length("bbbab") == 4
assert lps_length("cbbd") == 2

print("All test cases passed!")


# User input
log_stream = input("\nEnter the log sequence: ")

window_size = int(input("Enter window size: "))

if window_size <= 0 or window_size > len(log_stream):
    print("Invalid window size!")

else:

    results = audit_log_windows(log_stream, window_size)

    print("\nLog Window Analysis:")

    for window, length in results:
        print(f"Window: {window} → LPS Length: {length}")
