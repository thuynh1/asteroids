import sys

from pygame import Color

from score import Score
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import pygame

from player import Player


def main():
    print("Starting asteroids!")
    numpass, numfail = pygame.init()
    print(f"success = {numpass}, failed = {numfail}") # debug msg
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # todo: fps
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0  # delta time

    # Groups
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    bullets: pygame.sprite.Group = pygame.sprite.Group()

    # Components
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (bullets, updatable, drawable)

    # Instantiate a Player starting at the middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate Asteroids
    AsteroidField()

    # Game scoring system
    score = Score()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exit game loop if user has closed the window
                return

        screen.fill(Color('black'))

        for sprite in updatable:
            sprite.update(dt)

        # collision detection
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!") # todo: move this to a constant
                sys.exit()

            # bullet collision
            for bullet in bullets:
                if asteroid.collision(bullet):
                    score.increase(ASTEROID_DESTROYED_POINTS)
                    asteroid.split()
                    bullet.kill()

        for sprite in drawable:
            sprite.draw(screen)

        score.draw(screen, SCREEN_SCORE_X_POSITION, SCREEN_SCORE_Y_POSITION)

        pygame.display.flip()   # update the display

        # restrict frame rate to 60 FPS
        dt = clock.tick(GAME_FPS) / 1000    # convert from ms to sec


if __name__ == "__main__":
    main()