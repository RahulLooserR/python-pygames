from BirdClass import *
import PipePairClass
from PipePairClass import *
from Globals import *

# initialising the pygame module
pygame.init()
# creating bird with initial position
bird = Bird(startx, starty)

# list for pipes
pipes = []

value = WIDTH

# score of the game
score = 0

# creating initial 3 pipes with some gap between them
for i in range(3):
	gap = random.randint(300, 450)
	pipes.append(PipePair(value))
	value = value + gap


def reset():
	global GameOver
	GameOver = 0

	global bird
	# creating bird with initial position
	bird = Bird(startx, starty)
	bird.reset()

	# list for pipes
	global pipes
	pipes = []
	
	global value
	value = WIDTH

	# score of the game
	PipePairClass.count = 0

	global keyPressed
	keyPressed = False
	# creating initial 3 pipes with some gap between them
	for i in range(3):
		gap = random.randint(300, 450)
		pipes.append(PipePair(value))
		value = value + gap



# font for play again
fontPlayAgain = pygame.font.SysFont ('arial', 20, bold=True) 
textPlayAgain = fontPlayAgain.render ('Play Again!', True, GREEN)
textPlayAgainRect = textPlayAgain.get_rect()
textPlayAgainRect.center = (WIDTH/2, HEIGHT/2 + 60)
# area for clickable place
tx = textPlayAgainRect.left
w = textPlayAgainRect.left + textPlayAgainRect.width
ty = textPlayAgainRect.top
h = textPlayAgainRect.top + textPlayAgainRect.height

# font for score
fontScore = pygame.font.SysFont ('arial', 20, bold=True)

# font for GameOver
fontGameOver = pygame.font.SysFont ('arial', 30, bold=True)
textGameOver = fontGameOver.render ('! GAME OVER !', True, RED)
textGameOverRect = textGameOver.get_rect()
textGameOverRect.center = (WIDTH/2, HEIGHT/2)

# font for QUIT
fontQuit = pygame.font.SysFont('arial', 20, bold=True)
textQuit = fontQuit.render('QUIT', True, RED)
textQuitRect = textQuit.get_rect()
textQuitRect.center = (WIDTH/2, HEIGHT/2 + 120)
qx = textQuitRect.left
qw = textQuitRect.left + textQuitRect.width
qy = textQuitRect.top
qh = textQuitRect.top + textQuitRect.height


# if game is not over
while not GameOver:
	# windows background
	WINDOW.fill(PINK)
	
	# if key is not pressed bird will fall	
	if keyPressed == False:
		bird.sink()
	
	# checking for the events
	for event in pygame.event.get():
		# closing window
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		# if key is pressed 
		if event.type == KEYDOWN and event.key == K_SPACE:
			keyPressed = True
		
		# if key is released the bird will again fall, reseting the up velocity
		if event.type == KEYUP:
			keyPressed = False
			bird.reset()
	# if key is pressed then bird will fly
	if keyPressed == True:
		bird.fly()
		
	# checking for update and collision with bird for each pipe in pipes list
	for pipe in pipes:
		# getting score and updating pipe(movement of pipe)
		score = pipe.update(bird)
		# checking pipe collision with bird
		if pipe.collide(bird) == True:
			GameOver = 1
			time.sleep(1)
			 
		# checking if pipe is off screen and removing off screen pipe
		if pipe.off_screen() == True:
			pipes.pop(0)
	
	# checking number of pipes, if less than three than adding one more pipe
	if len(pipes) < 3:
		gap = random.randint(200, 400)
		value = pipes[1].rectUp.left + gap
		pipes.append(PipePair(value))
	
	# score text blitted on screen with no background
	textCount = fontScore.render ('Score : ' + str (score), 1, WHITE)
	WINDOW.blit (textCount, (HEIGHT/2 - 50, 50))		
	
	
	# using fps
	clock.tick(FPS)
	pygame.display.update()
		
	while GameOver:
		WINDOW.fill(PINK)
		textCount = fontScore.render ('Score : ' + str (score), 1, WHITE)
		WINDOW.blit (textCount, (HEIGHT/2 - 50, 50))		
	
		WINDOW.blit(textPlayAgain, textPlayAgainRect)
		WINDOW.blit(textGameOver, textGameOverRect)
		WINDOW.blit(textQuit, textQuitRect)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse=pygame.mouse.get_pos()
				if mouse[0]in range (tx, w) and  mouse[1]in range(ty, h):
					reset()
														
				if mouse[0]in range (qx, qw) and  mouse[1]in range(qy, qh):
					pygame.quit()
					sys.exit()

		clock.tick(FPS)
		pygame.display.update()






