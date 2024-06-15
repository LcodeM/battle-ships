# Ref: ioflood.com blog
from random import randint

# Board for cpu ships to be placed, using list of empty spaces
CPU_BOARD = [[' '] * 8 for x in range(8)]
# Board for user guesses to be placed, using list of empty spaces
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

# Convert letters to numbers for user input using dictionary:
# (0, 0) input would be A1 on board axis
# Ref CI LMS dictionary comprehensions
y_axis_converter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}


def generate_board(board):
    """
    Create boards, axis and separate columns using "|"
    Include row/column number and letter and separate rows
    """
    # 3 spaces to '-' and letters to format spacing
    # Reference: Knowledge Mavens Youtube
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    # For each row, create board contents
    for row in board:
        # Print "|" either side of columns for division
        # Reference: Knowledge Mavens Youtube & Phind.com
        print(f"{row_number}|{'|'.join(row)}|")
        # Increment row number by 1 for length of rows list (8)
        row_number += 1


def place_cpu_battleships(board):
    """
    Place battleships in cpu board (x5) at random
    Range 5 for 5 ships
    """
    for ship in range(5):
        # Generate random integer with row and column pair (1, 1 = A1 etc.)
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        # If the chosen numbers are equal to X on the board,
        # generate again
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7)
        # If empty, assign 'X'
        board[ship_row][ship_column] = 'X'


def choose_row():
    """
    User input for ship row location
    """
    # While loop to run through inputs until valid
    while True:
        # Look for integer input between 1 and 8
        try:
            row = input('Please enter a row 1-8\n')
            if row not in '1234567':
                # If input not valid, return error and run again
                raise ValueError("Invalid row")
            break
        # Report error to user in terminal
        except ValueError as e:
            print(f"Error: {e}\n Please enter a valid row")
    # Return our number and adjust for 0 indexing
    return int(row) -1


def choose_column():
    """
    User input for ship column location
    """
    try:
        row = input('Please enter a row 1-8\n')
        if row not in '1234567':
            # If input not valid, return error and run again
            raise ValueError("Invalid row")
    # Report error to user in terminal
    except ValueError as e:
        print(f"Error: {e}\n Please enter a valid row")

generate_board(PLAYER_BOARD)