import math

from code.OtherGameObject import OtherGameObject


class Cloud(OtherGameObject):
	def __init__(self,
		_animation,
		_animation_speed,
		_pos_left,
		_pos_top,
		_speed,
		_direction
		):
		
		super(
			Cloud,
			self).__init__(
				_animation,
				_animation_speed,
				_pos_left,
				_pos_top)
		
		self.speed = _speed
		self.direction = _direction
		
		self.move_x = math.sin(math.radians(self.direction)) * self.speed
		self.move_y = -math.cos(math.radians(self.direction)) * self.speed
	
	
	def move_by_itself(self):
		
		self.rect.move_ip(
			self.move_x,
			self.move_y)			
		
		if self.rect.top >= 5600:
			self.kill()
			
	
	def update(self,
		_move_left,
		_move_top,
		_helicopter,
		_map_tiles):
		
		self.rect.move_ip(
			_move_left,
			_move_top)
		
		if self.rect.colliderect(
			_helicopter.sprite.collission_rectangle) == True:
				_helicopter.sprite.reduce_energy()