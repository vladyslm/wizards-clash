# answer_list = [1 or 0, True or False]

FLAME_INIT_POS = 500
POINTS_FOR_ANSWER = 10
MAX_SCORE = 100
LIVES_COUNT = 3
MOVE_FLAME = 50


class Controller:
    def __init__(self, player_wizard, enemy_wizard, cast, problem_controller):
        self.player = player_wizard
        self.enemy = enemy_wizard
        self.magic_cast = cast
        self.problem_controller = problem_controller
        self.flame_x_pos = FLAME_INIT_POS

        self.players_score = 0
        self.enemys_score = 0

        self.players_life_left = LIVES_COUNT
        self.enemys_life_left = LIVES_COUNT

        self.problem_controller.set_problem()

    def validate_input(self, answer): # answer - tuple(is_player, is_answer_correct)
        if answer[0]:
            if answer[1]:
                self.players_score += POINTS_FOR_ANSWER
                self.flame_x_pos += MOVE_FLAME
            else:
                self.players_life_left -= 1
                self.flame_x_pos -= MOVE_FLAME
        else:
            if answer[1]:
                self.enemys_score += POINTS_FOR_ANSWER
                self.flame_x_pos -= MOVE_FLAME
            else:
                self.enemys_life_left -= 1
        # self.update_game_state()
        self.problem_controller.set_problem()

    def get_flame_pos(self):
        return self.flame_x_pos

    def update_game_state(self):
        print(self.problem_controller.get_problem())
        self.magic_cast.draw_flame(self.get_flame_pos())

    def player_win(self):
        pass

    def player_lose(self):
        pass
