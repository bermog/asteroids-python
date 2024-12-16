#!/usr/bin/env python3

import pygame
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable

    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(c.FPS_LIMIT) / 1000


if __name__ == "__main__":
    main()
