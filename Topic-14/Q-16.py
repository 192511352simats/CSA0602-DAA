def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]

    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def solve(row):
        if row == n:
            return True

        for col in range(n):

            if col in columns:
                continue

            if row - col in diagonal1:
                continue

            if row + col in diagonal2:
                continue

            board[row][col] = "Q"

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            if solve(row + 1):
                return True

            board[row][col] = "."

            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

        return False

    if solve(0):
        return board
    else:
        return None


# User Input
n = int(input("Enter the value of N: "))

solution = solve_n_queens(n)

if solution:
    print("\nOne Valid Solution:")

    for row in solution:
        print(" ".join(row))
else:
    print("No solution exists")
