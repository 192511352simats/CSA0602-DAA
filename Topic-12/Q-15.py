def fractional_knapsack(weights, profits, capacity):

    items = []

    for i in range(len(weights)):

        ratio = profits[i] / weights[i]

        items.append(
            (ratio, weights[i], profits[i])
        )

    # Sort according to profit/weight ratio
    items.sort(reverse=True)

    total_profit = 0

    for ratio, weight, profit in items:

        if capacity >= weight:

            capacity -= weight
            total_profit += profit

        else:

            total_profit += ratio * capacity
            break

    return total_profit


n = int(input("Enter number of items: "))

weights = list(map(float, input("Enter weights: ").split()))

profits = list(map(float, input("Enter profits: ").split()))

capacity = float(input("Enter warehouse capacity: "))

result = fractional_knapsack(weights, profits, capacity)

print("Maximum profit =", result)
