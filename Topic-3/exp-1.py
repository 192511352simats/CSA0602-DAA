def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i + 1
    return -1

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

pos = sequential_search(arr, key)

if pos != -1:
    print("Element found at position", pos)
    print("Number of comparisons =", pos)
else:
    print("Element not found")
