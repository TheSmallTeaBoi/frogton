import pygame


class Character:
    def __init__(self, x, y, screen, gravity=5):
        self.pygame = pygame
        self.pygame.init()
        self.screen = screen
        self.size = (10, 10, 10, 10)
        self.gravity = gravity

        self.terminalVelocity = 30

        self.speedX, self.speedY = 0, 0
        self.x = x
        self.y = y

    def draw(self):
        self.pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 10, 10))

    def fall(self):
        if self.y < 400:
            self.speedY += self.gravity
        else:
            self.y = 400

    def update(self):

        self.fall()

        # Clamp to max speeds
        self.speedX = max(
            min(self.speedX, self.terminalVelocity), -self.terminalVelocity
        )

        self.speedY = max(
            min(self.speedY, self.terminalVelocity), -self.terminalVelocity
        )

        self.x += self.speedX
        self.y += self.speedY

        self.draw()
