import math
points=eval(input("Enter points: "))
min_d=float("inf")
pair=()
for i in range(len(points)):
    for j in range(i+1,len(points)):
        d=math.dist(points[i],points[j])
        if d<min_d:
            min_d=d
            pair=(points[i],points[j])
print("Closest pair:",pair)
