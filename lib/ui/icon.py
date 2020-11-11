from configs.gameconf import *
from lib.utils import flip_sprite
from assets.gameassets.icon.gameobj import ICON


class IconController:
    def __init__(self, game_obj, is_player=True):
        self.icon = game_obj["icon"]
        self.flask = game_obj["flask"]
        self.filled_power = game_obj["power_filled"]
        self.unfilled_power = game_obj["power_unfilled"]
        self.player = is_player

        if not self.player:
            self.icon = flip_sprite(self.icon)

    def get_icon_pos(self):
        if self.player:
            return ICON_OFFSET_X, ICON_OFFSET_Y
        pos_x = SW - ICON_OFFSET_X - self.icon.get_width()
        return pos_x, ICON_OFFSET_Y

    def get_power_pos(self):
        if self.player:
            return POWER_OFFSET_X, POWER_OFFSET_Y
        pos_x = SW - POWER_OFFSET_X - self.filled_power.get_width()
        return pos_x, POWER_OFFSET_Y

    def get_flask_pos(self):
        if self.player:
            return FLASK_OFFSET_X, FLASK_OFFSET_Y
        pos_x = SW - FLASK_OFFSET_X - self.flask.get_width()
        return pos_x, FLASK_OFFSET_Y

    def draw_icon(self, screen):
        screen.blit(self.icon, self.get_icon_pos())

    def draw_power(self, screen, filled_cell, max_cell):
        offset_between_cells = 8
        filled_cell_count = 0
        init_pos_x, init_pos_y = self.get_power_pos()
        for i in range(1, max_cell + 1):
            if self.player:
                pos_x = init_pos_x + (offset_between_cells * i) + (self.unfilled_power.get_width() * i)
            else:
                pos_x = init_pos_x - (offset_between_cells * i) - (self.unfilled_power.get_width() * i)
            if filled_cell_count < filled_cell:
                screen.blit(self.filled_power, (pos_x, init_pos_y))
            else:
                screen.blit(self.unfilled_power, (pos_x, init_pos_y))
            filled_cell_count += 1

    def draw_flask(self, screen, life_left):
        offset_between = 8
        init_pos_x, init_pos_y = self.get_flask_pos()
        for i in range(life_left):
            if self.player:
                pos_x = init_pos_x + (offset_between * i) + (self.flask.get_width() * i)
            else:
                pos_x = init_pos_x - (offset_between * i) - (self.flask.get_width() * i)
            screen.blit(self.flask, (pos_x, init_pos_y))

    def display_ui(self, screen, left_life, filled_cell, max_cell):
        self.draw_icon(screen)
        self.draw_flask(screen, left_life)
        self.draw_power(screen, filled_cell, max_cell)


player_ui = IconController(ICON)
enemy_ui = IconController(ICON, False)
