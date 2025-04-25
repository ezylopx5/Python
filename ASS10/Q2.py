import random
import numpy as np
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check diagonal (")
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True

def solve_n_queens(n, board, row, solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    cols = list(range(n))
    random.shuffle(cols)  # Randomize column selection
    
    for col in cols:
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, board, row + 1, solutions)

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ['.'] * n
        line[board[row]] = 'Q'
        print(" ".join(line))
    print("\n")

def main():
    n = 8  # Size of the board
    solutions = []
    board = [-1] * n  # Track queen positions
    
    solve_n_queens(n, board, 0, solutions)
    
    print(f"Found {len(solutions)} solutions. Displaying one:")
    print_solution(random.choice(solutions))  # Show a random valid solution

if __name__ == "__main__":
    main()