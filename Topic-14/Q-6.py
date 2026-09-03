def is_safe(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

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


print("Enter Sudoku grid (0 for empty cells):")

grid = []

for i in range(9):
    grid.append(list(map(int, input().split())))


if solve_sudoku(grid):

    print("\nSudoku Solvable: YES")
    print("Solution Found Successfully")

else:
    print("\nSudoku Solvable: NO")
