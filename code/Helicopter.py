import pygame
pygame.init()

import math


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
		
		self.rect.x = self.pos_x
		self.rect.y = self.pos_y
		
		self.turn_amount = 2
		self.angle = 0
		self.speed_x = 0
		self.speed_y = 0
		self.max_speed = 5
		self.go = False
		self.turn_left = False
		self.turn_right = False
		
		self.last_turn_direction = "right"
		
	
	def update(self,
		_events):

		self.process_events(_events)
		
		if self.turn_left == True:
			self.angle -= self.turn_amount
			if self.angle < 0:
				self.angle = 360 - self.turn_amount
			self.rotate(360 - self.angle)

		if self.turn_right == True:
			self.angle += self.turn_amount
			if self.angle > 360:
				self.angle = self.turn_amount
			self.rotate(-self.angle)

		if self.go == True:
			self.speed_x = -math.sin(math.radians(self.angle)) * self.max_speed
			self.speed_y = math.cos(math.radians(self.angle)) * self.max_speed
		else:
			self.speed_x = 0
			self.speed_y = 0
		
		if self.animation.update() == True:
			self.image = self.animation.image				
			self.rect = self.animation.rect
			
		self.rect.centerx = self.pos_x
		self.rect.centery = self.pos_y		
	
	
	def process_events(self,
		_events):
		
		for e in _events:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_a:
					if self.last_turn_direction is not "left":
						self.animation.reverse()
					self.turn_left = True
					self.last_turn_direction = "left"
				if e.key == pygame.K_d:
					if self.last_turn_direction is not "right":
						self.animation.reverse()
					self.turn_right = True
					self.last_turn_direction = "right"
				if e.key == pygame.K_w:
					self.go = True


			if e.type == pygame.KEYUP:
				if e.key == pygame.K_a:
					self.turn_left = False
				if e.key == pygame.K_d:
					# Rotate right
					self.turn_right = False
				if e.key == pygame.K_w:
					self.go = False				



					
	
	def rotate(self, _degrees):

		self.animation.rotate(_degrees)

		self.rect.centerx = self.pos_x
		self.rect.centery = self.pos_y		