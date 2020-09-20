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
		
		if os.path.isfile(_paths):
			# Load image from file.				
			surfaces.append(
				pygame.image.load(
					_paths).convert_alpha())
					
		elif os.path.isdir(_paths):
			# Load images from dir.
			d = _paths
			print(os.listdir(d))
			for f in os.listdir(d):
				tmp_path = os.path.join(
					os.path.abspath(_paths),
					f)
				surfaces.append(
					pygame.image.load(
						tmp_path).convert_alpha())
	
	return surfaces


def load_sounds():
	pass


def load_music():
	pass
	
	