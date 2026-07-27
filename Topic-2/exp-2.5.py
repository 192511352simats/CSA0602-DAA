def bubble_sort(hand):
    for i in range(len(hand)-1):
        swapped = False
        for j in range(len(hand)-1-i):
            if hand[j] > hand[j+1]:
                hand[j], hand[j+1] = hand[j+1], hand[j]
                swapped = True
        if not swapped:
            break
    return hand

n = int(input("Enter number of cards: "))
hand = list(map(int, input("Enter card ranks: ").split()))

new_card = int(input("Enter new card: "))
hand.append(new_card)

print("Sorted Hand:", bubble_sort(hand))
