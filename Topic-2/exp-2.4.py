def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

n = int(input("Enter number of alerts: "))
alerts = list(map(int, input("Enter alert levels: ").split()))

print("Sorted Alerts:", bubble_sort(alerts))
