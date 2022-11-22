import math
from random import *
import random
import pygame

window_x = 550
window_y = 978


class Meteor(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image()
        self.health = 40
        self.all_meteors = pygame.sprite.Group()
        self.velocity = random.uniform(1, 2.5)

    def image(self):
        self.image = pygame.image.load(f"""assets/meteors/meteor{random.randint(1, len("assets/meteors"))}.png""")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = choice([0 - self.rect.width, window_x])
        self.rect.y = random.randint(0, window_y)
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.all_meteors.remove(self)

    # function to make rotate the projectile.
    def rotate(self):
        self.angle += self.velocity
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rotate()
        self.slow_down()
        if self.rect.x < math.ceil(window_x / 2):
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity

    def slow_down(self):
        if self.velocity > 0:
            self.velocity -= 0.015
        if self.velocity <= 0:
            self.velocity = 0

    def spawn_meteor(self):
        self.all_meteors.add(Meteor(self))
