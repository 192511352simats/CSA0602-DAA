def top_k_scores(scores):
    arr = scores.copy()
    n = len(arr)
    k = min(5, n)  
    for i in range(k):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr[:k]

n = int(input("Enter the number of participants: "))

scores = []
print("Enter the scores:")
for i in range(n):
    score = int(input(f"Score {i + 1}: "))
    scores.append(score)

top_scores = top_k_scores(scores)

print("\nTop 5 Scores:")
for score in top_scores:
    print(score)
