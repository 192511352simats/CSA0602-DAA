import time

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a
n = int(input("Enter the number of recently viewed items (8-10): "))
prices = []
print("Enter the item prices:")
for i in range(n):
    price = int(input(f"Price {i + 1}: "))
    prices.append(price)
start_time = time.perf_counter()
sorted_prices = selection_sort(prices)
end_time = time.perf_counter()
print("\nSorted Prices:")
print(sorted_prices)
print("Execution Time:", (end_time - start_time) * 1_000_000, "microseconds")
