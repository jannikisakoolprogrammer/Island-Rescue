import os.path
import random
import math
import copy

import pygame
pygame.init()


from code.Animation import Animation
from code import helpers
from code.Helicopter import Helicopter
from code import settings
from code.Map import Map
from code.Human import Human
from code.Cloud import Cloud
from code.Bird import Bird


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
		
	helicopter = create_helicopter()
	map = create_map()
	humans = create_humans(map.update_group)
	clouds = pygame.sprite.Group()
	birds = pygame.sprite.Group()
	
	cloud_animations = []
	cloud_animations.append(
		Animation(
			helpers.load_images(
				os.path.join(
					os.getcwd(),
					"graphics",
					"clouds",
					"cloud1.png")),
			100))
	cloud_animations.append(
		Animation(
			helpers.load_images(
				os.path.join(
					os.getcwd(),
					"graphics",
					"clouds",
					"cloud2.png")),
			100))
	cloud_animations.append(
		Animation(
			helpers.load_images(
				os.path.join(
					os.getcwd(),
					"graphics",
					"clouds",
					"cloud3.png")),
			100))
	cloud_animations.append(
		Animation(
			helpers.load_images(
				os.path.join(
					os.getcwd(),
					"graphics",
					"clouds",
					"cloud4.png")),
			100))


		
	running = True
	while running:
	
		if random.randint(1, 100) == 50:
			if len(clouds) <= 50:
				clouds.add(
					create_cloud(
						cloud_animations))
					
		if random.randint(1, 50) == 25:
			if len(birds) <= 100:
				birds.add(
					create_bird())					
		
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					running = False
		
		# Clouds always move.
		for cloud in clouds:			
			cloud.move_by_itself()
			
		# Birds always move.
		for bird in birds:			
			bird.move_by_itself()			
					
		if map.update(
			helicopter.sprite.speed_x,
			helicopter.sprite.speed_y,
			helicopter):
			# Map was moved, so can other game objects.
			# TODO:  Add humans, birds, clouds, ... here.
			humans.update(
				helicopter.sprite.speed_x,
				helicopter.sprite.speed_y,
				helicopter)	

			clouds.update(
				helicopter.sprite.speed_x,
				helicopter.sprite.speed_y,
				helicopter,
				map.update_group)
				
			birds.update(
				helicopter.sprite.speed_x,
				helicopter.sprite.speed_y,
				helicopter,
				map.update_group)
							
			
		helicopter.update(events)
					
		window.fill(blue)
		map.update_draw_group.draw(window)	
		humans.draw(window)
		birds.draw(window)		
		helicopter.draw(window)
		clouds.draw(window)
		
		clock.tick(
			settings.FPS)
			
		pygame.display.update()
		
	pygame.display.quit()
	

def create_helicopter():

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
			
	return helicopter
	
	
def create_map():

	map = Map(
		open(
			os.path.join(
				os.getcwd(),
				"map",
				"map.txt")))
				
	return map
	
	
def create_humans(
	map_tiles):

	humans = pygame.sprite.Group()
	
	invalid_tile_chars = ("f", "g", "h")
	# Get all map tiles where humans can be put

	valid_map_tiles = [x for x in map_tiles if x.tile_char not in invalid_tile_chars]
	
	for x in map_tiles:
		if x.tile_char == "g":
			landing_zone_rect = x.rect
			break
	
	human_animations = []
	humans_path = os.path.join(
		os.getcwd(),
		"graphics",
		"humans")
					
	human_animations.append(
			helpers.load_images(
				os.path.join(
					humans_path,
					"human1.png")))
					
	human_animations.append(
			helpers.load_images(
				os.path.join(
					humans_path,
					"human2.png")))

	human_animations.append(
			helpers.load_images(
				os.path.join(
					humans_path,
					"human3.png")))					
	
	for x in range(settings.N_HUMANS):
		random_map_tile = random.choice(
			valid_map_tiles)
		
		random_x = random.randint(
			random_map_tile.rect.left,
			random_map_tile.rect.right)
			
		random_y = random.randint(
			random_map_tile.rect.top,
			random_map_tile.rect.bottom)
			
		humans.add(
			Human(
				Animation(random.choice(human_animations)),
				1,
				random_x,
				random_y,
				landing_zone_rect))
	
	return humans


def create_cloud(_cloud_animations):
	direction = random.randint(140, 220)
	speed = random.randint(3, 8)
	
	start_x = random.randint(0, settings.WINDOW_WIDTH)
	start_y = random.randint(-600, -500)
	
	cloud_animation = random.choice(_cloud_animations)
	
	cloud = Cloud(
		cloud_animation,
		1,
		start_x,
		start_y,
		speed,
		direction)
		
	return cloud


def create_bird():

	speed = random.randint(3, 7)
	
	start_x = random.choice((
		random.randint(
			-100,
			-50),
		random.randint(	
			settings.WINDOW_WIDTH + 50,
			settings.WINDOW_WIDTH + 100)))
			
	start_y = random.choice((
		random.randint(
			-100,
			-50),
		random.randint(
			settings.WINDOW_HEIGHT + 50,
			settings.WINDOW_HEIGHT + 100)))	
			
	if start_y < 0:
		direction = random.randint(100, 250)
		
	else:
		direction = random.randint(290, 430)
		if direction >= 360:
			direction -= 360
		
	bird_animation = Animation(
			helpers.load_images(
				os.path.join(
					os.getcwd(),
					"graphics",
					"bird")),
			settings.FPS)
	
	bird = Bird(
		copy.copy(bird_animation),
		settings.FPS,
		start_x,
		start_y,
		speed,
		direction)
		
	return bird

main()