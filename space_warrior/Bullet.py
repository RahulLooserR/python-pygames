from Globals import *

#count = 0

class Bullet:
	POWER = 20
	def __init__(self, center):
		self.Rect = pygame.Rect(center-2, HEIGHT-30, 4, 10)
	
	def update(self):
		self.Rect.top -= 10
		pygame.draw.rect(WINDOW, GREEN,  self.Rect, 0)

	def off_screen(self):
		if self.Rect.top < -100:
			return True
		return False

	def collide_aliens(self, aliens, bullets):
		global score
		for alien in aliens:
			if self.Rect.colliderect(alien.Rect):
				i = aliens.index(alien)
				j = bullets.index(self)
				aliens.pop(i)
				bullets.pop(j)
	
				score += 1
		

		return score
