# Ref: ioflood.com blog
from random import randint

# Board for cpu ships to be placed, using list of empty spaces
CPU_BOARD = [[' '] * 8 for x in range(8)]
# Board for user guesses to be placed, using list of empty spaces
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

# Convert letters to numbers for user input using dictionary:
# (0, 0) input would be A1 on board axis
# Ref CI LMS dictionary comprehensions
y_axis_converter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def generate_board(board):
    """
    Create boards, axis and separate columns using "|"
    Include row/column number and letter and separate rows
    """
    # 3 spaces to '-' and letters to format spacing
    # Reference: Knowledge Mavens Youtube
    print('  A B C D E F G H')
    print('  ---------------')
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
        # If the chosen numbers are equal to O on the board,
        # generate again
        while board[ship_row][ship_column] == 'O':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        # If empty, assign 'O'
        board[ship_row][ship_column] = 'O'


def choose_row():
    """
    User input for ship row location
    """
    # While loop to run through inputs until valid
    while True:
        # Look for integer input between 1 and 8
        try:
            row = input('Please enter a row 1-8\n')
            if row not in '12345678':
                # If input not valid, return error and run again
                raise ValueError("Invalid row")
            # Re-run until valid
            break
        # Report error to user in terminal
        except ValueError as e:
            print(f"Error: {e}\n Please enter a valid row")
    # Return our number and adjust for 0 indexing
    return int(row) - 1


def choose_column():
    """
    User input for ship column location
    """
    # While loop to run through inputs until valid
    while True:
        try:
            column = input('Please enter a column A-H\n').upper()
            if column not in 'ABCDEFGH':
                # If input not valid, return error and run again
                raise ValueError("Invalid column")
            # Re-run until valid
            break
        # Report error to user in terminal
        except ValueError as e:
            print(f"Error: {e}\n Please enter a valid column")
    # Return column
    return column


def choose_coordinates():
    """
    Show choice by calling row & column functions (above)
    """
    # Define row and column and pass functions above
    row = choose_row()
    column = choose_column()
    # Return both values, convert column letter to an integer
    return row, y_axis_converter[column]


def count_hits(board):
    """
    Function to increment hit battleships when guess is correct
    """
    # Beging count on 0
    count = 0
    # for loop for CPU board
    for row in board:
        # Include column guess in check
        for column in row:
            # Check if selected column in row contains 'O'
            if column == 'O':
                # If true, increment count by 1
                count =+ 1
    # Show count
    return count


# Welcome message for users
print("\033[1;32;40mWelcome to Battleships\n")
# Instructions for starting the game
print("Select a row then a column to try and hit the battleships\n")

place_cpu_battleships(CPU_BOARD)
# generate_board(CPU_BOARD) ** UNCOMMENT TO SEE SHIP LOCATIONS **


# Declare turns, set to 10
turns = 10
# Run the game while turns are greater than 0
while turns > 0:
    """
    While loop that runs through player guess outcomes
    to determine hit/miss/already guessed coordinates.
    End of game hits = 5 (WIN) OR turns = 0 (LOSE)
    """
    # Show players board (only) while turns > 0
    generate_board(PLAYER_BOARD)
    # Get player inputs
    row, column = choose_coordinates()
    # If players already chosen coordinates print message
    if PLAYER_BOARD[row][column] == '-':
        print("Already guessed those coordinates")
    # Otherwise, if CPU board coords are O, print hit message
    elif CPU_BOARD[row][column] == 'O':
        print("That's a HIT!")
        # Update player board with X for hit.
        PLAYER_BOARD[row][column] = 'X'
    # If user misses
    else:
        print("Sorry, you missed...")
        # Mark player board with a miss marker
        PLAYER_BOARD[row][column] = '-'
        # Reduce number of turns by 1
        turns -= 1
    # If all ships hit (=5)
    if count_hits(PLAYER_BOARD) == 5:
        # Print congratualtions message
        print("CONGRATULATIONS! You sunk all battleships.")
        # End the game
        break
    # Display remaining turns after each guess.
    print(f"You have {turns} turns remaining.\n")
# If no more turns left, end game
if turns == 0:
    print("Game over... You ran out of turns.")
