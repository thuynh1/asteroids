import pygame.sprite

from pygame import Rect, Surface

# todo: add documentation
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int):
        """
        Initializes the CircleShape with position and radius.

        Parameters:
            x (float): The x-coordinate of the circle's center.
            y (float): The y-coordinate of the circle's center.
            radius (int): The radius of the circle.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: Surface) -> Rect:
        """
        Draws the shape on the specified surface.

        Parameters:
            screen (Surface): The Pygame surface to draw on.

        Returns:
            Rect: The area occupied by the drawn shape.
        """
        pass

    def update(self, dt: float) -> None:
        """
        Updates the shape's position based on its velocity and elapsed time.

        Parameters:
            dt (float): The time in seconds since the last update.
        """
        pass