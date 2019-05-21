import time
import random
import sys
import pygame
from pygame.locals import *
from pygame import gfxdraw

# Windows height and width variable
HEIGHT = 640
WIDTH  = 640

SIZE = 64

# defining colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
PINK  = (153, 206, 255)
GREEN = ( 77, 153,   0)
GREY  = (128, 128, 128)
PURPLE = (255,  0, 102)

colors = (WHITE, BLACK, RED, PINK, GREEN, GREY, PURPLE)

# frame rate for game
FPS = 45

clock = pygame.time.Clock()

# setting up windows
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption('Mines')

# game status
GameOver = False

