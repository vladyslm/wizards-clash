import time
from configs.gameconf import *
from lib.utils import flip_sprites


class AbstractWizard:
    def __init__(self, game_obj, screen, side=False):
        self.tmp = False
        self.cur_anim = None
        self.idle = None
        self.fight = None
        self.move_to = None
        self.screen = screen
        self.height = game_obj["height"]
        self.width = game_obj["width"]
        self.init_obj(game_obj, side)

        self.lt = 0
        self.cur_frame = 0

    def init_obj(self, game_obj, side):
        if side:
            self.idle = flip_sprites(game_obj["idle"])
            self.fight = flip_sprites(game_obj["fight"])
            self.move_to = (OFFSET_X * (-1)) + self.width / 2
        else:
            self.idle = game_obj["idle"]
            self.fight = game_obj["fight"]
            self.move_to = OFFSET_X + self.width / 2

    def get_pos(self):
        pos_x = SW / 2 - self.move_to
        pos_y = SH - OFFSET_Y - self.height
        return pos_x, pos_y

    def anim_controller(self, anim, delay=.3):
        if time.perf_counter() - self.lt >= delay:
            self.lt = time.perf_counter()
            self.cur_frame += 1
            if self.cur_frame > len(anim) - 1:
                self.cur_frame = 0
        self.screen.blit(anim[self.cur_frame], self.get_pos())

    def do_idle(self):
        self.anim_controller(self.idle)

    def do_fight(self):
        self.anim_controller(self.fight)

    def action(self, anim):
        if self.cur_anim == anim:
            self.cur_anim = anim
            anim()
        else:
            self.cur_frame = 0
            self.cur_anim = anim
            anim()
