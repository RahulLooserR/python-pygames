import pygame, sys
from pygame.locals import *

pygame.init()
WINDOW = pygame.display.set_mode ((500, 500))
pygame.display.set_caption ('Font')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)

fontObj = pygame.font.Font ('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render ('Hello World !', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 200)

while True:
	WINDOW.fill (WHITE)
	WINDOW.blit (textSurfaceObj, textRectObj)

	for event in pygame.event.get ():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update ()

