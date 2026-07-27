def search(arr, key):
    count = 0

    for i in range(len(arr)):
        count += 1
        print("Comparing", arr[i])

        if arr[i] == key:
            print("Found at position", i + 1)
            print("Comparisons =", count)
            return

    print("Element not found")
    print("Comparisons =", count)

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

key = int(input("Enter key: "))
search(arr, key)

