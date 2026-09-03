def fractional_knapsack(weights, profits, capacity):

    items = []

    for i in range(len(weights)):
        items.append((
            profits[i] / weights[i],
            weights[i],
            profits[i]
        ))

    items.sort(reverse=True)

    maximum_profit = 0

    for ratio, weight, profit in items:

        if capacity >= weight:
            maximum_profit += profit
            capacity -= weight
        else:
            maximum_profit += ratio * capacity
            break

    return maximum_profit


n = int(input("Enter number of gold items: "))

weights = list(map(float, input("Enter weights: ").split()))
profits = list(map(float, input("Enter profits: ").split()))

capacity = float(input("Enter weight capacity: "))

print("Maximum profit =", fractional_knapsack(weights, profits, capacity))
