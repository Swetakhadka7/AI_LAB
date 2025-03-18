import random

# Constants
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the board is full
def is_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check other diagonal
        return True
    return False

# Minimax algorithm to find the best move for AI
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, PLAYER_X):
        return -1
    if check_winner(board, PLAYER_O):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_val = float('-inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # User's turn (Player X)
        print("Your turn (Player X):")
        while True:
            try:
                user_input = input("Enter row and column (0, 1, or 2) separated by space: ")
                row, col = map(int, user_input.split())
                if row in range(3) and col in range(3):  # Ensure the row and column are valid
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_X
                        break
                    else:
                        print("Cell already occupied. Try again.")
                else:
                    print("Invalid row or column. Please enter values between 0 and 2.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two integers separated by space, each between 0 and 2.")

        print_board(board)

        if check_winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's turn (Player O)
        print("AI's turn (Player O):")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        print(f"AI played at {ai_move[0]}, {ai_move[1]}")
        print_board(board)

        if check_winner(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
