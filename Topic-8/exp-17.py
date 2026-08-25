n = int(input("Enter n: "))
r = int(input("Enter r: "))

c = 1
for i in range(1, r + 1):
    c = c * (n - i + 1) // i

print("C({}, {}) = {}".format(n, r, c))
