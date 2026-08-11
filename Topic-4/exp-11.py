from itertools import combinations
s=eval(input("Enter set: "))
target=int(input("Enter target sum: "))
found=False
for r in range(1,len(s)+1):
    for sub in combinations(s,r):
        if sum(sub)==target:
            print("Subset found:",list(sub))
            print("Sum:",target)
            found=True
            break
    if found:
        break
if not found:
    print("No subset found")
