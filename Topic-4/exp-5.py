import math
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def closest(points):
    min_d=float("inf")
    pair=()
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            d=distance(points[i],points[j])
            if d<min_d:
                min_d=d
                pair=(points[i],points[j])
    return pair,min_d
points=eval(input("Enter points: "))
pair,d=closest(points)
print("Closest pair:",pair)
print("Minimum distance:",d)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
