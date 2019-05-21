from Globals import *
from Arrow import *

pygame.init()

anchorPoint = [100, 400]
arrows = []
velocity = 0

while True:
	WINDOW.fill(WHITE)

	pygame.draw.aaline(WINDOW, BLACK, (100, 350), (100, 450), 2)
	pygame.draw.aaline(WINDOW, BLACK, (50, 400), (150, 400), 2)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			mouse = pygame.mouse.get_pos()
			magnitude = math.sqrt((mouse[0]-anchorPoint[0])**2 + (mouse[1]-anchorPoint[1])**2)
			
			try:
				a = ((float(mouse[1])-float(anchorPoint[1]))/(float(anchorPoint[0])-float(mouse[0])))
				angle = math.atan(a)
				print angle
			except:
				angle = math.pi/2

			if magnitude <= 80:
				velocity = magnitude * 2 
			else:
				velocity = 170
			if len(arrows) < 1:
				arrows.append(Arrow(anchorPoint, angle, velocity))

	if velocity >= 0:	
		for arrow in arrows:	
			arrow.update()
			if arrow.off_screen():
				arrows.pop(0)

	clock.tick(FPS)
	pygame.display.update()
