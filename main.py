import os.path

import pygame
pygame.init()


from code.Animation import Animation
from code import helpers
from code.Helicopter import Helicopter
from code import settings

#helpers.load_images("test")
#helpers.load_images(["file1", "file"])



def main():
	window = pygame.display.set_mode(
		(1680,
		1050))
		
	blue = pygame.Color(
		50,
		50,
		250)
	window.fill(blue)
	
	clock = pygame.time.Clock()
	
	path = os.path.join(
		os.getcwd(),
		"graphics")

	helicopter_surfaces = helpers.load_images(
		os.path.join(
			os.getcwd(),
			"graphics"))
			
	helicopter = pygame.sprite.GroupSingle(
		Helicopter(
			Animation(
				helicopter_surfaces,
				2),
			400,
			400))	
		
	running = True
	while running:
		
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					running = False
					
		helicopter.update()
					
		window.fill(blue)
		helicopter.draw(window)
		
		
		clock.tick(
			settings.FPS)
			
		pygame.display.update()
		
	pygame.display.quit()
		

main()