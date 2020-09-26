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
		self.landing_zone = None
		
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

		landing_zone_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"landing_zone.png"))	

		city_image = helpers.load_images(
			os.path.join(
				os.getcwd(),
				"graphics",
				"map",
				"city.png"))					
		
		# Create map here (iterate rows, columns)
		cnt = 0
		left = top = 0
		w = len(self.layout.readlines()[0].strip()) * settings.MAP_TILE_WIDTH
		self.layout.seek(0)
		
		for row in self.layout:
			for column in row.strip():
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
				if column == "g":
					animation = Animation(landing_zone_image)
				if column == "h":
					animation = Animation(city_image)

				# Create maptile, passing the animation instance to it.
				map_tile = MapTile(
						animation,
						1,
						left,
						top,
						column)
						
				if map_tile.tile_char == "g":
					self.landing_zone = map_tile
					
				self.update_group.add(map_tile)
						
				left += settings.MAP_TILE_WIDTH
	
			left = 0
			top += settings.MAP_TILE_HEIGHT

		h = top

		h -= settings.MAP_TILE_HEIGHT * 4
		w -= settings.MAP_TILE_WIDTH * 6
		self.image = pygame.Surface((
			w,
			h))
		self.rect = self.image.get_rect()	
		self.rect.top = settings.MAP_TILE_HEIGHT * 2
		self.rect.left = settings.MAP_TILE_WIDTH * 3
		# Set starting pos
		start_x = -(w / 2) - settings.MAP_TILE_WIDTH
		start_y = -h
		self.rect.move_ip(
			start_x,
			start_y)
			
		self.update_group.update(
			start_x,
			start_y,
			self.update_draw_group)
				
		
	def update(self,
		_move_left,
		_move_top,
		_helicopter):
		
		if self.rect.colliderect(
			_helicopter.sprite.collision_sprite.rect):
			
			self.refresh(
				_move_left,
				_move_top)
				
			# If helicopter carries humans, and is at the landing platform,
			# drop those humans, so the helicopter can rescue more humans.
			if self.landing_zone.rect.colliderect(
				_helicopter.sprite.rect):
				_helicopter.sprite.drop_humans()
			
			return True
			
		else:
			return False
			
	
	def refresh(self,
		_move_left,
		_move_top):
		
		self.rect.move_ip(
			_move_left,
			_move_top)
			
		self.update_group.update(
			_move_left,
			_move_top,
			self.update_draw_group)		
				
			