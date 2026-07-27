def insert_price(prices, price):
    prices.append(price)
    i = len(prices) - 2

    while i >= 0 and prices[i] > price:
        prices[i + 1] = prices[i]
        i -= 1

    prices[i + 1] = price
    return prices

n = int(input("Enter number of stock prices: "))
prices = []

for i in range(n):
    p = float(input("Enter price: "))
    prices = insert_price(prices, p)

print("Sorted Prices:", prices)
