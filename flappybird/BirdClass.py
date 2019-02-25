from Globals import *


# Class for bird
class Bird:
	# defining gravity with which bird will fall
	gravity = 0.5  
	# flying power of bird (anti-gravity)
	flyPower = -0.8
	
	# up velocity(flying) and down velocity(falling)
	upVel = 0
	downVel = 0
	
	# bird height and width
	height = 10
	
	# constructor for initialising bird position
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# definging falling of bird
	def sink(self):		
		# drawing circle (bird)
		pygame.draw.circle(WINDOW, PURPLE, (int(self.x), int(self.y)), Bird.height, 0)
		if self.y <= 630:
			Bird.downVel += Bird.gravity
			self.y += Bird.downVel 
	
	# defining flying of bird
	def fly(self):
		Bird.downVel = 0	
		pygame.draw.circle(WINDOW, PURPLE, (int(self.x), int(self.y)), Bird.height, 0)
		if self.y >= 10:
			Bird.upVel += Bird.flyPower
			self.y += Bird.upVel
	
	# resetting velocities when key is released
	def reset(self):
		Bird.upVel = 0
		Bird.downVel = 0

