# import pygame
from configs.gameconf import *


def get_frame_coef(anim):
    return GAME_FPS // len(anim)


class MagicCast:
    def __init__(self, flame_obj, cast_obj, screen):
        self.flame_height = flame_obj["height"]
        self.flame_width = flame_obj["width"]
        self.flame_anim = flame_obj["anim"]
        self.screen = screen
        self.flame_offset_y = SH - FLAME_OFFSET_Y
        self.cast_offset_y = CAST_OFFSET_Y

        self.flame_frame_count = 0

        self.cast_height = cast_obj["height"]
        self.cast_width = cast_obj["width"]
        self.cast = cast_obj["cast"]

    def get_pos(self, pos_x, pos_y=None):
        y_pos = self.flame_offset_y if pos_y is None else pos_y
        x_pos = pos_x - self.flame_width // 2
        return x_pos, y_pos

    def draw_flame(self, pos_x, pos_y=None):
        frame_coef = get_frame_coef(self.flame_anim)
        self.screen.blit(self.flame_anim[(self.flame_frame_count // frame_coef) - 1], self.get_pos(pos_x, pos_y))
        self.flame_frame_count += 1
        if self.flame_frame_count > GAME_FPS:
            self.flame_frame_count = 0

    def draw_cast(self):
        c = (OFFSET_X - 40) // self.cast_width
        init_x_pos = (SW / 2) - self.cast_width // 2
        sprite_w = self.cast_width
        sprite_x_pos = sprite_w
        is_first = True
        for i in range(c):
            if is_first:
                self.screen.blit(self.cast[0], (init_x_pos, SH - CAST_OFFSET_Y))
                is_first = False
            else:
                self.screen.blit(self.cast[0], (init_x_pos + sprite_x_pos, SH - CAST_OFFSET_Y))
                self.screen.blit(self.cast[0], (init_x_pos - sprite_x_pos, SH - CAST_OFFSET_Y))
                # print(sprite_w)
                sprite_x_pos = sprite_w * i
