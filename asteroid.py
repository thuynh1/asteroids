from typing import override

import pygame.draw
from pygame import Rect, Surface, Color

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)

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