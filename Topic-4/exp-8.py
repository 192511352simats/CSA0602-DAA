from itertools import combinations
points=eval(input("Enter points: "))
hull=set()
for a,b in combinations(points,2):
    side=[]
    for p in points:
        c=(b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        side.append(c)
    if all(x>=0 for x in side) or all(x<=0 for x in side):
        hull.add(a)
        hull.add(b)
print("Convex Hull Points:",list(hull))
