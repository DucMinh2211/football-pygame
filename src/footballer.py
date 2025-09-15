# src/footballer.py

import pygame
from enum import Enum
from src.ball import Ball

class Footballer(pygame.sprite.Sprite):
    # --- ROLES ---
    class Roles(Enum):
        FORWARDS = 0
        MID_L = 1
        MID_R = 2
        DEF_L = 3
        DEF_R = 4
        KEEPER = 5

    team_map: dict[int, dict[Roles, bool]] = { 
        0: {role: False for role in Roles},
        1: {role: False for role in Roles}  
    }

    def calc_position(self, SCREEN: tuple[int, int]) -> tuple[int, int]:
        if not self.__role:
            raise Exception("self.__role is null")
        # TODO: return footballer's position based on self.__role and self.__team_id
        return (SCREEN[0]//2, SCREEN[1]//2)


    def __init__(self, team_id: int, role: Roles, SCREEN: tuple[int, int]):
        if 0 > team_id > 1:
            raise Exception("team_id not valid")
        if Footballer.team_map[team_id][role]:
            raise Exception("The Role Already Existed.")

        Footballer.team_map[team_id][role] = True
        super().__init__()
        self.__role = role
        self.__team_id = team_id
        self.__position = self.calc_position(SCREEN)

        # TODO: DEL TMP IMAGE AND RECT
        self.image = pygame.Surface([32, 32])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.__position[0], self.__position[1]

        # TODO: self.image = ...
        # TODO: self.rect = self.image.get_rect(center=(x, y))
        # TODO: self.velocity = pygame.math.Vector2(0, 0)
        pass

    def move(self, direction: tuple[int, int]):
        # TODO: Implement player movement based on direction
        # e.g., self.velocity.x = ...
        pass

    def update(self):
        # TODO: Update player position based on velocity
        # self.rect.move_ip(self.velocity)
        pass

    def kick(self, ball: Ball):
        # TODO: Implement kicking logic
        # - Check for collision with the ball
        # - Apply force to the ball
        pass
