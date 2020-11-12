import pygame
from lib.text_input import TextInput
from configs.gameconf import SH, SW, GAME_FPS
from score_state import score_state
from lib.utils import save_score

pygame.init()

pygame.display.set_caption("WizardsClash")

BG = pygame.image.load('./assets/graphic/background/BG1.png')
screen = pygame.display.set_mode((SW, SH))
clock = pygame.time.Clock()
textinput = TextInput()
GREY = (211, 203, 202)
BLACK = (0, 0, 0)

rec_bg = pygame.Rect(SW // 2 - 150, SH // 2 - 75, 300, 150)
font = pygame.font.SysFont("arial", 28, True)
label = font.render(f"Enter your name:", True, BLACK)


def add_score():
    running = True
    while running:
        screen.blit(BG, (0, 0))
        pygame.draw.rect(screen, GREY, rec_bg)
        screen.blit(label, (SW / 2 - label.get_width() // 2, SH / 2 - label.get_height() // 2 - 50))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    data = {
                        "name": textinput.get_text(),
                        "score": score_state.get_score() # TODO: should separate get_score and reset methods
                    }

                    save_score(data)
                    running = False

        textinput.update(events)
        screen.blit(textinput.get_surface(), (SW // 2 - textinput.get_surface().get_width() // 2, SH // 2))

        pygame.display.update()
        clock.tick(GAME_FPS)

