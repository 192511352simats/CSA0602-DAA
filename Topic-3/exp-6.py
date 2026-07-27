def sentinel_search(arr, key):
    arr.append(key)
    i = 0

    while arr[i] != key:
        i += 1

    arr.pop()

    if i < len(arr):
        print("Position found:", i + 1)
    else:
        print("Element not found")

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

sentinel_search(arr, key)
