import pygame
from configs.gameconf import *
from lib.utils import flip_sprite, flip_sprites


def get_frame_coef(anim):
    return GAME_FPS // len(anim)


class AbstractWizard:
    def __init__(self, game_obj, screen, side=False):
        self.tmp = False
        self.cur_anim = None
        self.frame_count = 0
        self.idle = None
        self.fight = None
        self.move_to = None
        self.screen = screen
        self.height = game_obj["height"]
        self.width = game_obj["width"]
        self.init_obj(game_obj, side)

    def init_obj(self, game_obj, side):
        if side:
            self.idle = flip_sprites(game_obj["idle"])
            self.fight = flip_sprites(game_obj["fight"])
            self.move_to = (OFFSET_X * (-1)) + self.width / 2
        else:
            self.idle = game_obj["idle"]
            self.fight = game_obj["fight"]
            self.move_to = OFFSET_X + self.width / 2

    def reset_frame_count(self):
        self.frame_count = 0

    def get_pos(self):
        pos_x = SW / 2 - self.move_to
        pos_y = SH - OFFSET_Y - self.height
        return pos_x, pos_y

    def draw(self):
        self.screen.blit(self.idle[0], (self.get_pos()))

    def do_idle(self):
        frame_coef = get_frame_coef(self.idle)
        # self.reset_fame_count()
        print(self.frame_count)
        self.screen.blit(self.idle[(self.frame_count // frame_coef) - 1], self.get_pos())
        self.frame_count += 1
        if self.frame_count > GAME_FPS:
            # TODO: use reset_frame_count func instead of new assigning
            self.frame_count = 0

    def do_fight(self):
        frame_coef = get_frame_coef(self.fight)
        self.screen.blit(self.fight[(self.frame_count // frame_coef) - 1], self.get_pos())
        self.frame_count += 1
        if self.frame_count > GAME_FPS:
            self.frame_count = 0

    def action(self, anim):
        # print(anim)
        if self.cur_anim == anim or self.cur_anim is None:
            anim()
        else:
            self.reset_frame_count()
            anim()


