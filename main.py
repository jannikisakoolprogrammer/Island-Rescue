import os.path

import pygame
pygame.init()


from code.Animation import Animation
from code import helpers
from code.Helicopter import Helicopter
from code import settings
from code.Map import Map

#helpers.load_images("test")
#helpers.load_images(["file1", "file"])



def main():
	window = pygame.display.set_mode(
		(settings.WINDOW_WIDTH,
		settings.WINDOW_HEIGHT),
		pygame.FULLSCREEN)
		
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
			"graphics",
			"helicopter"))
			
	helicopter = pygame.sprite.GroupSingle(
		Helicopter(
			Animation(
				helicopter_surfaces,
				0),
			settings.WINDOW_WIDTH // 2,
			settings.WINDOW_HEIGHT // 2))
			
	map = Map(
		open(
			os.path.join(
				os.getcwd(),
				"map",
				"map.txt")))
		
	running = True
	while running:
		
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					running = False
					
		map.update(
			helicopter.sprite.speed_x,
			helicopter.sprite.speed_y,
			helicopter)
		helicopter.update(events)
					
		window.fill(blue)
		map.update_draw_group.draw(window)		
		helicopter.draw(window)
		
		clock.tick(
			settings.FPS)
			
		pygame.display.update()
		
	pygame.display.quit()
		

main()