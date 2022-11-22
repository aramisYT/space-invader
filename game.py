from rocket import Rocket
from meteor import Meteor
import pygame


class Game:

    def __init__(self):

        self.rocket = Rocket()
        self.meteor = Meteor(self)
        self.all_rocket = pygame.sprite.Group()
        self.all_rocket.add(self.rocket)
        self.is_playing = False
        self.pressed = {}

    def update(self, screen):

        self.rocket.all_projectile.draw(screen)

        screen.blit(self.rocket.image, self.rocket.rect)

        self.meteor.all_meteors.draw(screen)

        Rocket.pygame_event(self.rocket)

        for projectile in self.rocket.all_projectile:
            projectile.move()

        for meteor in self.meteor.all_meteors:
            meteor.move()

    def start(self):
        self.is_playing = True
