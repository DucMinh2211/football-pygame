# src/ball.py

import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.__position = [position[0], position[1]]
        # TODO: self.image = ...
        # TODO: self.rect = self.image.get_rect(center=(x, y))
        # TODO: self.velocity = pygame.math.Vector2(0, 0)
        # TODO: self.shadow = ...
        pass

    def update(self):
        # TODO: Update ball position based on velocity
        # self.rect.move_ip(self.velocity)
        # TODO: Apply friction
        # self.velocity *= 0.99
        # TODO: Update shadow position
        pass

    def draw_shadow(self, surface):
        # TODO: Draw the shadow underneath the ball
        pass
