import pygame, sys, math, time
from pygame.locals import *

pygame.init()

# setting fps
fps = 30 
clock = pygame.time.Clock()

# window size
WIDTH = 500
HEIGHT = 500
PI = math.pi 

# setting mass for both the bobs
m1 = 20
m2 = 20

# angle, angular Velocity, angular acceleration
angle1 = PI/3
angle2 = PI/3

aVel1 = 0
aVel2 = 0

aAccel1 = 0
aAccel2 = 0

g = 1 

# length of string 
r1 = 100
r2 = 100 

# drawing window
WINDOW = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption ('Double Pendulum Path')

# defining colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# starting Point for the first pendulum
startX = WIDTH/2
startY = 200

# coordinate/position of first bob from starting point
m1X = startX + r1 * math.sin (angle1)
m1Y = startY + r1 * math.cos (angle1)

# coordinate/position of second bob from first bob
m2X = m1X + r2 * math.sin (angle2)
m2Y = m1Y + r2 * math.cos (angle2)


# running game loop
while True:
	WINDOW.fill(WHITE)
	pygame.draw.aaline (WINDOW, BLACK, (startX, startY), (int (m1X), int (m1Y)), 2)
	pygame.draw.aaline (WINDOW, BLACK, (int (m1X), int (m1Y)), (int (m2X), int (m2Y)), 2)
	pygame.draw.circle (WINDOW, GREEN, (startX, startY), 5, 0)
	pygame.draw.circle (WINDOW, BLUE, (int(m1X), int(m1Y)), m1/5, 0)
	pygame.draw.circle (WINDOW, RED, (int(m2X), int(m2Y)), m2/5, 0)
	
	m1X = startX + r1 * math.sin (angle1)
	m1Y = startY + r1 * math.cos (angle1)
	
	m2X = m1X + r2 * math.sin (angle2)
	m2Y = m1Y + r2 * math.cos (angle2)

	aAccel1 = (-g*(2*m1+m2)*math.sin(angle1)-m2*g*math.sin(angle1-2*angle2)-2*math.sin(angle1-angle2)*m2*(aVel2*aVel2*r2+aVel1*aVel1*r1*math.cos(angle1-angle2)))/(r1*(2*m1+m2-m2*math.cos(2*angle1-2*angle2)))

	aAccel2 = (2*math.sin(angle1-angle2)*(aVel1*aVel1*r1*(m1+m2)+g*(m1+m2)*math.cos(angle1)+aVel2*aVel2*r2*math.cos(angle1-angle2)))/(r2*(2*m1+m2-m2*math.cos(2*angle1-2*angle2)))

	
	aVel1 += aAccel1
	aVel2 += aAccel2
	angle1 += aVel1
	angle2 += aVel2

	aVel1 *= 0.999
	aVel2 *= 0.999
	
	for event in pygame.event.get ():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update ()
	clock.tick(fps)









