arr = list(map(int, input("Enter elements: ").split()))
max_sum = curr_sum = arr[0]
for i in arr[1:]:
    curr_sum = max(i, curr_sum + i)
    max_sum = max(max_sum, curr_sum)
print("Maximum Subarray Sum:", max_sum)
