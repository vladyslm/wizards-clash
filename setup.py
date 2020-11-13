import pygame
from configs.gameconf import SW, SH

pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("WizardsClash")
GREY = (211, 203, 202)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("arial", 50, True)
FONT_SMALL = pygame.font.SysFont("arial", 28, True)

MENU_GB = pygame.image.load('assets/graphic/menu/wizards_clash.png')
GAME_BG = pygame.image.load('./assets/graphic/background/BG1.png')
SCOREBOARD_BG = pygame.image.load('assets/graphic/scoreboard/scoreboard_bgv2.png')
