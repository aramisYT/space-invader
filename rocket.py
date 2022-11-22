import math
import random
from projectile import Projectile

import pygame

window_x = 550
window_y = 978


class Rocket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.cheat = False
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.crit_chance = 20
        self.crit = 30
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load("assets/rocket.png")
        self.image = pygame.transform.scale(self.image, (90, 120))
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil((window_x / 2) - (self.rect.width / 2))
        self.rect.y = math.ceil(window_y / 2)

    def launch_projectile(self):
        if random.uniform(0, 100) <= self.crit_chance:
            self.all_projectile.add(Projectile(self, "beam_white", 44, 62, 25))
        else:
            self.all_projectile.add(Projectile(self, "laser_white", 18, 63, 37))

    def cheat_mode(self):
        easter_egg = input("please enter the password to access the cheat mode :")
        if easter_egg == "tank" and not self.cheat:
            self.cheat = True
            self.health = 100000
            self.attack = 100000
            self.crit = 100000
            self.velocity = 5
            self.image = pygame.image.load("assets/tank.png")
            self.image = pygame.transform.scale(self.image, (90, 120))
        elif easter_egg == "tank" and self.cheat:
            self.cheat = False
            self.health = self.max_health
            self.attack = 20
            self.crit = 30
            self.velocity = 3
            self.image = pygame.image.load("assets/rocket.png")
            self.image = pygame.transform.scale(self.image, (90, 120))
        else:
            print("wrong password ( don't cheat it's not good ) !!!")
            self.cheat_mode()

    def pygame_event(self):
        key_pressed_is = pygame.key.get_pressed()

        if key_pressed_is[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if key_pressed_is[pygame.K_d] and self.rect.x + self.rect.width < window_x:
            self.rect.x += self.velocity
        if key_pressed_is[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if key_pressed_is[pygame.K_s] and self.rect.y + self.rect.height < window_y:
            self.rect.y += self.velocity
        if key_pressed_is[pygame.K_p] and self.rect.x == 462 and self.rect.y == 858:
            self.cheat_mode()
