def insert_score(board, score):
    board.append(score)
    i = len(board) - 2

    while i >= 0 and board[i] < score:   # Descending order
        board[i + 1] = board[i]
        i -= 1

    board[i + 1] = score
    return board

n = int(input("Enter number of scores: "))
board = list(map(int, input("Enter scores: ").split()))

score = int(input("Enter updated score: "))

print("Updated Leaderboard:", insert_score(board, score))
