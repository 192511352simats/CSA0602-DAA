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


def count_solutions(board, row, n):

    if row == n:
        return 1

    count = 0

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            count += count_solutions(board, row + 1, n)

            board[row][col] = 0

    return count


n = int(input("Enter value of N: "))

board = [[0] * n for _ in range(n)]

total = count_solutions(board, 0, n)

print("Total Number of Solutions =", total)
