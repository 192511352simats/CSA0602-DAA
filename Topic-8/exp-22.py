n = int(input("Total Servers: "))
r = int(input("Servers Selected: "))

c = 1
for i in range(1, r + 1):
    c = c * (n - i + 1) // i

print("Number of Combinations =", c)
