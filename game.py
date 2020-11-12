import pygame
# from assets.gameassets.bluewizard.gameobj import BLUE_WIZARD
from assets.gameassets.bluewizard.gameobj import BLUE_WIZARD
from assets.gameassets.flame.gameobj import FLAME
from assets.gameassets.cast.gameobj import CAST
from lib.wizard.abstract_wizard import AbstractWizard
from lib.magic_cast.cast import MagicCast
from lib.game_controller.controller import Controller
# from lib.input_controller.problem_controller import ProblemController
from problem_controller import problem_controller
from lib.input_controller.input_controller import InputController
from lib.input_controller.npc_input_controller import NpcInputController
# from lib.ui.icon import IconController
# from assets.gameassets.icon.gameobj import ICON

from configs.gameconf import *

SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("WizardsClash")

BG = pygame.image.load('./assets/graphic/background/BG1.png')


pygame.init()


def game():
    run = True
    fps = GAME_FPS
    clock = pygame.time.Clock()

    p = AbstractWizard(BLUE_WIZARD, SCREEN)
    e = AbstractWizard(BLUE_WIZARD, SCREEN, True)
    flame = MagicCast(FLAME, CAST, SCREEN)

    # problem_controller = ProblemController()
    # problem_controller.set_problem()
    controller = Controller(p, e, flame, problem_controller, SCREEN)
    player_input_controller = InputController(controller)
    npc = NpcInputController(controller, False)
    problem_controller.add_input_controllers(player_input_controller, npc)
    controller.add_player_controller(player_input_controller)
    npc.set_countdown()

    def update_screen():
        SCREEN.blit(BG, (0, 0))
        controller.update_game_state()
        pygame.display.update()

    u_input = []
    while not controller.stopgame:
        # clock.tick(fps)
        npc.is_ready()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.stopgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_input_controller.add_input(player_input_controller.raw_input)
                    player_input_controller.get_keys_names()
                    player_input_controller.validate_input(problem_controller.get_answer())
                elif event.key == pygame.K_BACKSPACE:
                    player_input_controller.clean_input()
                elif event.key == pygame.K_q:
                    controller.stopgame = True
                else:
                    # u_input.append(event.key)
                    player_input_controller.add_raw_input(event.key)
        update_screen()
        clock.tick(fps)
