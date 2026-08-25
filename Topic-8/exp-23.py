e = list(map(int, input("Entry Times: ").split()))
x = list(map(int, input("Exit Times: ").split()))
a = list(map(int, input("Line 1: ").split()))
b = list(map(int, input("Line 2: ").split()))
t1 = list(map(int, input("Transfer 1: ").split()))
t2 = list(map(int, input("Transfer 2: ").split()))

f1 = e[0] + a[0]
f2 = e[1] + b[0]

for i in range(1, len(a)):
    n1 = min(f1 + a[i], f2 + t2[i-1] + a[i])
    n2 = min(f2 + b[i], f1 + t1[i-1] + b[i])
    f1, f2 = n1, n2

print("Minimum Production Time =", min(f1 + x[0], f2 + x[1]))
