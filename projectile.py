import pygame

window_x = 550
window_y = 978


class Projectile(pygame.sprite.Sprite):

    def __init__(self, rocket, name, x, y, rect_x):
        super().__init__()

        self.rocket = rocket
        self.velocity = 5
        self.image = pygame.image.load(f"assets/projectiles/{name}.png")
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = rocket.rect.x + rect_x
        self.rect.y = rocket.rect.y - 40

    # function to remove the projectile.
    def remove(self):
        self.rocket.all_projectile.remove(self)

    # function to make move the projectile forward.
    def move(self):
        if self.rect.y < -50:
            self.remove()
        else:
            self.rect.y -= self.velocity
