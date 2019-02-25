import sys, random, pygame 
from pygame.locals import *

# init
pygame.init()
clockRate = pygame.time.Clock()

# window
WIDTH = 500
HEIGHT = 500

windowSurface = pygame.display.set_mode ((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption ('collision detection')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# movememt variables
# mLeft : moveLeft
mLeft = False
mRight = False
mUp = False
mDown = False
SPEED = 4

# setting up counter
counter = 0
NEWBLOCK = 40
BLOCKSIZE = 20
	# rectange coordinate : Rect (left, top, width, height)
player = pygame.Rect (400, 100, 50, 50)
blocks = []
for i in range (20):
	blocks.append (pygame.Rect (random.randint (0, WIDTH - BLOCKSIZE),
	random.randint (0, HEIGHT - BLOCKSIZE), BLOCKSIZE, BLOCKSIZE))

# GAMELOOP
while True:
	for event in pygame.event.get():
		if event.type == QUIT :
			pygame.quit()
			sys.exit ()

		# when key is pressed
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				mLeft = True
				mRight = False

			if event.key == K_RIGHT or event.key == K_d:
				mRight = True
				mLeft = False

			if event.key == K_UP or event.key == K_w:
				mUp = True
				mDown = False

			if event.key == K_DOWN or event.key == K_s:
				mDown = True
				mUp = False

		# when a key is released
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit

			if event.key == K_LEFT or event.key == K_a:
				mLeft = False

			if event.key == K_RIGHT or event.key == K_d:
				mRight = False

			if event.key == K_UP or event.key == K_w:
				mUp = False

			if event.key == K_DOWN or event.key == K_s:
				mDown = False

			if event.key == K_x:
				player.top = random.randint(0, WINDOWHEIGHT - player.height)
				player.left = random.randint(0, WINDOWWIDTH - player.width)

		# when mopuse button is released
		if event.type == MOUSEBUTTONUP:
			blocks.append ( pygame.Rect ( event.pos[0], event.pos[1],
			BLOCKSIZE, BLOCKSIZE))
			
	counter = counter + 1
	if counter >= NEWBLOCK:
		counter = 0
		blocks.append (pygame.Rect (random.randint (0, WIDTH - BLOCKSIZE), 
		random.randint (0, HEIGHT - BLOCKSIZE), BLOCKSIZE, BLOCKSIZE))
			
	# drawing white surface
	windowSurface.fill (WHITE)
	
	# move the player
	if mDown and player.bottom < HEIGHT:
		player.top += SPEED

	if mUp and player.top > 0:
		player.top -= SPEED

	if mLeft and player.left > 0:
		player.left -= SPEED

	if mRight and player.right < WIDTH:
		player.right += SPEED			

	# drawing player on the surface
	pygame.draw.rect (windowSurface, BLACK, player)
	
	#checking wether player is touching any square or not
	for block in blocks[:]:
		if player.colliderect (block):
			blocks.remove (block)

	# draw the block
	for i in range (len (blocks)):
		pygame.draw.rect (windowSurface, GREEN, blocks[i])

	# Draw the window onto the screen.
	pygame.display.update()
	clockRate.tick(40)

