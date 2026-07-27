def all_occurrences(arr, key):
    pos = []

    for i in range(len(arr)):
        if arr[i] == key:
            pos.append(i + 1)

    if pos:
        print("Occurrences at positions:", *pos, sep=" ")
        print("Total occurrences =", len(pos))
    else:
        print("Element not found")

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

all_occurrences(arr, key)
