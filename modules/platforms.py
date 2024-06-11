import pygame


class Platform:
    def __init__(self, color=(0, 0, 0), x=400, y=300):
        self.pygame = pygame
        self.color = color
        self.pygame.init()
        self.x = x
        self.y = y
