import pygame, sys, time
from pygame.locals import *
import random
import math


# colors
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
CYAN  = (  0, 255, 255)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
PINK  = (153, 206, 255)
COLOR = (RED, GREEN, WHITE, BLUE)


WIDTH  = 640
HEIGHT = 640

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ARROW')

FPS = 30
clock = pygame.time.Clock()

GameOver = False
leftKeyPressed = False
rightKeyPressed = False
bulletKey = False

score = 0

GRAVITY = 9 
t = 0.15
