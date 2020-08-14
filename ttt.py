class Player:
	def __init__(self, icon, name):
		self.name = name
		self.icon = icon

def grid():
	board =  [[' '],[' '],[' ']],[[' '],[' '],[' ']],[[' '],[' '],[' ']]
	return board

def checkHorz(board):
	for row in board:
		if(row[0] == row[1] == row[2] != [' ']):
			return True
	return False

def checkVert(board):
	for i in range(3):
		if(board[0][i] == board[1][i] == board[2][i] != [' ']):
			return True
	return False

def checkDiag(board):
	middle = board[1][1]
	if(middle == board[0][0] == board[2][2] != [' '] or middle == board[0][2] == board[2][0] != [' ']):
		return True
	return False

def stalemate(board):
	for row in board:
		if(row[0] == [' '] or row[1] == [' '] or row[0] == [' ']):
			return False
	return True

def checkGameOver(board):
	if(checkVert(board) or checkHorz(board) or checkDiag(board)) or stalemate(board):
		return True
	return False

def printBoard(board):
	for row in board:
		print(row)

def main():
	p1name = input(f"Player 1 enter your name:\n")
	p1icon =  input(f"Player 1 choose a letter:\n")
	player1 = Player([p1icon], p1name)

	p2icon = p1icon
	p2name = input(f"Player 2 enter your name:\n")
	while(p2icon == p1icon):
		p2icon =  input(f"Player 2 choose a letter:\n")
		if(p2icon == p1icon):
			print("Choose a different letter than Player1...")
		player2 = Player([p2icon],p2name)

	board = grid()
	printBoard(board)
	i = 0
	while(not checkGameOver(board)):
		if(i%2 == 0):
			value = input(f"Player 1({player1.icon}):\n")
			player = player1
		else:
			value = input(f"Player 2({player2.icon}):\n")
			player = player2
		values = value.split(' ')

		if(len(values) != 2):
			print("Invalid input")
			continue
		try:
			x = int(values[0])
			y = int(values[1])
			if(board[x][y] == [' ']):
				board[x][y] = player.icon
			else:
				print("Invalid input")
				continue
		except:
			print("Invalid input")
			continue
		i = i + 1
		printBoard(board)
	print(f"Game Over. {player.name} wins!")

if __name__ == "__main__":
	main()