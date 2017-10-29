import random
import sys

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
inputs = 'XO'


def printBoard():
	for x in range(3):
		print(" ".join(board[x]))
	print()


def selectInput():
	pi = input('Do you wish to play as X or O?: ').upper()
	return inputs[inputs.index(pi)]


player_input = selectInput()

if player_input == 'X':
	computer_input = 'O'
else:
	computer_input = 'X'


def playerMove(board, player_input):
	position = input('Enter the row(1-3) and col(1-3) : ').strip().split()
	row = int(position[0]) - 1 
	col = int(position[1]) -1

	if board[row][col] == '-':
		board[row][col] = player_input

	else:
		print("Invalid")


def offence(board, computer_input, player_input):
	#row check
	for x in range(3):	
		if not player_input in board[x]:
			if board[x].count('O') == 2:

				board[x] = computer_input * 3
				return True

	#col check
	for y in range(3):
		array = []

		for x in range(3):
			array.append(board[x][y])

		if not player_input in array:
			if array.count(computer_input) == 2:
				pos = array.index('-')
				board[pos][y] = computer_input
				return True


	#right diagonal check
	array = []
	for x in range(3):
		array.append(board[x][x])
		
	if not player_input in array:
		if array.count(computer_input) == 2:
			pos = array.index('-')
			board[pos][pos] = computer_input
			return True

	#left diagonal check
	array = []
	for y in range(2, -1, -1):
		array.append(board[2 - y][y])

	if not player_input in array:
		if array.count(computer_input) == 2:
			pos = array.index('-')
			board[pos][2 - pos] = computer_input
			return True


def defence(board, computer_input, player_input):

	#row check
	for x in range(3):
		if not computer_input in board[x]: 
			if board[x].count(player_input) == 2:
				pos = board[x].index('-')
				board[x][pos] = computer_input
				return True

	#col check
	for y in range(3):
		array = []

		for x in range(3):
			array.append(board[x][y])

		if not computer_input in  array:
			if array.count(player_input) == 2:
				pos = array.index('-')
				board[pos][y] = computer_input
				return True

	#R diagonal check
	array = []
	for x in range(3):
		array.append(board[x][x])	

	if not computer_input in array:
		if array.count(player_input) == 2:
			pos = array.index('-')
			board[pos][pos] = computer_input
			return True

	#L diagonal check

	array = []
	for y in range(2, -1, -1):
		array.append(board[2 - y][y])

	if not computer_input in array:
		if array.count(player_input) == 2:
			pos = array.index('-')
			board[pos][2 - pos] = computer_input
			return True


def computerMove(board, computer_input, player_input):
	
	flag = offence(board, computer_input, player_input)
	if flag == True:
		return

	flag = defence(board, computer_input, player_input)
	if flag == True:
		return

	if board[0][0] == '-':
		board[0][0] = computer_input

	elif board[2][0] == '-':
		board[2][0] = computer_input

	elif board[0][2] == '-':
		board[0][2] = computer_input

	elif board[2][2] == '-':
		board[2][2] = computer_input

	else:

		while 1:
			row = random.randint(0, 2)
			col = random.randint(0, 2)

			if board[row][col] == '-':
				board[row][col] = computer_input
				break


def checkBoard(board, move_input):

	for x in range(3):
		if board[x].count(move_input) == 3:
			print("{} wins!".format(move_input))
			sys.exit()

	for y in range(3):
		array = []
		for x in range(3):
			array.append(board[x][y])

		if array.count(move_input) == 3:
			print("{} wins!".format(move_input))
			sys.exit()

	array = []
	for x in range(3):
		array.append(board[x][x])

	if array.count(move_input) == 3:
		print("{} wins!".format(move_input))
		sys.exit()

	array = []
	for y in range(2, -1, -1):
		array.append(board[2 - y][y])

	if array.count(move_input) == 3:
		print("{} wins!".format(move_input))
		sys.exit()	

	count = 0
	for x in range(3):
		for y in range(3):
			if board[x][y] != '-':
				count +=1

	if count == 9:
		print("It's a draw.")
		sys.exit(0)


while True:
	print("Player's turn")
	playerMove(board, player_input)
	printBoard()
	checkBoard(board, player_input)

	print("Computer's turn")
	computerMove(board, computer_input, player_input)
	printBoard()
	checkBoard(board, computer_input)

