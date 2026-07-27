def pick_up_card(hand, card):
    hand.append(card)
    i = len(hand) - 2

    while i >= 0 and hand[i] > card:
        hand[i + 1] = hand[i]
        i -= 1

    hand[i + 1] = card
    return hand

n = int(input("Enter number of cards: "))
hand = []

for i in range(n):
    card = int(input("Enter card: "))
    hand = pick_up_card(hand, card)

print("Sorted Hand:", hand)
