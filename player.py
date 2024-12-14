import pygame
import constants as c
import keymaps as k
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, c.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += c.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * c.PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), c.LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[k.KEY_FORWARD]:
            self.move(dt)
        if keys[k.KEY_BACK]:
            self.move(-dt)
        if keys[k.KEY_LEFT]:
            self.rotate(-dt)
        if keys[k.KEY_RIGHT]:
            self.rotate(dt)
