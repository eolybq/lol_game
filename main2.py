import pygame
import sys
from bullet import *
import math
from axe_list import *

pygame.init()
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
frame_interval = 1000 // 6

class Player:
    def __init__(self, x, y, image_path, size, cooldown_time):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.cooldown_time = cooldown_time
        self.max_health = 100
        self.current_health = 100

    def attack(self):
            return Bullet(self.rect.centerx, self.rect.centery, "bullet.png", (50, 50), 20, sion.rect.centerx, sion.rect.centery)

    def update_cooldown(self, dt):
        self.cooldown_time -= dt
        if self.cooldown_time < 0:
            self.cooldown_time = 0

class Axe:
    def __init__(self, x, y, size, obrazek):
        self.x = x
        self.y = y
        self.image = pygame.image.load(obrazek).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.size = size

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
        if distance!= 0:
            direction_x /= distance
            direction_y /= distance

        self.rect.x += direction_x * self.speed
        self.rect.y += direction_y * self.speed

    def update_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

sion = Player((screen_width - 50) // 2, screen_height - 150, 'sion.png', (200,220), 0)
vladimir = Player((screen_width - 50) // 2, screen_height - 150, 'vladimir.png', (140, 200), 0)
bullet = None

axe_paths = ['axe1.png', 'axe2.png', 'axe3.png', 'axe4.png', 'axe5.png', 'axe6.png']

axe_offset_x = -65  # Adjust this value to your desired offset
axe_offset_y = 0  # Adjust this value to your desired offset

axes_obj = [Axe(sion.rect.centerx + axe_offset_x, sion.rect.centery + axe_offset_y, (180, 180), path) for path in axe_paths]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)
minimize_text = font.render("_", True, WHITE)
close_text = font.render("x", True, RED)

minimize_rect = pygame.Rect(screen_width - 70, 0, 30, 30)
close_rect = pygame.Rect(screen_width - 35, 0, 30, 30)

axe_frame_interval = 1000 // 6  # Interval pro aktualizaci obrázků sekery (6 FPS)
axe_frame_timer = 0  # ��asovač pro aktualizaci obrázků sekery

current_frame = 0
frame_timer = 0
clock = pygame.time.Clock()
running = True
is_firing = True
dt = 0
toolbar_rect = pygame.Rect(0, 0, screen_width, 50)

is_animating_axes = False
axe_frame_timer = pygame.time.get_ticks()

damage_dealt = False

while running:

    dt = clock.tick(120) / 1000
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if minimize_rect.collidepoint(event.pos):
                pygame.display.iconify()  # Minimalizace okna
            elif close_rect.collidepoint(event.pos):
                pygame.quit()  # Ukončení Pygame
                sys.exit()  # Ukončení programu
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                is_animating_axes = True  # Start animating axes on 'm' press
                axe_frame_timer = current_time  # Reset the timer

            if event.key == pygame.K_q:
                if vladimir.cooldown_time <= 0:  # Kontrola cooldownu
                    
                    bullet = vladimir.attack()
                    
                    
                    vladimir.cooldown_time = 2.5

          
                    

    sion.update_cooldown(dt)
    vladimir.update_cooldown(dt)

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

    if is_animating_axes:
        if current_time - axe_frame_timer >= axe_frame_interval:
            current_frame = (current_frame + 1) % len(axes_obj)
            axe_frame_timer = current_time
            # Optional: Stop the animation after one cycle
            
            if current_frame == 0:
                is_animating_axes = False  # Stop animating after one full cycle
                damage_dealt = False

    # Drawing Axes if Animation is Active
    if is_animating_axes:
        screen.blit(axes_obj[current_frame].image, (sion.rect.x + axe_offset_x, sion.rect.y + axe_offset_y))
        
        for axe in axes_obj:
            if axe.rect.colliderect(vladimir.rect) and not damage_dealt:
                vladimir.current_health -= 20
                damage_dealt = True
    
    

    if bullet is not None:
        bullet.update_target(sion.rect.centerx, sion.rect.centery)
        bullet.move_towards()
        screen.blit(bullet.image, bullet.rect)
        if bullet.rect.colliderect(sion.rect):
            sion.current_health -= 20
            bullet = None  # Zničení střely po zásahu cíle

    # Vykreslení lišty s tlačítky minimalizace a zavření
    pygame.draw.rect(screen, (100, 100, 100), minimize_rect)
    pygame.draw.rect(screen, (100, 100, 100), close_rect)
    screen.blit(minimize_text, (screen_width - 65, 5))
    screen.blit(close_text, (screen_width - 30, 5))

    screen.blit(sion.image, sion.rect)
    screen.blit(vladimir.image, vladimir.rect)

    pygame.draw.rect(screen, BLACK, (vladimir.rect.x, vladimir.rect.y - 50, 200, 20))
    health_ratio = vladimir.current_health / vladimir.max_health
    health_width = int(200 * health_ratio)
    pygame.draw.rect(screen, RED, (vladimir.rect.x, vladimir.rect.y - 50, health_width, 20))


    pygame.draw.rect(screen, BLACK, (sion.rect.x, sion.rect.y - 50, 200, 20))
    health_ratio2 = sion.current_health / sion.max_health
    health_width2 = int(200 * health_ratio2)
    pygame.draw.rect(screen, RED, (sion.rect.x, sion.rect.y - 50, health_width2, 20))

    
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
