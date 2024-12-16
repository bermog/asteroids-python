import pygame
import random
import constants as c
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - c.ASTEROID_MIN_RADIUS
        new_velocity = random.uniform(
            c.ASTEROID_MIN_SPLIT_ANGLE, c.ASTEROID_MAX_SPLIT_ANGLE
        )
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = (
            self.velocity.rotate(new_velocity) * c.ASTEROID_SPEED_MULTIPLIER
        )
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = (
            self.velocity.rotate(-new_velocity) * c.ASTEROID_SPEED_MULTIPLIER
        )

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, c.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
