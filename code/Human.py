from code.OtherGameObject import OtherGameObject
from code import helpers


class Human(OtherGameObject):
	def __init__(self,
		_animation,
		_animation_speed,
		_pos_left,
		_pos_top,
		_landing_zone_rect
		):
		
		super(
			Human,
			self).__init__(
				_animation,
				_animation_speed,
				_pos_left,
				_pos_top)
		
		self.landing_zone_rect = _landing_zone_rect
		self.distance_to_landing_zone = helpers.calc_distance_in_px(
			self.rect,
			self.landing_zone_rect)
		
		self.is_rescued = False
		
	
	def update(self,
		_move_left,
		_move_top,
		_helicopter):
		
		self.rect.move_ip(
			_move_left,
			_move_top)
		
		if self.rect.colliderect(
			_helicopter.sprite.collission_rectangle) == True \
			and _helicopter.sprite.can_rescue_human() == True:
			
			# Human has been picked up the helicopter.  Hinder drawing.
			self.kill()
			
			# TODO:  Add human to Helicopter for counting.  Max 3 persons
			# can be carried at a time.
			_helicopter.sprite.add_human(self)
	
	
	def rescued(self):
		# Stop timer.
		# TODO
		
		self.is_rescued = True