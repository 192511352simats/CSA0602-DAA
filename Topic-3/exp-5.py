def search_count(arr, key):
    comparisons = 0
    matches = 0
    mismatches = 0

    for x in arr:
        comparisons += 1
        if x == key:
            matches += 1
        else:
            mismatches += 1

    print("Total comparisons =", comparisons)
    print("Total matches =", matches)
    print("Total mismatches =", mismatches)

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

search_count(arr, key)
