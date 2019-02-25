# animation.py : animation program

import sys, pygame, time
from pygame.locals import *

# init
pygame.init()

# window
WIDTH = 500
HEIGHT = 500
windowSurface = pygame.display.set_mode ((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption ('Animation')

# movespeed
MOVESPEED = 4

# directions
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the box data structure.
b1 = {'rect':pygame.Rect(450, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(250, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# gameloop
while True:
	# checking for quit event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

# Draw the white background onto the surface.
	windowSurface.fill(WHITE)
	
	for b in boxes:
# Move the box data structure.
		if b['dir'] == DOWNLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == DOWNRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top += MOVESPEED
		if b['dir'] == UPLEFT:
			b['rect'].left -= MOVESPEED
			b['rect'].top -= MOVESPEED
		if b['dir'] == UPRIGHT:
			b['rect'].left += MOVESPEED
			b['rect'].top -= MOVESPEED
# Check whether the box has moved out of the window.
		if b['rect'].top < 0:
# The box has moved past the top.
			if b['dir'] == UPLEFT:
				b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
				b['dir'] = DOWNRIGHT

		if b['rect'].bottom > HEIGHT:
# The box has moved past the bottom.
			if b['dir'] == DOWNLEFT:
				b['dir'] = UPLEFT
			if b['dir'] == DOWNRIGHT:
				b['dir'] = UPRIGHT
		if b['rect'].left < 0:
# The box has moved past the left side.
			if b['dir'] == DOWNLEFT:
				b['dir'] = DOWNRIGHT
			if b['dir'] == UPLEFT:
				b['dir'] = UPRIGHT
		if b['rect'].right > WIDTH:
# The box has moved past the right side.
			if b['dir'] == DOWNRIGHT:
				b['dir'] = DOWNLEFT
			if b['dir'] == UPRIGHT:
				b['dir'] = UPLEFT
# Draw the box onto the surface.
		pygame.draw.rect(windowSurface, b['color'], b['rect'])
# Draw the window onto the screen.
	pygame.display.update()
	time.sleep(0.01)
















	
