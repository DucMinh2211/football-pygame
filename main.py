# main.py

import pygame
from src.footballer import Footballer
from src.ball import Ball
from src.goal import Goal
from src.ui import draw_score

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 820, 480
SCREEN = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

def spawn_footballer(team_id: int) -> list[Footballer]:
    return [Footballer(team_id=team_id, role=_role, SCREEN=SCREEN) for _role in Footballer.Roles]

def add_foorballers_to_all_sprites(footballers: list, all_sprites: pygame.sprite.Group):
    for footballer in footballers:
        all_sprites.add(footballer)

def main():
    # --- Initialization ---
    pygame.init()
    screen = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("Football Game")
    clock = pygame.time.Clock()
    score = [0, 0]

    # --- Game Objects ---
    all_sprites = pygame.sprite.Group()

    footballers_t0 = spawn_footballer(team_id=0)
    footballers_t1 = spawn_footballer(team_id=1)
    add_foorballers_to_all_sprites(footballers=footballers_t0, all_sprites=all_sprites)
    add_foorballers_to_all_sprites(footballers=footballers_t1, all_sprites=all_sprites)

    # ball = Ball(...)
    # all_sprites.add(ball)
    # goal1 = Goal(...)
    # all_sprites.add(goal1)
    # goal2 = Goal(...)
    # all_sprites.add(goal2)

    # --- Game Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle input for player movement, switching players, kicking
            if event.type == pygame.KEYDOWN:
            # TODO: implement input
            #     if event.key == pygame.K_...: # Player 1 move
            #         active_player_p1.move(...)
            #     if event.key == pygame.K_...: # Player 2 move
            #         active_player_p2.move(...)
            #     if event.key == pygame.K_...: # Switch player 1
            #         switch active player logic for p1
            #         pass
            #     if event.key == pygame.K_...: # Switch player 2
            #         switch active player logic for p2
            #         pass
            #     if event.key == pygame.K_...: # Kick
            #         active_player.kick(ball)
                pass


        # --- Game Logic / Physics ---
        all_sprites.update()
        # Check for collisions between players and ball
        for footballer in footballers_t0 + footballers_t1:
        #    footballer.run_ball(ball)
            pass

        # Check for goal
        # if goal1.check_goal(ball):
        #     score_player2 += 1
        #     Reset positions
        # if goal2.check_goal(ball):
        #     score_player1 += 1
        #     Reset positions

        # --- Drawing ---
        screen.fill((0, 128, 0)) # Green field
        all_sprites.draw(screen)
        # ball.draw_shadow(screen)

        # --- UI (Score) ---
        draw_score(screen, (score[0], score[1]), SCREEN_WIDTH)


        # --- Update Display ---
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
