import random
import time

# Function to create an empty game board
def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

# Function to print the game board
def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')

# Function to check if a piece can be placed at the given position
def is_valid_position(board, piece, row, col):
    for r in range(len(piece)):
        for c in range(len(piece[0])):
            if piece[r][c] != ' ' and (row + r >= len(board) or col + c >= len(board[0]) or board[row + r][col + c] != ' '):
                return False
    return True

# Function to place a piece on the board
def place_piece(board, piece, row, col):
    for r in range(len(piece)):
        for c in range(len(piece[0])):
            if piece[r][c] != ' ':
                board[row + r][col + c] = piece[r][c]

# Function to remove completed rows and shift the rows above
def remove_completed_rows(board):
    completed_rows = [i for i, row in enumerate(board) if all(cell != ' ' for cell in row)]

    for row_index in completed_rows:
        del board[row_index]
        board.insert(0, [' ' for _ in range(len(board[0]))])

# Function to generate a new random Tetris piece
def generate_piece():
    pieces = [
        [['X', 'X', 'X', 'X']],
        [['X', 'X'], ['X', 'X']],
        [['X', 'X', ' '], [' ', 'X', 'X']],
        [[' ', 'X', 'X'], ['X', 'X', ' ']],
        [['X', 'X', 'X'], [' ', ' ', 'X']],
        [['X', 'X', 'X'], ['X', ' ', ' ']],
        [['X', 'X', 'X'], [' ', 'X', ' ']]
    ]
    return random.choice(pieces)

# Function to rotate a Tetris piece 90 degrees clockwise
def rotate_piece(piece):
    return list(zip(*reversed(piece)))

# Main game loop
def play_game(rows, cols):
    board = create_board(rows, cols)
    current_piece = generate_piece()
    current_row = 0
    current_col = cols // 2 - len(current_piece[0]) // 2
    score = 0

    while True:
        print('Score:', score)
        print_board(board)

        # Move the piece down automatically
        if is_valid_position(board, current_piece, current_row + 1, current_col):
            current_row += 1
        else:
            place_piece(board, current_piece, current_row, current_col)
            remove_completed_rows(board)

            # Check if the game is over
            if any(cell != ' ' for cell in board[0]):
                print('Game Over!')
                break

            # Generate a new piece
            current_piece = generate_piece()
            current_row = 0
            current_col = cols // 2 - len(current_piece[0]) // 2

        time.sleep(0.5)  # Delay between moves

        # Check for user input to move or rotate the piece
        key = input('Enter a key (A: Left, D: Right, W: Rotate): ').upper()

        if key == 'A' and is_valid_position(board, current_piece, current_row, current_col - 1):
            current_col -= 1
        elif key == 'D' and is_valid_position(board, current_piece, current_row, current_col + 1):
            current_col += 1
        elif key == 'W':
            rotated_piece = rotate_piece(current_piece)
            if is_valid_position(board, rotated_piece, current_row, current_col):
                current_piece = rotated_piece

# Start the game with a 10x20 board
play_game(20, 10)
