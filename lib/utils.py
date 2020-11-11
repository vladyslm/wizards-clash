import pygame


def flip_sprite(sprite):
    return pygame.transform.flip(sprite, True, False)


def flip_sprites(sprite_list):
    flipped = []
    for sprite in sprite_list:
        sprite = flip_sprite(sprite)
        flipped.append(sprite)
    return flipped
