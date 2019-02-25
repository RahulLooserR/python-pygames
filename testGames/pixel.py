import sys, pygame
from pygame.locals import *

pygame.init ()

WINDOW = pygame.display.set_mode ((200, 200))
pygame.display.set_caption ('test')

WHITE = (255,255,255)
BLACK = (0,0,0)

i = 50
j = 50
i1 = 100
j1 = 100
pixelObj = pygame.PixelArray (WINDOW)

while True:
	WINDOW.fill (WHITE)
	#pygame.draw.line (WINDOW, BLACK, (100, 100), (100, 100), 5)
	pixelObj[i1][j1] = BLACK

	pixelObj[i][j] = BLACK
#	if i < 200 and j < 200:
#		i += 1
#		j += 1
	pygame.display.update()
