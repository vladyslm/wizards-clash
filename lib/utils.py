from pathlib import Path
import pygame
import json
from configs.gameconf import SBOARD_ROOT_KEY, SCOREBOARD_FILE_NAME


def flip_sprite(sprite):
    return pygame.transform.flip(sprite, True, False)


def flip_sprites(sprite_list):
    flipped = []
    for sprite in sprite_list:
        sprite = flip_sprite(sprite)
        flipped.append(sprite)
    return flipped


def get_project_root():
    return Path(__file__).parent.parent


def create_sboard_json_struc(data=0):
    i_data = [data] if data != 0 else []
    struc = {
        SBOARD_ROOT_KEY: i_data
    }
    return struc


def read_json_data(path):
    try:
        with open(path, 'r') as reader:
            json_data = json.load(reader)
    except json.decoder.JSONDecodeError:
        json_data = None
    return json_data


def write_json(data, path, mode="w"):
    with open(path, mode) as write:
        json.dump(data, write, ensure_ascii=False)


def init_scoreboard():
    data = create_sboard_json_struc()
    root = get_project_root()
    path = f"{root}/{SCOREBOARD_FILE_NAME}"
    write_json(data, path)


def save_score(score_data):
    root = get_project_root()
    path = f"{root}/{SCOREBOARD_FILE_NAME}"
    try:
        json_data = read_json_data(path)
        if json_data:
            json_data[SBOARD_ROOT_KEY].append(score_data)
            write_json(json_data, path)
        else:
            write_json(create_sboard_json_struc(score_data), path)
    except FileNotFoundError:
        write_json(create_sboard_json_struc(score_data), path)

