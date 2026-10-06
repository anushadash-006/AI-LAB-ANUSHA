# Check if placing a queen is safe
def is_safe(board, row, col):

    # Check current column in previous rows
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


# Solve 8-Queens problem
def solve_8_queens(board, row):

    # Base case: all 8 queens are placed
    if row == 8:
        return True

    for col in range(8):

        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Place queen

            if solve_8_queens(board, row + 1):
                return True

            board[row][col] = ' '  # Backtrack

    return False


# Initialize 8x8 board
board = [[' ' for _ in range(8)] for _ in range(8)]

# Solve and display the solution
if solve_8_queens(board, 0):
    print("Solution for 8-Queens Problem:\n")

    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")