import pygame
import constants as c
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, c.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
