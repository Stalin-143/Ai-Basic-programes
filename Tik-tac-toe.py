import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'X'
    ai = 'O'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        row, col = map(int, input("Enter your move (row and column 0-2, separated by space): ").split())
        if board[row][col] != ' ':
            print("Cell already occupied. Try again.")
            continue
        board[row][col] = human

        winner = check_winner(board)
        if winner or is_full(board):
            break

        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = ai

        print_board(board)
        winner = check_winner(board)
        if winner or is_full(board):
            break

    print_board(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
