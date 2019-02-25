import time
import random
import sys
import pygame
from pygame.locals import *

# Windows height and width variable
HEIGHT = 640
WIDTH  = 640

# defining colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
PINK  = (153, 206, 255)
GREEN = ( 77, 153,   0)
GREY  = (128, 128, 128)
PURPLE = (255,  0, 102)
# frame rate for game
FPS = 45

# birds initial position
startx = 100
starty = 200

clock = pygame.time.Clock()

# setting up windows
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption('Flappy Bird')

# to check if key pressed
keyPressed = False

# game status
GameOver = False
