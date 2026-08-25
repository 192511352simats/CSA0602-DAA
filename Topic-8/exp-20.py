n = int(input("Total Players: "))
r = int(input("Players Required: "))

c = 1
for i in range(1, r + 1):
    c = c * (n - i + 1) // i

print("Number of Selections =", c)
