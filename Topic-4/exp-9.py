from itertools import combinations
points=eval(input("Enter points: "))
hull=set()
for a,b in combinations(points,2):
    left=right=0
    for p in points:
        c=(b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        if c>0:left+=1
        elif c<0:right+=1
    if left==0 or right==0:
        hull.add(a)
        hull.add(b)
print("Convex Hull Points:",list(hull))
