import pygame
from typing import override
from pygame import Surface, Color, Rect, Vector2

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED
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

    def rotate(self, dt: float) -> None:
        """
        Rotate the player based on the time elapsed.

        This method updates the player's rotation angle. The rotation speed
        is determined by PLAYER_TURN_SPEED and is time-based for smooth
        movement regardless of frame rate.

        Args:
            dt (float): The time elapsed since the last update, typically in seconds.
                        This ensures consistent rotation speed across different frame rates.

        Returns:
            None

        Note:
            - Positive dt values rotate clockwise.
            - Negative dt values rotate counter-clockwise.
            - The actual rotation angle is calculated as PLAYER_TURN_SPEED * dt.
            - PLAYER_TURN_SPEED should be defined in your constants or config file.
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        """
        Move the player in the direction they are facing.

        This method updates the player's position based on their current rotation
        and the time elapsed since the last frame. The movement is frame-rate
        independent due to the use of delta time (dt).

        Args:
            dt (float): Delta time - the time elapsed since the last frame, in seconds.
                        Used to ensure smooth movement regardless of frame rate.

        Returns:
            None

        Notes:
            - The player moves in the direction they are facing (determined by self.rotation).
            - Movement speed is calculated as PLAYER_MOVE_SPEED * dt.
            - Positive dt moves the player forward, negative dt moves them backward.
            - PLAYER_MOVE_SPEED should be defined as a constant elsewhere in the code.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

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

    @override
    def update(self, dt: float):
        """
        Update the player's state based on keyboard input and elapsed time.

        This method overrides the base class `update` method. It processes player input
        to handle rotation and movement. The player's rotation and position are updated
        smoothly based on the elapsed time (`dt`), ensuring frame rate independence.

        Args:
            dt (float): The time elapsed since the last update, in seconds. This value
                        is used to calculate movement and rotation proportional to time.

        Returns:
            None

        Key Controls:
            - Pressing 'A' rotates the player counter-clockwise.
            - Pressing 'D' rotates the player clockwise.
            - Pressing 'W' moves the player forward in the direction they are facing.
            - Pressing 'S' moves the player backward in the direction they are facing.

        Notes:
            - The rotation speed is proportional to `dt` and is determined by a constant
              (e.g., `PLAYER_TURN_SPEED`).
            - The movement speed is also proportional to `dt` and depends on a constant
              (e.g., `PLAYER_MOVE_SPEED`).
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
