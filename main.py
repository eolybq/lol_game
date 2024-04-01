import pygame

class Player:
	def __init__(self, x, y, image_path):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=(x,y))
		
character = ((width - 50) // 2,height -150, 'sion.png')
