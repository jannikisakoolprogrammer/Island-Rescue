import os
import string

import pygame
pygame.init()

from code.MapTile import MapTile
from code.Animation import Animation
from code import helpers
from code import settings

class Map(pygame.sprite.Sprite):
	def __init__(self,
		_layout): # Layout of the map.
		super(
			Map,
			self).__init__()
		
		self.layout = _layout
		
		
		self.update_group = pygame.sprite.Group()
		self.update_draw_group = pygame.sprite.Group()
		
		island_center_1_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_center1.png"))
				
		island_center_2_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_center2.png"))

		island_water_right_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_right.png"))	
				
		island_water_right_image2 = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_right2.png"))				

		island_water_left_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_left.png"))	
				
		island_water_left_image2 = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_left2.png"))					

		island_water_top_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_top.png"))	
				
		island_water_top_image2 = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_top2.png"))				

		island_water_bottom_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_bottom.png"))	
				
		island_water_bottom_image2 = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_bottom2.png"))					

		island_water_top_left_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_top_left.png"))	

		island_water_top_right_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_top_right.png"))	

		island_water_bottom_right_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_bottom_right.png"))	

		island_water_bottom_left_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_water_bottom_left.png"))
				
		island_bar = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"island_bar.png"))				
				
		water_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"water.png"))				
		
		# Create map here (iterate rows, columns)
		cnt = 0
		left = top = 0

		for row in self.layout:
			for column in row.strip():
				print(column)
				# Create animation.
				if column == "1":						
					animation = Animation(island_center_1_image)
				if column == "2":						
					animation = Animation(island_center_2_image)
				if column == "3":						
					animation = Animation(island_water_right_image)
				if column == "4":						
					animation = Animation(island_water_left_image)
				if column == "5":						
					animation = Animation(island_water_top_image)
				if column == "6":						
					animation = Animation(island_water_bottom_image)
				if column == "7":						
					animation = Animation(island_water_top_left_image)
				if column == "8":						
					animation = Animation(island_water_top_right_image)
				if column == "9":						
					animation = Animation(island_water_bottom_right_image)
				if column == "0":						
					animation = Animation(island_water_bottom_left_image)
				if column == "a":						
					animation = Animation(island_water_top_image2)
				if column == "b":						
					animation = Animation(island_water_bottom_image2)
				if column == "c":						
					animation = Animation(island_water_left_image2)
				if column == "d":						
					animation = Animation(island_water_right_image2)
				if column == "e":						
					animation = Animation(island_bar)
				if column == "f":						
					animation = Animation(water_image)									

				# Create maptile, passing the animation instance to it.
				self.update_group.add(
					MapTile(
						animation,
						1,
						left,
						top,
						column))
						
				left += settings.MAP_TILE_WIDTH
	
			left = 0
			top += settings.MAP_TILE_HEIGHT
	
		self.image = pygame.Surface((
			settings.WINDOW_WIDTH,
			settings.WINDOW_HEIGHT))
		self.rect = self.image.get_rect()
			
			