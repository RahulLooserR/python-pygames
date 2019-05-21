# ########################################################################
# Created by    : Rahul Kumar Nonia
# File name     : main.py
# Created on    : 20-05-2019
# Last modified : Tuesday 21 May 2019 03:40:15 PM IST
# Description   : 
# ########################################################################


from Block import *
from Globals import *

pygame.init()

blocks = []

# number of blocks
nr_blocks = WIDTH/SIZE * HEIGHT/SIZE

x = 0
y = 0

# appending block in blocks
for i in range(WIDTH/SIZE):
	x = 0
	for j in range (HEIGHT/SIZE):
		blocks.append(Block(x, y, (i, j)))
		x += SIZE
	
	y += SIZE

# getting count of mines for each block
for block in blocks:
	block.getCount(blocks)	

# drawing lines between blocks 
def drawlines():
	lx = 0
	ly = 0
	for i in range(WIDTH/SIZE):
		pygame.draw.aaline(WINDOW, BLACK, [lx, ly+SIZE], [WIDTH, ly+SIZE])
		ly += SIZE
	lx = 0
	ly = 0	
	for i in range(HEIGHT/SIZE):
		pygame.draw.aaline(WINDOW, BLACK, [lx+SIZE, ly], [lx+SIZE, HEIGHT])
		lx += SIZE

unRevealedBlocks = 0
mines = 0

for block in blocks:
	if block.mine == 1:
		mines += 1

#mouse = pygame.mouse.get_pos()
while not GameOver:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	  		sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			mouse = pygame.mouse.get_pos()

			for block in blocks:
				result = block.isRevealed(mouse)
				if result == True:
					GameOver = True

	for block in blocks:
		block.draw()
	
	drawlines()

	if mines == unRevealedBlocks:
		GameOver = True
	
	clock.tick(FPS)
	pygame.display.update()

# font for game over
font = pygame.font.SysFont('arial', 50, bold=True)
text = font.render("Game Over", True, RED)
textRect = text.get_rect()
textRect.center = (WIDTH/2, HEIGHT/2)

while GameOver:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	  		sys.exit()
	
	for block in blocks:
		block.revealed = True

	for block in blocks:
		block.draw()

	drawlines()
	WINDOW.blit(text, textRect)
	
	clock.tick(FPS)
	pygame.display.update()
