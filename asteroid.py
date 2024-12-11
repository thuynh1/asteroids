from typing import override

import random
import pygame.draw
from pygame import Rect, Surface, Color, Vector2

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)

    def split(self):
        """

        Notes:
            - Large asteroids split into two medium asteroids
            - Medium asteroids split into two small asteroids
            - Small asteroids disappear when destroyed
        """
        old_radius = self.radius # is this needed?
        self.kill() # destroy the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS: # small asteroid, no further split
            return
        # spawning 2 smaller sized asteroids
        random_angle = random.uniform(20.0, 50.0)
        split_angle_1 = self.velocity.rotate(random_angle)
        split_angle_2 = self.velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        # todo: can update the end range to split into more asteroids, would need to refactor
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # todo: add control for the increased velocity of the smaller asteroid
        # update trajectory of the two smaller asteroids and increase their velocity
        asteroid_1.velocity = split_angle_1 * 1.2
        asteroid_2.velocity = split_angle_2 * 1.2


    # todo: add param to change the color and/or line width (for drawing) of the asteroid
    @override
    def draw(self, screen: Surface) -> Rect:
        """
        Draws the asteroid on the specified surface.

        Parameters:
            screen (Surface): The Pygame surface on which to draw the asteroid.

        Returns:
            Rect: A Pygame Rect object that represents the area of the drawn circle.
        """
        return pygame.draw.circle(
            screen,
            Color('white'),
            self.position,
            self.radius,
            2
        )

    @override
    def update(self, dt: float) -> None:
        """
        Updates the asteroid's position based on its velocity and elapsed time.

        Parameters:
            dt (float): The time in seconds since the last update. This value
                        is used to scale the movement according to the frame rate.
        """
        self.position += self.velocity * dt