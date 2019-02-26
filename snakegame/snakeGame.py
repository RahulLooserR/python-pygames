import pygame, sys, random, time, numpy
from pygame.locals import *



# setting windows width and height and other variables
WIDTH     = 600
HEIGHT    = 700
BOUNDARY  = 100 
BLOCKSIZE = 10    # blocksize used for food and each block of snake
length    = 3 	  # intial length of snake 
x, y = [100, 200] # initial position of snake
snake = [[x, y], [x, y-10], [x, y-20]] # Drawing initial snake with 3 blocks

# colors
RED   = (255,   0,   0) 
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREY  = (128, 128, 128)
 
# creating tuple for the colors
colors = (RED, BLUE, GREEN, WHITE, BLACK, GREY)

# variable for food
foodX = -10
foodY = -10
food  = 0
foodCount = 0

# variable to check wether game is over
gameOver = 0

# initial direction of movement for snake
direction = 'right' 

# setting fps
fps = 15
clock = pygame.time.Clock ()

# starting the game
pygame.init()

# font setup to display gameover and other information
fontObj = pygame.font.Font ('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render ('!!! GAME OVER !!!', True, colors[0], colors[5])
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (WIDTH/2, HEIGHT/2)

fontScore = pygame.font.SysFont ('arial', 15)


# Drawing the window
WINDOW = pygame.display.set_mode ((WIDTH, HEIGHT), pygame.HWSURFACE, 32)
pygame.display.set_caption ('Snake Game')

# starting game loop
while True:
	WINDOW.fill(GREY)
	pygame.draw.rect (WINDOW, colors[0], (foodX, foodY, BLOCKSIZE, BLOCKSIZE))
	pygame.draw.aaline (WINDOW, BLACK, (0, BOUNDARY), (WIDTH, BOUNDARY), 1)

	# checking if game is over
	if snake[0][0] in [0, WIDTH] or snake[0][1] in [BOUNDARY, HEIGHT] :
		gameOver = 1
		WINDOW.blit (textSurfaceObj, textRectObj)  # drawing font on screen
	
	# checking if food is present in the window
	if food == 0:
		foodX = random.randint(0,  (WIDTH-BLOCKSIZE)/BLOCKSIZE) * BLOCKSIZE 
		foodY = random.randint(BLOCKSIZE,  (HEIGHT-BLOCKSIZE)/BLOCKSIZE) * BLOCKSIZE
		pygame.draw.rect (WINDOW, colors[0], (foodX, foodY, BLOCKSIZE, BLOCKSIZE))
		food = 1
	
	newHead  = [snake[0][0], snake[0][1]]
	snake.insert(0, newHead)

	if direction == 'up' and gameOver == 0:
		newHead[1] -= BLOCKSIZE 
	if direction == 'down' and gameOver == 0:
		newHead[1] += BLOCKSIZE
	if direction == 'left' and gameOver == 0:
		newHead[0] -= BLOCKSIZE
	if direction == 'right'and gameOver == 0:
		newHead[0] += BLOCKSIZE

	for i in range (length):
		tempx, tempy = snake[i]
		pygame.draw.rect (WINDOW, colors[4], (tempx, tempy, BLOCKSIZE, BLOCKSIZE))
	
	# checking if food is eaten
	if newHead[0] == foodX and newHead[1] == foodY:
		food = 0
		length += 1   # increasing length of snake
		foodCount += 1

	for event in pygame.event.get ():
		if event.type == QUIT:
			pygame.quit()
			sys.exit ()

	Pressed_keys = pygame.key.get_pressed ()
		
		# checking key press
	if Pressed_keys[K_UP]:
		if direction == 'down':
			pass
		else:	
			direction = 'up'

	elif Pressed_keys[K_DOWN]:
		if direction == 'up':
			pass
		else:
			direction = 'down'

	elif Pressed_keys[K_LEFT]:
		if direction == 'right':
			pass
		else:
			direction = 'left'

	elif Pressed_keys[K_RIGHT]:
		if direction == 'left':
			pass
		else:
			direction = 'right'

	
	textCount = fontScore.render ('Score : ' + str (foodCount), True, colors [1], GREY)
	textCountRect = textCount.get_rect()
	textCountRect.center = (500, 50)
	WINDOW.blit (textCount, textCountRect)

	pygame.display.update()
	clock.tick(fps)

