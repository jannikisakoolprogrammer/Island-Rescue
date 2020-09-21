import pygame
pygame.init()

from code import settings
from code.Timer import Timer
import copy


class Animation(pygame.sprite.Sprite):
	def __init__(self,
		_surfaces,
		_update_interval = settings.FPS / settings.FPS):
		
		self.surfaces = _surfaces
		self.orig_surfaces = copy.copy(_surfaces)
		
		if _update_interval > settings.FPS:
			self.update_interval = settings.FPS
		else:
			self.update_interval = _update_interval
		
		self.timer = Timer(
			self.update_interval,
			1)
		
		
		self.cur_surface_idx = 0
		self.max_surface_idx = len(self.surfaces) - 1
		self.set_next_surface()
		
		
	def update(self):
		
		if self.timer.update() == True:
			self.update_cur_surface_idx()
			self.set_next_surface()
			
			return True
		
		else:
			return False
	
	
	def update_cur_surface_idx(self):
	
		if self.cur_surface_idx >= self.max_surface_idx:
			self.cur_surface_idx = 0
			
		else:
			self.cur_surface_idx += 1
		
	
	def set_next_surface(self):
	
		self.image = self.surfaces[self.cur_surface_idx]
		self.rect = self.image.get_rect()
	
	
	def rotate(self,
		_direction):
		
		for x in range(len(self.orig_surfaces)):
			new_surface = pygame.transform.rotate(
				self.orig_surfaces[x],
				_direction)
			self.surfaces[x] = new_surface
	
	
	def reverse(self):
		self.surfaces.reverse()
		self.orig_surfaces.reverse()
		
		