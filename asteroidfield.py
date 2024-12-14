import pygame
import random
import constants as c
from asteroid import Asteroid


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-c.ASTEROID_MAX_RADIUS, y * c.SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                c.SCREEN_WIDTH + c.ASTEROID_MAX_RADIUS, y * c.SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * c.SCREEN_WIDTH, -c.ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * c.SCREEN_WIDTH, c.SCREEN_HEIGHT + c.ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > c.ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            edge = random.choice(self.edges)
            speed = random.randint(c.ASTEROID_MIN_SPEED, c.ASTEROID_MAX_SPEED)
            velocity = edge[0] * speed
            velocity = velocity.rotate(
                random.randint(
                    c.ASTEROID_MIN_VELOCITY_ANGLE, c.ASTEROID_MAX_VELOCITY_ANGLE
                )
            )
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, c.ASTEROID_KINDS)
            self.spawn(c.ASTEROID_MIN_RADIUS * kind, position, velocity)
