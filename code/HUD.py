import pygame
pygame.init()

import datetime

from code import settings


class HUD(object):
	def __init__(self,
		_helicopter_hitpoints,
		_helicopter_energy,
		_humans_rescued,
		_humans_carrying,
		_stopwatch):
		
		self.helicopter_hitpoints = _helicopter_hitpoints
		self.helicopter_energy = _helicopter_energy
		self.humans_rescued = _humans_rescued
		self.humans_carrying = _humans_carrying
		self.stopwatch = _stopwatch
		
		self.helicopter_hitpoints_max = _helicopter_hitpoints
		self.helicopter_energy_max = _helicopter_energy
		self.humans_rescued_max = settings.N_HUMANS
		self.humans_carrying_max = settings.MAX_HUMANS_BEING_CARRIED
		
		self.helicopter_hitpoints_text = "Hitpoints: %f / %f"
		self.helicopter_energy_text = "Energy: %f / %f"
		self.humans_rescued_text = "Humans rescued: %d / %d"
		self.humans_carrying_text = "Humans carrying: %d / %d"
		self.stopwatch_text = "Stopwatch: %H:%M:%S"
		
		self.helicopter_hitpoints_sprite = pygame.sprite.Sprite()
		self.helicopter_energy_sprite = pygame.sprite.Sprite()
		self.humans_rescued_sprite = pygame.sprite.Sprite()
		self.humans_carrying_sprite = pygame.sprite.Sprite()
		self.stopwatch_sprite = pygame.sprite.Sprite()

		
		# Font.
		self.font = pygame.font.SysFont(
			"monospace",
			20,
			True)
			
		self.fg_colour = pygame.Color(0, 0, 0)
		self.bg_colour = pygame.Color(255, 255, 255)
		
		self.update_helicopter_hitpoints_text()
		self.update_helicopter_energy_text()
		self.update_humans_rescued_text()		
		self.update_humans_carrying_text()
		self.update_stopwatch_text()
	
	def update_helicopter_hitpoints_text(self):
	
		self.helicopter_hitpoints_sprite.image = self.font.render(
			self.helicopter_hitpoints_text % (
				self.helicopter_hitpoints,
				self.helicopter_hitpoints_max),
				True,
				self.fg_colour,
				self.bg_colour)			
		
		self.helicopter_hitpoints_sprite.rect = self.helicopter_hitpoints_sprite.image.get_rect()
		self.helicopter_hitpoints_sprite.rect.left = 50
		self.helicopter_hitpoints_sprite.rect.top = 50
		
		
	def update_helicopter_energy_text(self):
	
		self.helicopter_energy_sprite.image = self.font.render(
			self.helicopter_energy_text % (
				self.helicopter_energy,
				self.helicopter_energy_max),
				True,
				self.fg_colour,
				self.bg_colour)			
		
		self.helicopter_energy_sprite.rect = self.helicopter_energy_sprite.image.get_rect()
		self.helicopter_energy_sprite.rect.left = 50
		self.helicopter_energy_sprite.rect.top = 100
		
		
	def update_humans_rescued_text(self):
	
		self.humans_rescued_sprite.image = self.font.render(
			self.humans_rescued_text % (
				self.humans_rescued,
				self.humans_rescued_max),
				True,
				self.fg_colour,
				self.bg_colour)			
		
		self.humans_rescued_sprite.rect = self.humans_rescued_sprite.image.get_rect()
		self.humans_rescued_sprite.rect.left = 50
		self.humans_rescued_sprite.rect.top = 150


	def update_humans_carrying_text(self):
	
		self.humans_carrying_sprite.image = self.font.render(
			self.humans_carrying_text % (
				self.humans_carrying,
				self.humans_carrying_max),
				True,
				self.fg_colour,
				self.bg_colour)			
		
		self.humans_carrying_sprite.rect = self.humans_carrying_sprite.image.get_rect()
		self.humans_carrying_sprite.rect.left = 50
		self.humans_carrying_sprite.rect.top = 200


	def update_stopwatch_text(self):
	
		self.stopwatch_sprite.image = self.font.render(
			str(datetime.timedelta(seconds=self.stopwatch)),
				True,
				self.fg_colour,
				self.bg_colour)			
		
		self.stopwatch_sprite.rect = self.stopwatch_sprite.image.get_rect()
		self.stopwatch_sprite.rect.left = 50
		self.stopwatch_sprite.rect.top = 250		
	
	
	def reduce_hitpoints_bird_collision(self):
		self.helicopter_hitpoints -= settings.BIRD_HITPOINT_REDUCTION
		
	
	def reduce_energy_cloud_collision(self):
		self.helicopter_energy -= settings.ENERGY_DRAINAGE_CLOUD
		
		
	def reduce_energy_cloud_turbo(self):
		self.helicopter_energy -= settings.ENERGY_DRAINAGE_CLOUD
		
		
	def restore_hitpoints(self):
		if self.helicopter_hitpoints < settings.HELICOPTER_HITPOINTS:
			self.helicopter_hitpoints += settings.HITPOINT_RESTORE_RATE	
			
	
	def increase_humans_rescued(self):
		
		self.humans_rescued += 1
		self.humans_carrying -= 1
		
	
	def increase_humans_carrying(self):
		
		self.humans_carrying += 1
	
	
	def update_stopwatch(self):
		
		self.stopwatch += 1
		
	
	def update(self):
	
		#if self.helicopter_hitpoints < settings.HELICOPTER_HITPOINTS:
		#	self.helicopter_hitpoints += settings.HITPOINT_HEAL	
	
		if self.helicopter_energy < settings.HELICOPTER_ENERGY:
			self.helicopter_energy += settings.ENERGY_CHARGE_RATE
			
		self.update_helicopter_hitpoints_text()
		self.update_helicopter_energy_text()
		self.update_humans_rescued_text()
		self.update_humans_carrying_text()
		self.update_stopwatch_text()
		
		
		if self.humans_rescued >= 50:
			return True
		
		if self.helicopter_energy <= 0:
			return True
		
		if self.helicopter_hitpoints <= 0:
			return True