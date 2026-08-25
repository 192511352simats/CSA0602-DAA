n = int(input("Total Volunteers: "))
r = int(input("Group Size: "))

c = 1
for i in range(1, r + 1):
    c = c * (n - i + 1) // i

print("Number of Groups =", c)
