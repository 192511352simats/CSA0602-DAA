def insertion_sort(log):
    for i in range(1, len(log)):
        key = log[i]
        j = i - 1

        while j >= 0 and log[j] > key:
            log[j + 1] = log[j]
            j -= 1

        log[j + 1] = key
    return log

n = int(input("Enter number of readings: "))
log = list(map(float, input("Enter temperature readings: ").split()))

print("Sorted Log:", insertion_sort(log))
