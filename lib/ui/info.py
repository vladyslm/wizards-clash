import pygame
from configs.gameconf import *
pygame.font.init()


class LevelInfo:
    def __init__(self):
        self.info_font = pygame.font.SysFont("arial", 30, True, False)

    def get_lvl_pos(self, label):
        x_pos = SW // 2 - label.get_width() // 2
        return x_pos, LVL_OFFSET_Y

    def get_score_pos(self, label):
        x_pos = SW // 2 - label.get_width() // 2
        return x_pos, SCORE_OFFSET_Y

    def draw_lvl(self, screen, lvl):
        label = self.info_font.render(f"Level: {lvl}", True, (255, 255, 255))
        # pos_x, pos_y = self.get_lvl_pos()
        # pos_x = pos_x - label.get_width() // 2
        screen.blit(label, self.get_lvl_pos(label))

    def draw_score(self, screen, score):
        label = self.info_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(label, self.get_score_pos(label))

    def display_info(self, screen, score, lvl):
        self.draw_lvl(screen, lvl)
        self.draw_score(screen, score)


lvl_info = LevelInfo()
