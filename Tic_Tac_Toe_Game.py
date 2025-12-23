# Tic-Tac-Toe Game in Python

def print_board(board):
    """Prints the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check rows, columns and diagonals for a winner"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Check if the board is full (draw)"""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            # Get player input
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid move! Choose between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue

            # Place move
            board[row][col] = current_player
            print_board(board)

            # Check for win
            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break

            # Check for draw
            if is_full(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    tic_tac_toe()
