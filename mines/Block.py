# ########################################################################
# Created by    : Rahul Kumar Nonia
# File name     : Block.py
# Created on    : 20-05-2019
# Last modified : Tuesday 21 May 2019 04:09:39 PM IST
# Description   : 
# ########################################################################

from Globals import *
MINES = 20
#global GameOver
class Block:
	
	def __init__(self, x, y, nr):
		self.x = x
		self.y = y
		self.height =  SIZE
		self.width = SIZE
		self.random = random.randint(0, 11)
		self.mine = 0
		
		if self.random in range(0, 3):
			self.mine = 1
			print MINES

		self.count = 0
		self.color = GREY 
		self.nr = nr
		self.Rect = pygame.Rect(self.x, self.y, SIZE, SIZE)

		self.font = pygame.font.SysFont('arial', 10, bold=True)
		self.text = self.font.render(str(self.count), True, BLACK)
		
		self.revealed = False
			
	def draw(self):
		pygame.draw.rect(WINDOW, self.color, self.Rect, 0)
		if self.mine == 1 and self.revealed == True:
			pygame.gfxdraw.aacircle(WINDOW, self.x + SIZE/2, self.y + SIZE/2, 15, BLACK)
			pygame.gfxdraw.filled_circle(WINDOW, self.x + SIZE/2, self.y + SIZE/2, 15, BLACK)
		
		if self.revealed == True: 	
			WINDOW.blit(self.text, (self.x+SIZE/2, self.y+SIZE/2))


	def isRevealed(self, mouse):

		if mouse[0] in range(self.x, self.x+SIZE) and mouse[1] in range(self.y, self.y + SIZE) and self.revealed == False:
			self.color = WHITE
			self.draw()
			self.revealed = True
						
		if self.mine == 1 and self.revealed == True:
			return True 
		
		return False

	def getCount(self, blocks):
		if self.mine == 0:
			for block in blocks:
				if block.nr[0] in range(self.nr[0]-1, self.nr[0]+2) and block.nr[1] in range(self.nr[1]-1, self.nr[1]+2) and block.mine == 1:
					self.count += 1
		
		self.font = pygame.font.SysFont('arial', 10, bold=True)
		self.text = self.font.render(str(self.count), True, BLACK)
