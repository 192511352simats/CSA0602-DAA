def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Register Number found at position", i + 1)
            return
    print("Register Number not found")

n = int(input("Enter number of register numbers: "))
arr = list(map(int, input("Enter register numbers: ").split()))
key = int(input("Enter register number to search: "))

search(arr, key)
