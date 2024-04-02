import pygame
import math
class Bullet:
    def __init__(self, x, y, image_path, size, speed, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed



    def move_towards(self):
        direction_x = self.target_x - self.rect.centerx
        direction_y = self.target_y - self.rect.centery
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        self.rect.x += direction_x * self.speed
        self.rect.y += direction_y * self.speed

    def update_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
