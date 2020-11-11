import pygame
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

icon = pygame.image.load(f"{dir_path}/sprites/icon.png")
power_filled = pygame.image.load(f"{dir_path}/sprites/power_filled.png")
power_unfilled = pygame.image.load(f"{dir_path}/sprites/power_unfilled.png")
flask = pygame.image.load(f"{dir_path}/sprites/flask.png")

resized_flask = pygame.transform.scale(flask, (30, 35))

ICON = {
    "icon": icon,
    "power_unfilled": power_unfilled,
    "power_filled": power_filled,
    "flask": resized_flask
}
