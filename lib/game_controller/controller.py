import pygame
from configs.gameconf import PROBLEM_SCREEN_OFFSET_Y, SW, SH, GAME_FPS
from lib.ui.icon import player_ui, enemy_ui
from lib.ui.info import lvl_info
from score_state import score_state

# TODO: clean up the code below
# answer_list = [1 or 0, True or False]

FLAME_INIT_POS = SW / 2
POINTS_FOR_ANSWER = 1
MAX_SCORE = 100
LIVES_COUNT = 3
FLAME_STEP = 30
SCORE = 100


class Controller:
    def __init__(self, player_wizard, enemy_wizard, cast, problem_controller, screen):
        self.player = player_wizard
        self.enemy = enemy_wizard
        self.magic_cast = cast
        self.problem_controller = problem_controller
        self.screen = screen
        self.flame_x_pos = FLAME_INIT_POS

        self.player_score = 0
        self.players_power = 0
        self.enemy_power = 0
        self.cur_lvl = 1

        self.players_life_left = LIVES_COUNT
        self.enemys_life_left = LIVES_COUNT

        self.problem_controller.set_problem()
        self.game_font = pygame.font.SysFont("arial", 50, True)

        self.player_input_controller = None

        self.delay = GAME_FPS * 2  # 2sec
        self.pause = 0

        self.gameover = False
        self.stopgame = False

    def add_player_controller(self, input_controller):
        self.player_input_controller = input_controller

    def validate_input(self, answer):  # answer - tuple(is_player, is_answer_correct)
        if answer[0]:
            print("player answering")
            print(answer)
            if answer[1]:
                self.player_score += SCORE
                self.players_power += POINTS_FOR_ANSWER
                self.flame_x_pos += FLAME_STEP
            else:
                self.players_life_left -= 1
                self.flame_x_pos -= FLAME_STEP
        else:
            print("nps answering")
            if answer[1]:
                self.enemy_power += POINTS_FOR_ANSWER
                self.flame_x_pos -= FLAME_STEP
            else:
                self.enemys_life_left -= 1
                self.flame_x_pos += FLAME_STEP
        # self.update_game_state()
        self.problem_controller.set_problem()

    def get_flame_pos(self):
        return self.flame_x_pos

    def update_game_state(self):
        self.state_controller()

    def playing(self):
        player_ui.display_ui(self.screen, self.players_life_left, self.players_power, 10)
        enemy_ui.display_ui(self.screen, self.enemys_life_left, self.enemy_power, 10)
        users_cur_input = self.player_input_controller.get_str_input()
        # lvl_info.draw_lvl(self.screen, self.cur_lvl)
        lvl_info.display_info(self.screen, self.player_score, self.cur_lvl)
        # print(f"users: cur input {users_cur_input}")
        problem_label = self.game_font.render(
            f"{self.problem_controller.get_problem()} = {users_cur_input}", True, (238, 231, 231)
        )
        p_label_x_offset = problem_label.get_width() // 2
        self.screen.blit(problem_label, (SW / 2 - p_label_x_offset, PROBLEM_SCREEN_OFFSET_Y))
        # print(self.problem_controller.get_problem())
        self.magic_cast.draw_cast()
        self.player.action(self.player.do_fight)
        self.enemy.action(self.enemy.do_fight)
        self.magic_cast.draw_flame(self.get_flame_pos())

    def player_win(self):
        # lvl_info.draw_lvl(self.screen, self.cur_lvl)
        lvl_info.display_info(self.screen, self.player_score, self.cur_lvl)
        self.player.action(self.player.do_idle)
        player_ui.display_ui(self.screen, self.players_life_left, self.players_power, 10)
        if self.delay <= self.pause:
            self.reset()
        self.pause += 1

    def player_lose(self):
        self.enemy.action(self.enemy.do_idle)
        enemy_ui.display_ui(self.screen, self.enemys_life_left, self.enemy_power, 10)
        self.gameover = True

    def get_game_status(self):
        if self.gameover:
            return "gameover"
        if self.players_life_left <= 0 or self.enemy_power >= 10 or self.flame_x_pos <= SW // 2 - 350:
            return "lose"
        if self.enemys_life_left <= 0 or self.players_power >= 10 or self.flame_x_pos >= SW // 2 + 350:
            return "win"
        return "playing"

    def reset(self):
        self.flame_x_pos = FLAME_INIT_POS

        # self.player_score = 0
        self.players_power = 0
        self.enemy_power = 0
        self.cur_lvl += 1

        self.players_life_left = LIVES_COUNT
        self.enemys_life_left = LIVES_COUNT

        self.pause = 0

    def state_controller(self):
        stages = {
            "lose": self.player_lose,
            "win": self.player_win,
            "playing": self.playing,
            "gameover": self.game_over
        }
        state = self.get_game_status()
        print(state)
        stages[state]()

    def game_over(self):
        label = self.game_font.render(f"Game Over", True, (238, 231, 231))
        self.screen.blit(label, (SW // 2 - label.get_width() // 2, SH // 2 - label.get_height() // 2))
        if GAME_FPS / 4 <= self.pause:
            score_state.add_score(self.player_score)
            self.stopgame = True
        self.pause += 1
