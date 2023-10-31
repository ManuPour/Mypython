# My XoX game

board =['']*9
currentPlayer = 'X'
winner = None
gameRunning = True

#def main():
#   print("Be bazi-ye DOZ khosh amadid!")
#   input('Esmet chie?:')
#main()

# Create board and show it
def showBoard(board):
    print(board[0] + '      |' + board[1] + '     |' + board[2])
    print('--------------------')
    print(board[3] + '      |' + board[4] + '     |' + board[5])
    print('--------------------')
    print(board[6] + '      |' + board[7] + '     |' + board[8])

# Create player
def playerInput(board):
    while True:  # Use a loop to keep asking for input until a valid move is made
        try:
            inp = int(input("Enter a number between 1 to 9: "))
            if 1 <= inp <= 9 and board[inp - 1] == '':
                board[inp - 1] = currentPlayer
                return
            else:
                print('Invalid input or position already taken, try again')
        except ValueError:
            print('Invalid input, please enter a number between 1 to 9')


# Check the vertical
def checkVertical (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '':
        winner = board[2]
        return True

# Check the row
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '':
        winner = board[6]
        return True

# Check the diagonal
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '':
        winner = board[2]
        return True

# Check the winner
def checkWinner(board):
    global gameRunning
    if checkVertical(board):
        showBoard(board)
        print(f'The winner is {winner}!')
        gameRunning = False
    elif checkRow(board):
        showBoard(board)
        print(f'The winner is {winner}!')
        gameRunning = False
    elif checkDiag(board):
        showBoard(board)
        print(f'The winner is {winner}!')
        gameRunning = False
# Check tie
def checkIfTie(board):
    global gameRunning
    if '' not in board:
        showBoard(board)
        print("It is a tie!")
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer ='X'


while gameRunning:
    showBoard(board)
    playerInput(board)
    checkWinner(board)
    switchPlayer()
    checkIfTie(board)
    checkWinner(board)

