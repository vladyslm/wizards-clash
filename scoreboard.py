from pygame.locals import *
from configs.gameconf import *
from modules.menu_ui_el import *
from lib.utils import read_json_data, get_project_root

clock = pygame.time.Clock()
pygame.init()

SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("WizardsClash")
BG = pygame.image.load('assets/graphic/scoreboard/sboard_bg.png')

font = pygame.font.SysFont("arial", 50, True)

WHITE = (255, 255, 255)


def get_scoreboard():
    root = get_project_root()
    path = f"{root}/{SCOREBOARD_FILE_NAME}"
    data = read_json_data(path)
    l_list = []
    try:
        for el in data[SBOARD_ROOT_KEY]:
            label = font.render(f"{el['name']} - {el['score']}", True, WHITE)
            l_list.append(label)
    except TypeError:
        # TODO: add error handling!
            pass
    return l_list


def display_scoreboard(labels_list, screen):
    space_between = 8
    offset_y = SBOARD_OFFSET_Y
    for i, label in enumerate(labels_list):
        pos_x = SW / 2 - label.get_width() // 2
        pos_y = offset_y + label.get_height() * i + space_between * i
        screen.blit(label, (pos_x, pos_y))


def scoreboard():
    running = True
    labels = get_scoreboard()
    while running:
        SCREEN.blit(BG, (0, 0))
        display_scoreboard(labels, SCREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_event = True

        pygame.display.update()
        clock.tick(GAME_FPS)
