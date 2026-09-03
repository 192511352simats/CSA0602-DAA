def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    used = [-1] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used[i] = coin

    result = []

    if dp[amount] == float('inf'):
        return [], -1

    while amount > 0:
        result.append(used[amount])
        amount -= used[amount]

    return result, len(result)


n = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

result, minimum = coin_change(coins, amount)

print("Coins used =", *result)
print("Minimum coins =", minimum)
