import pygame
from configs.gameconf import PROBLEM_SCREEN_OFFSET_Y, SW
# TODO: clean up the code below
# answer_list = [1 or 0, True or False]

FLAME_INIT_POS = SW / 2
POINTS_FOR_ANSWER = 10
MAX_SCORE = 100
LIVES_COUNT = 3
FLAME_STEP = 50


class Controller:
    def __init__(self, player_wizard, enemy_wizard, cast, problem_controller, screen):
        self.player = player_wizard
        self.enemy = enemy_wizard
        self.magic_cast = cast
        self.problem_controller = problem_controller
        self.screen = screen
        self.flame_x_pos = FLAME_INIT_POS

        self.players_score = 0
        self.enemys_score = 0

        self.players_life_left = LIVES_COUNT
        self.enemys_life_left = LIVES_COUNT

        self.problem_controller.set_problem()
        self.game_font = pygame.font.SysFont("arial", 50)

        self.player_input_controller = None

    def add_player_controller(self, input_controller):
        self.player_input_controller = input_controller

    def validate_input(self, answer): # answer - tuple(is_player, is_answer_correct)
        if answer[0]:
            print("player answering")
            print(answer)
            if answer[1]:
                self.players_score += POINTS_FOR_ANSWER
                self.flame_x_pos += FLAME_STEP
            else:
                self.players_life_left -= 1
                self.flame_x_pos -= FLAME_STEP
        else:
            print("nps answering")
            if answer[1]:
                self.enemys_score += POINTS_FOR_ANSWER
                self.flame_x_pos -= FLAME_STEP
            else:
                self.enemys_life_left -= 1
                self.flame_x_pos += FLAME_STEP
        # self.update_game_state()
        self.problem_controller.set_problem()

    def get_flame_pos(self):
        return self.flame_x_pos

    def update_game_state(self):
        users_cur_input = self.player_input_controller.get_str_input()
        # print(f"users: cur input {users_cur_input}")
        problem_label = self.game_font.render(f"{self.problem_controller.get_problem()} = {users_cur_input}", True, (0, 0, 0))
        p_label_x_offset = problem_label.get_width() // 2
        self.screen.blit(problem_label, (SW / 2 - p_label_x_offset, PROBLEM_SCREEN_OFFSET_Y))
        # print(self.problem_controller.get_problem())
        self.magic_cast.draw_cast()
        self.magic_cast.draw_flame(self.get_flame_pos())

    def player_win(self):
        self.player.action(self.player.do_idle)

    def player_lose(self):
        pass
