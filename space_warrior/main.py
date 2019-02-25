from Spaceship import *
from Globals import *
from Bullet import *
from Alien import *

pygame.init()

#score = 0

spaceship = Spaceship()
bullets = []
aliens = []
for n in xrange(5):
	aliens.append(Alien())

def reset():
	global score
	global spaceship
	global bullets
	global aliens
	global GameOver
	global leftKeyPressed
	global rightKeyPressed
	global bulletKey

	GameOver = False
	leftKeyPressed = False
	rightKeyPressed = False
	bulletKey = False
	if score:
		score = 0
	bullets = []
	aliens = []

	for n in xrange(10):
		aliens.append(Alien())
	
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


while not GameOver:
	WINDOW.fill(BLACK)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN and event.key == K_LEFT:
			leftKeyPressed = True

		if event.type == KEYDOWN and event.key == K_RIGHT:
			rightKeyPressed = True

		if event.type == KEYDOWN and event.key == K_SPACE:
			bulletKey = True

		if event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT):
			leftKeyPressed = False
			rightKeyPressed = False
		
		if event.type == KEYUP and event.key == K_SPACE:
			bulletKey = False

	shipCenter = spaceship.show()
	if leftKeyPressed:
		spaceship.move_left()
	if rightKeyPressed:
		spaceship.move_right()
	
	if bulletKey:
		l = len(bullets)
		if l == 0:
			bullets.append(Bullet(shipCenter))
		elif((HEIGHT-30) - bullets[l-1].Rect.top) >= 30:
			bullets.append(Bullet(shipCenter))

	for bullet in bullets:		
		bullet.update()
		if bullet.off_screen():
			bullets.pop(0)
		score = bullet.collide_aliens(aliens, bullets)

	for alien in aliens:
		alien.update()
		i = aliens.index(alien)
		if alien.off_screen():
			aliens.pop(i)

		if alien.collide_ship(spaceship):
			GameOver = True
			del aliens[:]
			time.sleep(2)
			
	if len(aliens) < 10:
		aliens.append(Alien())
		
	# score text blitted on screen with no background
	textCount = fontScore.render ('Score : ' + str (score), 1, WHITE)
	WINDOW.blit (textCount, (HEIGHT/2 - 50, 50))

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

