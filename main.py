from time import sleep

import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP

from modules import character
from modules import platforms

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Set up the player
player = character.Character(400, 300, screen)

platform = platforms.Platform()


# Move
def move(character):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        character.speedX -= 20
    if keys[K_RIGHT]:
        character.speedX += 20

    if not keys[K_RIGHT] and not keys[K_LEFT]:
        character.speedX = 0

    if keys[K_UP] and character.y >= 400:
        character.speedY -= 100


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Update the player
    move(player)
    player.update()

    # Flip the display
    pygame.display.flip()
    # 60fps
    sleep(0.013)

pygame.quit()
