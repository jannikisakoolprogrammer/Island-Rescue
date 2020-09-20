import os.path

import pygame
pygame.init()


def load_images(
	_paths):
	
	surfaces = []
	
	print(type(_paths))
	
	if type(_paths) == (list or tuple):
		# Can either be a single file or a list of files.
		print("# Can either be a single file or a list of files.")
		
		for p in _paths:
			# Load image from file.				
			surfaces.append(
				pygame.image.load(
					p).convert_alpha())

	
	elif type(_paths) == str:
		# Can either be dir or file.
		print("# Can either be dir or file.")
		
		for p in _paths:
		
			if os.path.isfile(p):
				# Load image from file.				
				surfaces.append(
					pygame.image.load(
						p).convert_alpha())
						
			elif os.path.isdir(p):
				# Load images from dir.
				d = p
				for f in d:
					surfaces.append(
						pygame.image.load(
							f).convert_alpha())
	
	return surfaces


def load_sounds():
	pass


def load_music():
	pass
	
	