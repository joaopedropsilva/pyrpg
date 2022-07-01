from os import system
from sys import stdout

from game import LevelInfo
from structures.hero import Hero
from structures.stack import Stack
from structures.game_constants import MAX_LINE_LENGTH


# General purpose functions


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


# Input related functions

def get_selected_item(item_index, item_place, bag_use_flag=False):
    if (bag_use_flag is False):
        return item_place[item_index]
    return item_place.peek()


# Level related functions


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


def convert_belt_info_to_array(belt_as_str):
    new_belt_as_str = ''

    for item in belt_as_str:
        if (item == '[' or item == ']' or item == '"' or item == "'"):
            continue
        new_belt_as_str += item
    belt_as_array = new_belt_as_str.split(',')

    belt_as_array = list(map(lambda item: item.strip(), belt_as_array))

    return belt_as_array


def convert_bag_info_to_stack(bag_as_str):
    bag_as_stack = Stack()
    new_bag_as_str = bag_as_str.strip('Stack()')

    new_bag_as_array = convert_belt_info_to_array(new_bag_as_str)

    for item in new_bag_as_array:
        bag_as_stack.push(item)

    return bag_as_stack


def setup_level(full_level_content, process_return, pre_save_flag):
    level_info_as_array = pop_level_info_from_file(
        full_level_content)

    level_info = LevelInfo(
        level_info_as_array[0], level_info_as_array[1], level_info_as_array[2])

    if (pre_save_flag):
        player = Hero(
            process_return[0], process_return[1], process_return[2], process_return[3], int(process_return[6]))
        player.belt = convert_belt_info_to_array(process_return[4])
        player.bag = convert_bag_info_to_stack(process_return[5])
    else:
        player = Hero(
            process_return[0], process_return[1], process_return[2], process_return[3], int(process_return[6]))

    return level_info, player


def init_level(process_return, pre_save_flag):
    full_level_content = open_level_file(
        get_player_level_from_save(process_return))

    level_info, player = setup_level(
        full_level_content, process_return, pre_save_flag)

    # remove the first 3 items (level info related)
    level_content = [line for index,
                     line in enumerate(full_level_content) if index > 2]

    return level_info, player, level_content


def check_line_length(line):
    line_size = len(line)

    if (line_size > MAX_LINE_LENGTH):
        # breaks the line into elements, including spaces
        new_line = [element for item in line.split()
                    for element in (item, ' ')][:-1]

        # iterates through the elements in new_line in reverse
        for index in reversed(range(len(new_line))):
            line_size -= len(new_line[index])
            if (new_line[index] == ' ' and line_size <= MAX_LINE_LENGTH):
                dropped_part = new_line[index:]
                del new_line[index:]
                break

        new_line_as_string = ''.join(new_line)
        dropped_part_as_string = ''.join(dropped_part)
        return new_line_as_string, dropped_part_as_string

    return None, None


# Save related functions


def autosave(level_info, player):
    file_path = './saves/save_' + str(player.name) + '.txt'
    with open(file_path, 'w') as save:
        save.write(
            f'{player.name}\n{player.hp}\n{player.atk}\n{player.dfs}\n{str(player.belt)}\n{str(player.bag)}\n{player.screens}\n{level_info.level_code}')


def get_entry_point_to_level(level_info, player):
    flags_to_reach = player.screens
    flags_count = 0
    full_level_content = open_level_file(level_info.level_code)

    # remove the first 3 items (level info related)
    level_content = [line for index,
                     line in enumerate(full_level_content) if index > 2]

    for index, line in enumerate(level_content):
        if (line == '\start'):
            flags_count += 1
        if (flags_count == flags_to_reach):
            return index
