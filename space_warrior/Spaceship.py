from Globals import *

class Spaceship:
	HEIGHT = 20
	WIDTH  = 20

	def __init__(self):
		self.shipRect = pygame.Rect(WIDTH/2-Spaceship.WIDTH/2, HEIGHT-30, Spaceship.WIDTH, Spaceship.HEIGHT)
	
	def move_left(self):
		if(self.shipRect.left >= 0):
			self.shipRect.left -= 5
	
	def move_right(self):
		if(self.shipRect.left <= WIDTH-Spaceship.WIDTH):
			self.shipRect.left += 5	
	
	def show(self):
		pygame.draw.rect(WINDOW, CYAN, self.shipRect, 0)
		return self.shipRect.left + Spaceship.WIDTH/2	
