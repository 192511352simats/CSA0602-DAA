r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

key = int(input("Enter key: "))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == key:
            print("Element found at Row", i + 1, "Column", j + 1)
            exit()

print("Element not found")
