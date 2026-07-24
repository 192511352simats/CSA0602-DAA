
import heapq

arr = list(map(int, input("Enter elements: ").split()))

heapq.heapify(arr)

sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))

print("Sorted array:", sorted_arr)
