def subset_sum(arr, target, index, current):
    if sum(current) == target:
        print(current)
        return
    if index == len(arr) or sum(current) > target:
        return
    subset_sum(arr, target, index + 1, current + [arr[index]])
    subset_sum(arr, target, index + 1, current)
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))
print("Subsets with sum", target, ":")
subset_sum(arr, target, 0, [])
