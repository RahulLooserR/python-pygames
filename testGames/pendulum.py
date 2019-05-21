import pygame, sys, math, time
from pygame.locals import *


pygame.init()

# Windows setting
WIDTH = 500
HEIGHT = 500

# setting colors
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# setting starting point of string
startX = WIDTH/2
startY = 50

fps = 30
fpsClock = pygame.time.Clock()

# varibles required for pendulum
PI = math.pi

MASS = 20
LENGTH = 200
angle = PI/3 
g = 9.8
aVel = 0
aAccel = 0
mX = startX + LENGTH * math.sin (angle)
mY = startY + LENGTH * math.cos (angle)


# setting windows size
WINDOW = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption ('Pendulum Motion')
#pixObj = []
#i = 0
#WINDOW.fill (WHITE)

while True:
	WINDOW.fill (WHITE)
	pygame.draw.circle (WINDOW, GREEN, (startX, startY), 5, 1)
	pygame.draw.aaline (WINDOW, BLACK, (startX, startY), (mX, mY), 1)
	pygame.draw.circle (WINDOW, BLUE, (int (mX), int (mY)), 10, 0)
 	
	mX = startX + LENGTH * math.sin (angle)
	mY = startY + LENGTH * math.cos (angle)
#	pixObj[i] =  pygame.PixelArray (WINDOW)
#	blit(mX, mY, area=None, special_flags = 0) -> Rect
	aAccel = -0.01 * math.sin (angle)
	angle += aVel
	aVel += aAccel
	aVel *= 0.99

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick (10)
