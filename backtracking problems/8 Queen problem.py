def is_safe(board, row, col):
    n = len(board)

    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):
    n = len(board)

    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


n = int(input("Enter number of queens: "))

board = [-1] * n

if solve(board, 0):
    print("Solution:")

    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists")
