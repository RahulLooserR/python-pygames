from Globals import *

# variable for score
count = 0

# class for pipe pairs
class PipePair:
	
	# initialising pipes with x position
	def __init__(self, x):	
		self.x = x
		# getting random height and gap(80) for pipe pairs
		self.height = random.randint(50, 500)
		self.rectUp = pygame.Rect(self.x, 0, 50, self.height)
		self.rectDown = pygame.Rect(self.x, self.height+80, 50, HEIGHT-self.height-40)
	
	# defining motion of pipe
	def update(self, Bird):
		# drawing uppper pipe
		pygame.draw.rect(WINDOW, BLACK, self.rectUp, 0)
		# drawing lower pipe
		pygame.draw.rect(WINDOW, BLACK, self.rectDown, 0)
		
		# moving both pipes to left
		self.rectUp.left -= 5
		self.rectDown.left -= 5
		
		self.boundary = Bird.x - self.rectUp.left - 50
		# when player scores
		if self.boundary >= 0 and self.boundary < 5:
			global count
			count += 1
			
		return count
	
	# defining collision with bird
	def collide(self, Bird):
		birdrect = pygame.Rect(Bird.x, Bird.y, Bird.height, Bird.height)
		if self.rectUp.colliderect(birdrect) or self.rectDown.colliderect(birdrect): 
			return True
		else:
			return False
			

	# defining pipe is out of screen on left
	def off_screen(self):
		if self.rectUp.left <= -50:
			return True

		return False		
