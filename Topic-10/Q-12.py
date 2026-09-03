def rod_cut(price, n):

    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        for j in range(i):

            dp[i] = max(
                dp[i],
                price[j] + dp[i - j - 1]
            )

    return dp[n]


n = int(input("Enter length of rod: "))

price = []

for i in range(n):

    p = int(input(f"Enter price for rod length {i + 1}: "))

    price.append(p)


print("Maximum Revenue =", rod_cut(price, n))
