def is_safe(board, row, col):
    # Check if there is a queen in the same row
    if any(board[row]):
        return False

    # Check if there is a queen in the same column
    if any(board[i][col] for i in range(8)):
        return False

    # Check if there is a queen in the upper-left to lower-right diagonal
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check if there is a queen in the upper-right to lower-left diagonal
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, 8))):
        return False

    return True

def solve_queens(board, row):
    if row == 8:
        # All queens are placed successfully
        return True

    for col in range(8):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1

            # Recur to place queens in the remaining rows
            if solve_queens(board, row + 1):
                return True

            # If placing queen in the current position doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If no column is found to place the queen, backtrack to the previous row
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

if __name__ == "__main__":
    # Initialize an 8x8 chessboard
    chessboard = [[0] * 8 for _ in range(8)]

    if solve_queens(chessboard, 0):
        print("Solution found:")
        print_board(chessboard)
    else:
        print("No solution found.")
