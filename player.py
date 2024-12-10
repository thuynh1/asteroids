import pygame
from typing import override
from pygame import Surface, Color, Rect, Vector2

from constants import PLAYER_RADIUS
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        """
        Initializes the Player object.

        Args:
            x (float): Starting x-coordinate of the player.
            y (float): Starting y-coordinate of the player.

        Returns:
            None
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0  # Rotation is a float (degrees).

    def triangle(self) -> list[Vector2]:
        """
        Calculate the three points of the triangle representing the player.

        This method computes the vertices of an isosceles triangle based on the
        player's position, rotation, and radius. The triangle points forward
        in the direction of the player's rotation.

        Returns:
            list[Vector2]: A list containing three Vector2 objects
            representing the vertices of the triangle in the order:
            [front point, back-left point, back-right point].
        """
        forward: Vector2 = Vector2(0, 1).rotate(self.rotation)
        right: Vector2 = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: Surface) -> Rect:
        """
        Draw the player on the given screen.

        This method overrides the base class draw method. It renders the player
        as a white triangle outline on the specified screen surface.

        Args:
            screen (Surface): The surface on which to draw the player.

        Returns:
            Rect: A rectangle object representing the area of the screen
            that was affected by the drawing operation.
        """
        return pygame.draw.polygon(screen, Color('white'), self.triangle(), 2)