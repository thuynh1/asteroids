from typing import override

import pygame.draw
from pygame import Surface, Rect, Color

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    # todo: add param to change the color of the shots
    @override
    def draw(self, screen: Surface) -> Rect:
        return pygame.draw.circle(
            screen,
            Color('yellow'),
            self.position,
            SHOT_RADIUS,
            2
        )

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt