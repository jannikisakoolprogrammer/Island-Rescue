import pygame
pygame.init()

from code import settings


class OtherGameObject(pygame.sprite.Sprite):
	def __init__(self,
		_animation,
		_animation_speed,
		_pos_left,
		_pos_top
		):
		super(
			OtherGameObject,
			self).__init__()
		
		self.animation = _animation
		self.animation_speed = _animation_speed
		self.pos_left = _pos_left
		self.pos_top = _pos_top
		
		self.image = self.animation.image
		self.rect = self.image.get_rect()
		self.rect.left = self.pos_left
		self.rect.top = self.pos_top
		
	
	def update(self,
		_move_left,
		_move_top,
		_update_draw_group):
		
		self.rect.move_ip(
			_move_left,
			_move_top)
		
		if self.rect.right < -settings.MAP_TILE_WIDTH \
		   or self.rect.left > settings.WINDOW_WIDTH + settings.MAP_TILE_WIDTH \
		   or self.rect.bottom > settings.WINDOW_HEIGHT + settings.MAP_TILE_HEIGHT \
		   or self.rect.top < -settings.MAP_TILE_HEIGHT:
			self.remove(_update_draw_group)
		else:
			if not self in _update_draw_group:					
				
				self.add(_update_draw_group)				
			
		
		
	