def min_coins(coins, amount):

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:

                dp[i] = min(
                    dp[i],
                    dp[i - coin] + 1
                )

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


n = int(input("Enter number of coin types: "))

coins = []

for i in range(n):
    coin = int(input(f"Enter coin {i + 1}: "))
    coins.append(coin)

amount = int(input("Enter amount: "))

result = min_coins(coins, amount)

if result == -1:
    print("It is not possible to make the given amount.")
else:
    print("Minimum Coins =", result)
