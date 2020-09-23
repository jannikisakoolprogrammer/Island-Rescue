from code.OtherGameObject import OtherGameObject

class MapTile(OtherGameObject):
	def __init__(self,
		_animation,
		_animation_speed,
		_pos_left,
		_pos_top,	
		_tile_char):
		super(
			MapTile,
			self).__init__(
				_animation,
				_animation_speed,
				_pos_left,
				_pos_top)
		
		self.tile_char = _tile_char
		
		