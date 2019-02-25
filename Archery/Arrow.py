from Globals import *


class Arrow:
	# 1/2 length of the arrow
	LENGTH = 50
	
	# constructor with parameters, starting point(anchorPoint), angle of projectile and velocity
	def __init__(self, anchorPoint, angle, velocity):
		self.x, self.y = anchorPoint
		self.xoffset, self.yoffset = anchorPoint
		# angle fixed for the equation
		self.angle = angle
		# variable angle for drawing line in each point (tangent)
		self.a = self.angle

		# start position for drawing 
		self.startpos = [self.x-Arrow.LENGTH*math.cos(self.a), self.y+Arrow.LENGTH*math.sin(self.a)]
		# end position for drawing line
		self.endpos = [self.x+Arrow.LENGTH*math.cos(self.a), self.y-Arrow.LENGTH*math.sin(self.a)]

		# velocity and their x and y component
		self.velocity = velocity
		self.velx = velocity * math.cos(angle)
		self.vely = velocity * math.sin(angle)
	
	def update(self):
		global GRAVITY
		global t

		# horizontal distance covered
		self.x += self.velx * t 
		# y position for given x (translating x and y with the offset)
		self.y = self.yoffset-(math.tan(self.angle)*(self.x-self.xoffset)-GRAVITY*(self.x-self.xoffset)**2/(2* self.velocity**2 * math.cos(self.angle)**2))
		
		# change in y component of velocity
		self.vely = self.vely - GRAVITY * t
		# chane in angle on projectile
		self.a = math.atan(self.vely/self.velx)

		self.startpos = [self.x-Arrow.LENGTH*math.cos(self.a), self.y+Arrow.LENGTH*math.sin(self.a)]
		self.endpos = [self.x+Arrow.LENGTH*math.cos(self.a), self.y-Arrow.LENGTH*math.sin(self.a)]
				
		# drawing anti-aliased line
		pygame.draw.aaline(WINDOW, BLACK, self.startpos, self.endpos, 6)
	
	def off_screen(self):
		return self.x > WIDTH + Arrow.LENGTH or self.y > HEIGHT + Arrow.LENGTH
