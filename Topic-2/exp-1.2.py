def selection_sort_min_writes(arr):
    a = arr.copy()
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1

    return a, swaps


n = int(input("Enter the number of temperature readings: "))

readings = []
print("Enter the temperature readings:")
for i in range(n):
    value = float(input(f"Reading {i + 1}: "))
    readings.append(value)

sorted_readings, swap_count = selection_sort_min_writes(readings)

print("\nSorted Temperature Readings:")
print(sorted_readings)

print("Number of Swaps:", swap_count)


