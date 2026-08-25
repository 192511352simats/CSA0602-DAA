from itertools import product

n = int(input("Number of Dice: "))
m = int(input("Faces per Dice: "))
target = int(input("Target Score: "))

count = 0
for x in product(range(1, m + 1), repeat=n):
    if sum(x) == target:
        count += 1

print("Number of ways =", count)
