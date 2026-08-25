from itertools import product

n = int(input("Number of Dice: "))
m = int(input("Faces per Dice: "))
target = int(input("Target Sum: "))

count = sum(sum(x) == target
            for x in product(range(1, m + 1), repeat=n))

print("Number of ways =", count)
