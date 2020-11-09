import pygame
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

cast = [
    pygame.image.load(f"{dir_path}/cast-sprite/magic_cast.png")
]

height = cast[0].get_height()
width = cast[0].get_width()

CAST = {
    "cast": cast,
    "height": height,
    "width": width
}
