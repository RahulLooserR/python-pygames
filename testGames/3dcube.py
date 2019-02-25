import pygame
from pygame.locals import *
from sys import exit
from math import *
from random import randint

from gameobjects import Vector3


### game setup
SCREEN_SIZE = (640, 480)
COUNT = 300
CUBE_SIZE = 300


# calculating distance using field of view
def calculate_viewing_distance (fov, scree_width):
	return ((screen_width / 2.0) / tan (fov / 2.0))

# game initialisation

def run ():
	pygame.init()
	screen = pygame.display.set_mode (SCREEN_SIZE, 0)

	default_font = pygame.font.get_default_font ()
	font = pygame.SysFont (default_font, 24)
	
	# 3d points
	points = []

	fov = 90.
	viewing_distance = calculate_viewing_distance (radians (fov), SCREEN_SIZE[0])

	# creating a list of points along the edge of cube 
	for x in xrange (0, CUBE_SIZE+1, 20):
		edge_x = x == 0 or x == CUBE_SIZE

		for y in xrange (0, CUBE_SIZE+1, 20):
			edge_y = y == 0 or y == CUBE_SIZE
			
			for z in xrange (0, CUBE_SIZE+1, 20):
				edge_z = z == 0 or z == CUBE_SIZE

				if sum (( edge_x, edge_y, edge_z)) >= 2:
					point_x = float (x) - CUBE_SIZE/2
					point_y = float (y) - CUBE_SIZE/2
					point_z = float (z) - CUBE_SIZE/2

					points.append (Vector3 (point_x, point_y, point_z))

	# sort points in z order
	def point_z (point):
		return point.z

