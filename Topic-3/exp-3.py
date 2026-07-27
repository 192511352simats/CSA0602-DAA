def first_occurrence(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("First occurrence at position", i + 1)
            return
    print("Element not found")

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

first_occurrence(arr, key)
