import pygame
from lib.input_controller.input_validator import validate


class InputController:
    def __init__(self, game_controller, is_player=True):
        self.input = None
        self.keys = []
        self.game_controller = game_controller
        self.isCorrect = None

        self.is_player = is_player
        self.raw_input = []

    def get_keys_names(self):
        keys = []
        for key_code in self.input:
            key_name = pygame.key.name(key_code)
            keys.append(key_name)
        # self.clean_input()
        print(keys)
        self.keys = keys

    def add_input(self, input_key):
        # self.input.append(input_key)
        self.input = input_key

    def validate_input(self, correct_answer):
        self.isCorrect = validate(self.keys, correct_answer)
        self.notify_controller()
        self.clean_input()

    def notify_controller(self):
        self.game_controller.validate_input((self.is_player, self.isCorrect))

    def clean_input(self):
        self.input.clear()
        self.keys.clear()
        self.raw_input.clear()

    def add_raw_input(self, char):
        self.raw_input.append(char)
