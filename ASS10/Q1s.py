import numpy as np

def is_safe(board, row, col, n):
    """Check if a queen can be placed at (row, col) safely."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False  # Column or diagonal conflict
    return True

def solve_n_queens(n, row=0, board=[]):
    """Solve N-Queens using backtracking."""
    if row == n:
        return [board.copy()]  # A valid solution found
    
    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solutions.extend(solve_n_queens(n, row + 1, board))
            board.pop()  # Backtrack
    
    return solutions

# Find one valid solution for 8-Queens
solutions = solve_n_queens(8)
solution_board = np.zeros((8, 8), dtype=int)

for r, c in enumerate(solutions[0]):  # Use the first valid solution
    solution_board[r, c] = 1

print("Valid 8-Queens Solution:\n", solution_board)