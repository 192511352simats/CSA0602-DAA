def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_all(board, row, n, solutions):

    if row == n:
        solution = [r[:] for r in board]
        solutions.append(solution)
        return

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            solve_all(board, row + 1, n, solutions)

            board[row][col] = 0


n = int(input("Enter value of N: "))

board = [[0] * n for _ in range(n)]
solutions = []

solve_all(board, 0, n, solutions)

print("\nTotal Solutions =", len(solutions))

for i, solution in enumerate(solutions, start=1):

    print(f"\nSolution {i}:")

    for row in solution:
        print(*row)
