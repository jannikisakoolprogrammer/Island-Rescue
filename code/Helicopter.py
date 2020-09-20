import pygame
pygame.init()


from code.Animation import Animation


class Helicopter(pygame.sprite.Sprite):
	def __init__(self,
		_animation,
		_pos_x,
		_pos_y,):
		super(
			Helicopter,
			self).__init__()
		
		self.animation = _animation
			
		self.image = self.animation.image
		self.rect = self.animation.rect
		
		self.pos_x = _pos_x
		self.pos_y = _pos_y
		
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y
		
	
	def update(self,
		_events):

		self.process_events(_events)
		
		if self.animation.update() == True:
			self.image = self.animation.image
			self.rect = self.animation.rect
			
			self.rect.x = self.pos_x
			self.rect.y = self.pos_y
	
	
	def process_events(self,
		_events):
		
		pass