# My XoX game

board =['']*10
currentPlayer = 'X'
winner = None
gameRunning = True
#def main():
#   print("Be bazi-ye DOZ khosh amadid!")
#   input('Esmet chie?:')
#main()

# Create board and show it
def showGame(board):
    print('      |     |')
    print('      |     |')
    print('' + board[0] + '      |' + board[1] + '     |' + board[2])
    print('--------------------')
    print('      |     |')
    print('' + board[3] + '      |' + board[4] + '     |' + board[5])
    print('      |     |')
    print('--------------------')
    print('' + board[6] + '      |' + board[7] + '     |' + board[8])
    print('      |     |')
    print('      |     |')

showGame(board)

# Create player
def playerInput(board):
    inp = int(input("Enter a nubmer between 1 to 9: "))
    if board[inp-1] == '':
        board[inp-1] = currentPlayer
    else:
        print('Player is already there')
# Check the winner

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
    elif board[2] == board[4] == board[6] and board[2] != '':
        winner = board[2]
        return True
# Check tie
def checkTie(board):
    global gameRunning
    if '' not in board:
        showGame(board)
        print('It is a tie!')
        gameRunning = False
# Check the winner
def checkWinner():
    global gameRunning
    if checkVertical(board) or checkRow(board) or checkDiag(board):
        print(f'The winner is {winner}')
        gameRunning = False
# Switch the player
def swithPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer ='X'

while gameRunning:
    showGame(board)
    playerInput(board)
    checkTie(board)
    checkWinner()
    swithPlayer()