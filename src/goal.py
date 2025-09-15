# src/goal.py

import pygame
from src.ball import Ball

class Goal(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.__position = [position[0], position[1]]
        # TODO: self.image = pygame.Surface([width, height])
        # TODO: self.image.fill((255, 255, 255)) # Or use an image
        # TODO: self.rect = self.image.get_rect(topleft=(x, y))
        pass

    def check_goal(self, ball: Ball):
        # TODO: Check if the ball has entered the goal
        # if pygame.sprite.collide_rect(self, ball):
        #     return True
        # return False
        pass
