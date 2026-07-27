def bubble_sort_frames(arr):
    print("Original:", arr)

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Pass", i+1, ":", arr)

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

bubble_sort_frames(arr)
