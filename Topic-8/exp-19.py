n = int(input("Total Professors: "))
r = int(input("Committee Size: "))

c = 1
for i in range(1, r + 1):
    c = c * (n - i + 1) // i

print("Number of Committees =", c)
