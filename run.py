# Board for cpu ships to be placed, using list of empty spaces
CPU_BOARD = [[' '] * 8 for x in range(8)]
# Board for user guesses to be placed, using list of empty spaces
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

# Convert letters to numbers for user input using dictionary:
# (0, 0) input would be A1 on board axis
# Ref CI LMS dictionary comprehensions
y_axis_converter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

