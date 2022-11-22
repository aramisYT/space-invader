from game import Game
import pygame
import math
import random
pygame.init()

# set the different variables
clock = pygame.time.Clock()
FPS = 144
game = Game()
window_x = 550
window_y = 978

# some parameters for the window.
pygame.display.set_caption("space invader")
screen = pygame.display.set_mode((window_x, window_y))

# backgrounds.
background = pygame.image.load("assets/bg.png")
background = pygame.transform.scale(background, (window_x, window_y))

# button
start_button = pygame.image.load("assets/GUI/start_button.png")
start_button = pygame.transform.scale(start_button, (300, 120))
start_button_rect = start_button.get_rect()
start_button_rect.x = math.ceil(window_x / 4)
start_button_rect.y = math.ceil(window_y / 2)

# loop of the game
running = True
while running:

    # draw the background
    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        # draw the start button
        screen.blit(start_button, start_button_rect)

    # refresh the display
    pygame.display.flip()

    # loop to detect the different event
    for event in pygame.event.get():

        # close the window and the program if the player quit the game
        if event.type == pygame.QUIT:
            game.is_playing = False
            running = False
            pygame.quit()
            exit()

        # if a key is pressed set "game.pressed" on "True".
        elif event.type == pygame.KEYDOWN:

            # if the key pressed is space launch a projectile.
            if event.key == pygame.K_SPACE:
                game.rocket.launch_projectile()
                game.meteor.spawn_meteor()

        # if the player clicks on the play button, start the "start" function.
        elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_playing:
            if start_button_rect.collidepoint(event.pos):
                game.start()

    # set the clock of the program
    clock.tick(FPS)
