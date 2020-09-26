import math
import random

from code.OtherGameObject import OtherGameObject


class Bird(OtherGameObject):
	def __init__(self,
		_animation,
		_animation_speed,
		_pos_left,
		_pos_top,
		_speed,
		_direction
		):
		
		super(
			Bird,
			self).__init__(
				_animation,
				_animation_speed,
				_pos_left,
				_pos_top)
		
		self.speed = _speed
		self.direction = _direction
		
		self.move_x = math.sin(math.radians(self.direction)) * self.speed
		self.move_y = -math.cos(math.radians(self.direction)) * self.speed
	
		
		centerx = self.rect.centerx
		centery = self.rect.centery

		self.animation.rotate(-self.direction)
		
		self.rect.centerx = centerx
		self.rect.centery = centery		
	
	
	def move_by_itself(self):
		
		self.rect.move_ip(
			self.move_x,
			self.move_y)	

		self.rect.move_ip(
			random.randint(-1, 1),
			random.randint(-1, 1))
		
		if self.rect.top >= 5600:
			self.kill()
			
		if self.rect.bottom <= -200:
			self.kill()
			
		if self.animation.update() == True:
			centerx = self.rect.centerx
			centery = self.rect.centery
			self.image = self.animation.image				
			self.rect = self.animation.rect	

			self.rect.centerx = centerx
			self.rect.centery = centery
			
	
	def update(self,
		_move_left,
		_move_top,
		_helicopter,
		_map_tiles):
		
		self.rect.move_ip(
			_move_left,
			_move_top)
		
		if self.rect.colliderect(
			_helicopter.sprite.rect) == True:
				self.kill()
			
			# Reduce helicopter damage taken energ on crash
			# _helicopter.sprite.alter_damage_energy()