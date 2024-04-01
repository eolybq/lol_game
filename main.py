import pygame

class Player:
	def __init__(self, x, y, image_path):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=(x,y))
		
sion = Player((width - 50) // 2,height -150, 'sion.png')




class Bullets:
	def __init__(self, image_path):
		self.image = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect(topleft=(x, y))
		
	def move(self, dx, dy):
        self.x += dx
        self.y += dy
