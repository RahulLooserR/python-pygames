from Globals import *

class Alien:
	POWER = 0
	WIDTH = 10
	

	def __init__(self):
		self.color = random.randint(0,3)
		self.x = random.randint(0, WIDTH-Alien.WIDTH) 
		self.y = -100
		self.Rect = pygame.Rect(self.x, self.y, Alien.WIDTH, Alien.WIDTH)
		self.speed = random.randint(2, 5)

		if color == 0:
			Alien.POWER = 20

		if color == 1:
			Alien.POWER = 40

		if color == 2:
			Alien.POWER = 60

		if color == 3:
			Alien.POWER = 80
	

	def update(self):
		pygame.draw.rect(WINDOW, COLOR[self.color], self.Rect, 0)
		self.Rect.top += self.speed

	def collide_ship(self, ship):
		return self.Rect.colliderect(ship.shipRect)

	def off_screen(self):
		return self.Rect.top >= HEIGHT+Alien.WIDTH


