def distribute_prizes(participants):
    arr = participants.copy()
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j][1] > arr[max_index][1]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr
n = int(input("Enter the number of participants: "))
participants = []
print("Enter participant details:")
for i in range(n):
    name = input(f"Participant {i + 1} Name: ")
    score = int(input(f"Participant {i + 1} Score: "))
    participants.append((name, score))
ranking = distribute_prizes(participants)
print("\nContest Prize Ranking:")
rank = 1
for name, score in ranking:
    print(f"Rank {rank}: {name} - {score}")
    rank += 1
