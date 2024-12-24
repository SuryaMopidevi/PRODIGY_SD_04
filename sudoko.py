import random

# Function to check if it's safe to place a number in the given row and column
def is_safe(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 0 indicates an empty cell
                # Try all numbers from 1 to 9
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        # Assign the number and continue
                        board[row][col] = num
                        
                        if solve_sudoku(board):  # Recursively try to solve
                            return True
                        
                        # If it doesn't work, backtrack
                        board[row][col] = 0
                return False  # If no number fits, return False
    return True  # If all cells are filled, return True

# Function to print the board in a readable format
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Function to generate a random complete Sudoku board
def generate_complete_board():
    board = [[0] * 9 for _ in range(9)]
    
    def fill_board(board):
        # Try filling the board recursively with random numbers
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    random_numbers = list(range(1, 10))
                    random.shuffle(random_numbers)
                    for num in random_numbers:
                        if is_safe(board, row, col, num):
                            board[row][col] = num
                            if fill_board(board):  # Recursively try to fill the board
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    fill_board(board)
    return board

# Function to remove some numbers from the grid to create a puzzle
def create_puzzle(board, num_holes=40):
    puzzle = [row[:] for row in board]  # Make a copy of the complete board
    attempts = 0
    while attempts < num_holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts += 1
    return puzzle

# Generate a random complete board
complete_board = generate_complete_board()

# Create a random Sudoku puzzle from the complete board
random_puzzle = create_puzzle(complete_board)

# Display the random Sudoku puzzle
print("Random Sudoku Puzzle:")
print_board(random_puzzle)

# Solve the puzzle
if solve_sudoku(random_puzzle):
    print("\nSolved Sudoku:")
    print_board(random_puzzle)
else:
    print("No solution exists.")
