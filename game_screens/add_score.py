from lib.text_input import TextInput
from configs.gameconf import GAME_FPS
from modules.score_state import score_state
from lib.utils import save_score
from setup import *

textinput = TextInput()


rec_bg = pygame.Rect(SW // 2 - 150, SH // 2 - 75, 300, 150)
label = FONT_SMALL.render(f"Enter your name:", True, BLACK)


def add_score():
    running = True
    while running:
        SCREEN.blit(GAME_BG, (0, 0))
        pygame.draw.rect(SCREEN, GREY, rec_bg)
        SCREEN.blit(label, (SW / 2 - label.get_width() // 2, SH / 2 - label.get_height() // 2 - 50))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    data = {
                        "name": textinput.get_text(),
                        "score": score_state.get_score()  # TODO: should separate get_score and reset methods
                    }

                    save_score(data)
                    running = False

        textinput.update(events)
        SCREEN.blit(textinput.get_surface(), (SW // 2 - textinput.get_surface().get_width() // 2, SH // 2))

        pygame.display.update()
        clock.tick(GAME_FPS)
