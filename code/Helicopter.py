import pygame
pygame.init()

import math

from code import settings
from code.Animation import Animation
from code.Timer import Timer


class Helicopter(pygame.sprite.Sprite):
	def __init__(self,
		_animation,
		_pos_x,
		_pos_y,
		_hud):
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
		
		self.hud = _hud
		
		self.turn_amount = 3
		self.angle = 0
		self.speed_x = 0
		self.speed_y = 0
		self.speed_normal = settings.HELICOPTER_SPEED_NORMAL
		self.speed_turbo = settings.HELICOPTER_SPEED_TURBO
		print(self.speed_turbo)
		self.speed = self.speed_normal
		self.go = False
		self.turn_left = False
		self.turn_right = False
		
		self.last_turn_direction = "right"
		
		# Collision rect.
		self.collision_sprite = pygame.sprite.Sprite()
		self.collision_sprite.image = pygame.Surface((20, 20))
		self.collision_sprite.image.fill((123, 123, 123))
		self.collision_sprite.rect = self.collision_sprite.image.get_rect()
		self.collision_sprite.rect.centerx = 0
		self.collision_sprite.rect.centery = 0
			
		self.collision_rect_x = 0
		self.collision_rect_y = 0
		
		# for carrying humans.
		self.rescue_humans = pygame.sprite.Group()
		
		# TODO:  Create collision rectangle for better collission detection.
		self.collission_rectangle = pygame.Rect((
			0,
			0,
			150,
			150))
			
		self.stopwatch_timer = Timer(
			settings.FPS,
			1)
			
		self.turbo = None
	
	def update(self,
		_events):

		self.process_events(_events)
		
		if self.turbo == True:
			self.speed = self.speed_turbo
			# Reduce energy.
			self.hud.reduce_energy_cloud_turbo()
		else:
			self.speed = self.speed_normal
		
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
			self.speed_x = -math.sin(math.radians(self.angle)) * self.speed
			self.speed_y = math.cos(math.radians(self.angle)) * self.speed
		else:
			self.speed_x = 0
			self.speed_y = 0
		
		if self.animation.update() == True:
			self.image = self.animation.image				
			self.rect = self.animation.rect
			
		self.rect.centerx = self.pos_x
		self.rect.centery = self.pos_y

		self.collission_rectangle.centerx = self.pos_x
		self.collission_rectangle.centery = self.pos_y

		self.update_collision_sprite()
		
		if self.stopwatch_timer.update() == True:
			self.hud.update_stopwatch()
	
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
				if e.key == pygame.K_SPACE:
					self.turbo = True


			if e.type == pygame.KEYUP:
				if e.key == pygame.K_a:
					self.turn_left = False
				if e.key == pygame.K_d:
					# Rotate right
					self.turn_right = False
				if e.key == pygame.K_w:
					self.go = False
				if e.key == pygame.K_SPACE:
					self.turbo = False

	
	def rotate(self, _degrees):

		self.animation.rotate(_degrees)

		self.rect.centerx = self.pos_x
		self.rect.centery = self.pos_y		
		
	
	def update_collision_sprite(self):	
		self.collision_sprite.rect.centerx = self.rect.centerx - (-math.sin(math.radians(self.angle)) * settings.HELICOPTER_COLLISION_RECT_DISTANCE)
		self.collision_sprite.rect.centery = self.rect.centery - math.cos(math.radians(self.angle)) * settings.HELICOPTER_COLLISION_RECT_DISTANCE
		
	
	def can_rescue_human(self):
		
		if len(self.rescue_humans) >= settings.MAX_HUMANS_BEING_CARRIED:
			return False
		else:
			return True
	
	
	def add_human(self,
		_human):
		
		self.rescue_humans.add(
			_human)
		
		self.hud.increase_humans_carrying()
	
	
	def drop_humans(self):
		
		for human in self.rescue_humans:
			human.rescued()
			self.hud.increase_humans_rescued()
			
		self.rescue_humans.empty()
		
		
	def reduce_energy(self):
		self.hud.reduce_energy_cloud_collision()
	
	
	def reduce_hitpoints(self):
		self.hud.reduce_hitpoints_bird_collision()
		
		
	def restore_hitpoints(self):
		self.hud.restore_hitpoints()		
	