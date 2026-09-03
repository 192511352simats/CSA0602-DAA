def fractional_knapsack(weights, profits, capacity):

    items = []

    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i]))

    items.sort(reverse=True)

    total = 0

    for ratio, weight, profit in items:

        if capacity >= weight:
            total += profit
            capacity -= weight

        else:
            total += ratio * capacity
            capacity = 0
            break

    return total


n = int(input("Enter number of relief items: "))

weights = list(map(float, input("Enter weights: ").split()))
profits = list(map(float, input("Enter importance/profits: ").split()))

capacity = float(input("Enter truck capacity: "))

print("Maximum profit =", fractional_knapsack(weights, profits, capacity))
