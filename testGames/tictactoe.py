# tic-tac-toe game

import random 

def drawBoard (board):
	# function to draw tic-tac-toe board
	print ()
	print (' ' + board[7] + ' | ' + board [8] + ' | ' + board[9])
	print ('---+---+---')
	print (' ' + board[4] + ' | ' + board [5] + ' | ' + board[6])
	print ('---+---+---')
	print (' ' + board[1] + ' | ' + board [2] + ' | ' + board[3])
	

# function to take input from and return what the player is 'x' or 'o'
def playerInput ():
	
	letter = ''
	
	while not (letter == 'X' or letter == 'O'):
		print ('Do you want to be \'X\' or \'O\'? : ', end = '')
		letter = input ().upper ()
	
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

# function to randomly select who will go first either player or computer
def whoWillGoFirst ():
	if (random.randint (0,1) == 0):
		return 'player'
	else:
		return 'computer'

# function to assign move
def makeMove (board, letter, move):
	board[move] = letter

# function to check winner
# b: board
# l: letter
# function check the same letter accross the horizontally,
# vertically and diagonally.
def isWinner (b, l):
	return ((b[7] == l and	b[8] == l and b[9] == l) or
			(b[4] == l and  b[5] == l and b[6] == l) or
			(b[1] == l and  b[2] == l and b[3] == l) or
			(b[1] == l and  b[4] == l and b[7] == l) or
			(b[2] == l and  b[5] == l and b[8] == l) or
			(b[3] == l and  b[6] == l and b[9] == l) or
			(b[7] == l and  b[5] == l and b[3] == l) or
			(b[9] == l and  b[5] == l and b[1] == l))
			
# function to make copy of the main board, to keep track of which position
# position is filled or empty
def copy (board):
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

# function to check wether the space is free to fill letter
# if the board[i] = ' ' then return true
def isSpaceFree (board, move):
	return (board[int(move)] == ' ')

# function to get move of player from (1-9)
# and checking if space is free or not and player do not make same move
def getPlayerMove (board):
	move = ' '

	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree (board, move):
		print ('Enter your move (1-9): ', end = '')
		move = input()
	return int(move)

#function to check if board is full
def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree (board, i):
	  		return False

	return True

# function for selecting random moves from given possible moves
# moveList: list of possible moves
def randomMove (board, moveList):
	possibleMoves = []
	for i in moveList:
		possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice (possibleMoves)
	else:
		return None

# function to make move by the computer
def computerMove (board, cLetter):
	# cLetter : computer letter
	# pLetter : player's letter
	if cLetter == 'X':
		pLetter = 'O'
	else:
		pLetter = 'X'
	
	for i in range (1, 10):
		boardCopy = copy (board)
		if isSpaceFree (boardCopy, i):
			makeMove (boardCopy, cLetter, i)
			if isWinner (boardCopy, cLetter):
				return i
	
	for i in range (1, 10):
		boardCopy = copy (board)
		if isSpaceFree (boardCopy, i):
			makeMove (boardCopy, pLetter, i)
			if isWinner (boardCopy, pLetter):
				return i
	
	move = randomMove (board, [7, 9, 3, 1])
	if move != None:
		return move
	
	if isSpaceFree (board):	
		return 5

	move = randomMove (board, [4, 8, 6, 2])
	if move != None:
		return move
	

# main program
print ('!!! TIC-TAC-TOE !!!')
print ('===================')

while True:
	pLetter, cLetter = playerInput ()
	turn = whoWillGoFirst ()
	print (turn + ' will go first')
	board = [' '] * 10
	playing = True
	print (pLetter)
	print (cLetter)
	
	while playing:
		
		if turn == 'player':
			drawBoard (board)
			move = getPlayerMove (board)
			makeMove (board, pLetter, move)

			if isWinner (board, pLetter):
				drawBoard (board)
				print (' !!! you win !!!')
				playing = False
				break
			
			elif isBoardFull(board):
				print ('!!! Tie !!!')
				break
			else:
				turn = 'computer'

		elif turn == 'computer':
			drawBoard (board)
			move = computerMove (board, cLetter)
			makeMove (board, cLetter, move)

			if isWinner ( board, cLetter):
				drawBoard (board)
				print ('!!! you loose !!!')
				playing = False
				break
			elif isBoardFull(board):
				print ('!!! Tie !!!')
				break
			else:
				turn = 'player'

	playAgain = ''
	
	while (playAgain != 'y' and playAgain != 'n'):
		print ('Do you want to play again [y/n] : ', end = '')
		playAgain = input()
		playAgain = playAgain.lower()
	
	if playAgain != 'y':
		break



















	
