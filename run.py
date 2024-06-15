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

def place_cpu_battleships():
    """
    Place battleships in cpu board (x5) at random
    """
    for ship in range(5):