from math import dist

n = int(input("Enter number of points: "))
p = []

for i in range(n):
    x, y = map(int, input("Enter x y: ").split())
    p.append((x, y))

m = 999999
pair = ()

for i in range(n):
    for j in range(i + 1, n):
        d = dist(p[i], p[j])
        if d < m:
            m, pair = d, (p[i], p[j])

print("Closest Pair:", pair)
print("Distance:", m)
