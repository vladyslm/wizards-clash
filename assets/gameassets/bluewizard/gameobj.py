import pygame
import os
from lib.utils import scale

dir_path = os.path.dirname(os.path.abspath(__file__))

idle_anim = [
    pygame.image.load(f"{dir_path}/idle-anim/idle_1.png"),
    pygame.image.load(f"{dir_path}/idle-anim/idle_2.png"),
    pygame.image.load(f"{dir_path}/idle-anim/idle_3.png"),
    pygame.image.load(f"{dir_path}/idle-anim/idle_4.png")
]
fight_anim = [
    # pygame.image.load(f"{dir_path}/fight-anim/fight_1.png"),
    # pygame.image.load(f"{dir_path}/fight-anim/fight_2.png"),
    pygame.image.load(f"{dir_path}/fight-anim/fight_3.png"),
    pygame.image.load(f"{dir_path}/fight-anim/fight_4.png"),
]


rescaled_fight_anim = scale(fight_anim, 218, 243)
rescaled_idle_anim = scale(idle_anim, 218, 243)

height = rescaled_fight_anim[0].get_height()
width = rescaled_fight_anim[0].get_width()


BLUE_WIZARD = {
    "idle": rescaled_idle_anim,
    "fight": rescaled_fight_anim,
    "height": height,
    "width": width
}
