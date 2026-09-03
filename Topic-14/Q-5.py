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


def solve_sudoku(grid):

    for row in range(9):

        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):

                    if is_safe(grid, row, col, num):

                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = 0

                return False

    return True


print("Enter Sudoku grid (use 0 for empty cells):")

grid = []

for i in range(9):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    grid.append(row)


if solve_sudoku(grid):

    print("\nSolved Sudoku Grid:")

    for row in grid:
        print(*row)

else:
    print("No solution exists")
