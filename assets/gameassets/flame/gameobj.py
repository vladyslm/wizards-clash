import pygame
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

flame_anim = [
    pygame.image.load(f"{dir_path}/flame-anim/f_1.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_2.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_3.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_4.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_5.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_6.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_7.png"),
    pygame.image.load(f"{dir_path}/flame-anim/f_8.png")
]


def scale(list_anim, a_width, a_height):
    al = []
    for frame in list_anim:
        al.append(pygame.transform.scale(frame, (a_width, a_height)))
    return al


rescaled = scale(flame_anim, 64, 140)


height = rescaled[0].get_height()
width = rescaled[0].get_width()

FLAME = {
    "anim": rescaled,
    "height": height,
    "width": width
}
