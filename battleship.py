from random import randint

# variables 

board = []
turn = 0

# welcome
print 'Welcome to "Battleship: The game"' 
print "Here's our sea:"
print "You have 4 turns to sank my battleship"
print ''
#
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
print ""

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


print ""
print ship_row
print ship_col
print ""

##### logic 
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."

    elif guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break

    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."

    else:
        if turn == 3:
            print "Game Over"
        print "You missed my battleship!"
        print ""
        board[guess_row][guess_col] = "X"
        print_board(board)
        print ""
        print "Turn", (turn + 1)
        print ""
        
