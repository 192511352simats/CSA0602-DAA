def is_safe(grid, row, col, num):

    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


print("Enter Sudoku grid (9 rows, 9 numbers each):")

grid = []

for i in range(9):
    row = list(map(int, input(f"Row {i}: ").split()))
    grid.append(row)

row = int(input("Enter row (0-8): "))
col = int(input("Enter column (0-8): "))
num = int(input("Enter number to place (1-9): "))

if grid[row][col] != 0:
    print("Cell is already filled")

elif is_safe(grid, row, col, num):
    print("Safe Placement: YES")

else:
    print("Safe Placement: NO")
