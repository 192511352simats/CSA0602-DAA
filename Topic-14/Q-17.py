def is_safe(board, row, col, num):

    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def count_solutions(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                count = 0

                for num in range(1, 10):

                    if is_safe(board, row, col, num):

                        board[row][col] = num

                        count += count_solutions(board)

                        board[row][col] = 0

                return count

    return 1


# User Input
board = []

print("Enter the Sudoku grid row by row.")
print("Use 0 for empty cells.\n")

for i in range(9):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    board.append(row)


solutions = count_solutions(board)

print("\nNumber of Valid Solutions =", solutions)
