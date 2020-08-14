import pygame
import ttt

pygame.init()

window_height = 700 
window_width = 700
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255, 255, 0)
line_thickness = int(window_height * 0.025)
grid_thickness = int(line_thickness / 2)

win = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption("TicTacToe")

def grid(win):
	pygame.draw.line(win, white, (0, (window_height/3)),(window_width,(window_height/3)), grid_thickness)
	pygame.draw.line(win, white, (0, (window_height/3*2)),(window_width,(window_height/3*2)), grid_thickness)
	pygame.draw.line(win, white, ((window_width/3), 0),((window_width/3), window_height), grid_thickness)
	pygame.draw.line(win, white, ((window_width/3*2), 0),((window_width/3*2), window_height), grid_thickness)
	pygame.display.update()

def cross(win, y = 0, x = 0):
	ys = y + window_height/3 * 0.2
	xs = x + window_width/3 * 0.2
	ye = y + window_height/3 * 0.8
	xe = x + window_width/3 * 0.8
	pygame.draw.line(win, blue, (ys, xs),(ye, xe), line_thickness)
	pygame.draw.line(win, blue, (ys, xe),(ye, xs), line_thickness)
	pygame.display.update()

def circle(win, y = 0, x = 0):
	centre = (int(y + (window_height/3/2)), int(x +(window_width/3/2)))
	radius = int(window_height/3*0.8/2)
	pygame.draw.circle(win, red, centre, radius, line_thickness)
	pygame.display.update()

def getBlockCoords(y, x):
	yOut = 0
	xOut = 0
	if(y > window_width/3):
		if(y < window_width/3*2):
			yOut = window_width/3
		else:
			yOut = window_width/3*2
	
	if(x > window_height/3):
		if(x < window_height/3*2):
			xOut = window_width/3
		else:
			xOut = window_width/3*2

	return(yOut, xOut)

def gameOver(win, winner):
	pygame.display.set_caption('Show Text')
	font = pygame.font.Font('freesansbold.ttf', 32) 
	text = font.render(winner, True, yellow, blue) 
	textRect = text.get_rect()
	textRect.center = (window_width // 2, window_height // 2)
	win.fill(white)
	win.blit(text, textRect)
	pygame.display.update()
	pygame.time.delay(3000)
	pygame.quit()

def getBlock(y, x):
	yOut = 0
	xOut = 0
	if(y > window_width/3):
		if(y < window_width/3*2):
			yOut = 1
		else:
			yOut = 2
	
	if(x > window_height/3):
		if(x < window_height/3*2):
			xOut = 1
		else:
			xOut = 2

	return(yOut, xOut)

def main():
	run = True
	board = ttt.grid()
	i = 0

	while(run):
		pygame.time.delay(100)
		grid(win)

		if(ttt.checkGameOver(board)):
			if(ttt.stalemate(board)):
				gameOver(win, "Now, nobody wins")
			if(i % 2 == 0):
				gameOver(win, "Blue Wins!!!")
			else:
				gameOver(win, "Red Wins!!!")
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				coords = getBlockCoords(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0])
				block = getBlock(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0])
				if(board[block[0]][block[1]] == [' ']):
					if(i % 2 == 0):
						circle(win, coords[1], coords[0])
						board[block[0]][block[1]] = ['O']
						
					else:
						cross(win, coords[1], coords[0])
						board[block[0]][block[1]] = ['X']
					i += 1
		pygame.display.update()
	pygame.quit()

if(__name__ == '__main__'):
	main()