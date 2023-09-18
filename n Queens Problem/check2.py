def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # All queens are placed successfully, add this solution to the list
        solutions.append(["".join(["Q" if x == 1 else "." for x in row]) for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place a queen in this cell
            board[row][col] = 1
            
            # Recur to place queens in the next row
            solve_n_queens_util(board, row + 1, n, solutions)
            
            # Backtrack and remove the queen from this cell
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Example usage:
n = int(input()) # Change this to the desired board size
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
