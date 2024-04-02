import pygame
import sys
from bullet import *

pygame.init()
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

class Player:
    def __init__(self, x, y, image_path, size):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move_up(self):
        self.y -= self.speed



sion = Player((screen_width - 50) // 2, screen_height - 150, 'sion.png', (150, 150))
vladimir = Player((screen_width - 50) // 2, screen_height - 150, 'vladimir.png', (150, 150))
bullet = Bullet((screen_width - 50) // 2, screen_height - 150, "bullet.png", (500, 500), 2, sion.x, sion.y)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)
minimize_text = font.render("_", True, WHITE)
close_text = font.render("x", True, RED)

minimize_rect = pygame.Rect(screen_width - 70, 0, 30, 30)
close_rect = pygame.Rect(screen_width - 35, 0, 30, 30)

clock = pygame.time.Clock()
running = True
is_firing = True
dt = 0
toolbar_rect = pygame.Rect(0, 0, screen_width, 50)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:  # Detekce stisku klávesy pro střelbu
            if event.key == pygame.K_q and bullet is None:  # Stisk klávesy pro výstřel
                bullet = Bullet(sion.rect.centerx, sion.rect.centery, "bullet.png", (20, 20), 5, vladimir.rect.centerx,
                                vladimir.rect.centery)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if minimize_rect.collidepoint(event.pos):
                pygame.display.iconify()  # Minimalizace okna
            elif close_rect.collidepoint(event.pos):
                pygame.quit()  # Ukončení Pygame
                sys.exit()  # Ukončení programu

    screen.fill("white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sion.rect.y -= 5  # Posun nahoru
    if keys[pygame.K_DOWN]:
        sion.rect.y += 5  # Posun dolů
    if keys[pygame.K_LEFT]:
        sion.rect.x -= 5  # Posun doleva
    if keys[pygame.K_RIGHT]:
        sion.rect.x += 5  # Posun doprava



    if keys[pygame.K_w]:
        vladimir.rect.y -= 5  # Posun nahoru
    if keys[pygame.K_s]:
        vladimir.rect.y += 5  # Posun dolů
    if keys[pygame.K_a]:
        vladimir.rect.x -= 5  # Posun doleva
    if keys[pygame.K_d]:
        vladimir.rect.x += 5  # Posun doprava

    # bullet.move()


    if keys[pygame.K_q]:
        screen.blit(bullet.image, bullet.rect)
        bullet.move_towards()


    # Vykreslení lišty s tlačítky minimalizace a zavření
    pygame.draw.rect(screen, (100, 100, 100), minimize_rect)
    pygame.draw.rect(screen, (100, 100, 100), close_rect)
    screen.blit(minimize_text, (screen_width - 65, 5))
    screen.blit(close_text, (screen_width - 30, 5))


    screen.blit(sion.image, sion.rect)
    screen.blit(vladimir.image, vladimir.rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
