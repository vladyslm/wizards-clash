import sys
from pygame.locals import *
from configs.gameconf import *
from game_screens.game import game
from game_screens.add_score import add_score
from game_screens.scoreboard import scoreboard
from modules.menu_ui_el import *
from setup import *


def menu():
    click_event = False
    while True:
        SCREEN.blit(MENU_GB, (0, 0))

        new_game_btn = newgame_rect
        scoreboard_btn = sboard_rect
        exit_btn = exit_rect

        m_x, m_y = pygame.mouse.get_pos()
        if new_game_btn.collidepoint((m_x, m_y)):
            if click_event:
                print("new game clicked")
                game()
                print("end game")
                # print(f"Your score: {score_state.get_score()}")
                add_score()
                scoreboard()
        if scoreboard_btn.collidepoint((m_x, m_y)):
            if click_event:
                print("scoreboard clicked")
                scoreboard()
        if exit_btn.collidepoint((m_x, m_y)):
            if click_event:
                pygame.quit()

        click_event = False

        SCREEN.blit(new_game_sprite, newgame_rect)
        SCREEN.blit(scoreboard_sprite, sboard_rect)
        SCREEN.blit(exit_sprite, exit_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_event = True

        pygame.display.update()
        clock.tick(GAME_FPS)


menu()
