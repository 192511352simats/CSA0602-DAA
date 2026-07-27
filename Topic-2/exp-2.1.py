def optimized_bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

n = int(input("Enter number of roll numbers: "))
arr = list(map(int, input("Enter roll numbers: ").split()))

print("Sorted Roll Numbers:", optimized_bubble_sort(arr))
