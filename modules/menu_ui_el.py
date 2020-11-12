import pygame
from configs.gameconf import SW, SH, SPACE_BETWEEN_BTN

new_game_sprite = pygame.image.load('assets/graphic/menu/newgame_btn.png').convert()
newgame_rect = new_game_sprite.get_rect()
newgame_rect.center = (SW / 2, SH / 2)
scoreboard_sprite = pygame.image.load('assets/graphic/menu/scoreboard_btn.png').convert()
sboard_rect = scoreboard_sprite.get_rect()
sboard_rect.center = (SW / 2, SH / 2 + SPACE_BETWEEN_BTN + scoreboard_sprite.get_height())
exit_sprite = pygame.image.load('assets/graphic/menu/exit_btn.png').convert()
exit_rect = exit_sprite.get_rect()
exit_rect.center = (SW / 2, SH / 2 + SPACE_BETWEEN_BTN * 2 + exit_sprite.get_height() * 2)
