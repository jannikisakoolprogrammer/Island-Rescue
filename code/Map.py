from code.MapTile import MapTile

class Map(pygame.sprite.Group):
	def __init__(self,
		_layout): # Layout of the map.
		super(
			Map,
			self).__init__()
		
		self.layout = _layout
		
		# Create map here (iterate rows, columns)
		left = top = 0
		for row in self.layout:
			for column in row:
				# Create animation.
				# Create maptile, passing the animation instance to it.
				self.add(
					MapTile(
						animation,
						animation_speed,
						left,
						top,
						column))
				left += 50
			left = 0
			top += 50