def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at position", i + 1)
            print("Number of comparisons =", i + 1)
            return
    print("Element not found")
    print("Number of comparisons =", len(arr))

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

sequential_search(arr, key)
