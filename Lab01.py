# 1. Name:
#      Tim Howell
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Read the file  if it exists.
    try:
        file = open(filename, "r")
        board_text = file.read()
        board_json = json.loads(board_text)
        return board_json('board')
    # Generate blank board otherwise.
    except:
        return blank_board('board ')

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    with open(filename, "w") as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    # Iterate through each row
    for row in range(3):
        # There is a horizontal bar before evry row except the first.
        if row != 0:
            print("---+---+---")
        # Display each element in a row.
        for col in range(3):
            print(' ', board[row * 3 + col], ' ', 
                  sep = '', end = '\n' if col == 2 else '|')            



def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    num_X = 0
    num_O = 0

    # Count the nubmer of X's and O's.
    for square in board:
        if square == X:
            num_X += 1
        if square == O:
            num_O += 1
    return num_X == num_O



def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    # Place the prompt on the screen.
    x_turn = is_x_turn(board)
    user_input = input("X>" if x_turn else "O>")
    square = int(user_input) -1 if user_input.isdigit() else -1

    # Accept input from the user.
    if 0 <= square <= 8:
        if board[square] == BLANK:
            board[int(user_input) -1] = X if x_turn else 0
        else:
            print("That square is taken. Try again.")
            return True
    else:
        return False
    
# Read the board if one exists.
board = read_board("board.json")


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

display_board(board)
while play_game(board) and not game_done(board, message=True):
    display_board(board)

# The file read code, game loop code, and file close code goes here.
save_board("board,json",  blank_board['board'] if game_done(board) else board)