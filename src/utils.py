from os import system
from game import LevelInfo
from structures.hero import Hero


def clear_screen():
    system('cls || clear')


def remove_newline(name):
    correct_name = ''

    for letter in name:
        if letter != '\n':
            correct_name += letter
        else:
            break

    return correct_name


def get_player_level_from_save(player_info_loaded):
    return player_info_loaded[-1]


def open_level_file(level):
    level_file_path = './src/levels/' + level + '.txt'

    with open(level_file_path, 'r') as level_file:
        full_level_content = level_file.readlines()
        full_level_content = list(map(remove_newline, full_level_content))

        return full_level_content


def pop_level_info_from_file(full_level_content):
    level_info = []

    for index in range(4):
        level_info.append(full_level_content[index])

    return level_info


def setup_level(full_level_content, process_return):
    level_info_as_array = pop_level_info_from_file(
        full_level_content)

    level_info = LevelInfo(
        level_info_as_array[0], level_info_as_array[1], level_info_as_array[2])
    player = Hero(
        process_return[0], process_return[1], process_return[2], process_return[3])

    return level_info, player


def init_level(process_return):
    full_level_content = open_level_file(
        get_player_level_from_save(process_return))

    level_info, player = setup_level(
        full_level_content, process_return)

    return level_info, player
