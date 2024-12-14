import pygame
import constants as c
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, c.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
