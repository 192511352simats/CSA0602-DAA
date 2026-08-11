import math
from itertools import permutations
tests=[eval(input("Enter points: "))]
for points in tests:
    best=float("inf")
    path=None
    for p in permutations(points[1:]):
        route=[points[0]]+list(p)+[points[0]]
        d=sum(math.dist(route[i],route[i+1]) for i in range(len(route)-1))
        if d<best:
            best=d
            path=route
    print("Shortest Distance:",best)
    print("Shortest Path:",path)
