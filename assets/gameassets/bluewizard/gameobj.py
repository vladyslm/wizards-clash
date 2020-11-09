import pygame
import os

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

height = idle_anim[0].get_height()
width = idle_anim[0].get_width()


BLUE_WIZARD = {
    "idle": idle_anim,
    "fight": fight_anim,
    "height": height,
    "width": width
}
