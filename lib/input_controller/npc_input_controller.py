from time import time, perf_counter
from random import randrange
from lib.input_controller.input_controller import InputController
from configs.gameconf import G_DIFFICULTY, ERROR_CHANCE

difficulty = G_DIFFICULTY[1]


class NpcInputController(InputController):
    def __init__(self, game_controller, is_player=True):
        super().__init__(game_controller, is_player)
        self.count_down = None
        self.start = None

    def think(self):
        pass

    def set_countdown(self):
        self.count_down = randrange(difficulty[0], difficulty[1])
        self.start = time()

    def is_ready(self):
        cur_time = time()
        diff = cur_time - self.start
        if diff >= self.count_down:
            coef = randrange(0, 100)
            print(f"rand coef: {coef}")
            chance = 100 - ERROR_CHANCE
            print(f"chance: {chance}")
            self.isCorrect = True if coef <= chance else False
            self.notify_controller()
            self.set_countdown()
