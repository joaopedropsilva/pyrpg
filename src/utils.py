from argparse import ArgumentError
from copy import deepcopy
from os import system
from sys import stdout

from game import LevelInfo, all_items
from structures.hero import Hero
from structures.stack import Stack
from structures.game_constants import MAX_LINE_LENGTH, DEFAULT_HERO_BELT_LENGTH


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


# Input functions


def check_inventory_state(player):
    if (player.bag.peek() == ''):
        return 'Vazia', False
    return player.bag.peek(), True


def get_item_by_name(item_name, all_items):
    for item in all_items.values():
        if(item_name == item.name):
            return item


def get_selected_item(item_index, player, bag_use_flag=False):
    if (bag_use_flag is False):
        item_name = player.belt[item_index-1]
        return get_item_by_name(item_name, all_items)
    item_name = player.bag.peek()
    return get_item_by_name(item_name, all_items)


def process_item_found_decision(option, player, item):
    try:
        if (item is None):
            raise ArgumentError

        if (option == 1 and len(player.belt) == DEFAULT_HERO_BELT_LENGTH):
            player.bag.push(item.name)

            return 'item_add_to_bag'
        elif (option == 1 and len(player.belt) < DEFAULT_HERO_BELT_LENGTH):
            if (player.belt[0] == ''):
                player.belt.pop()
            player.belt.append(item.name)

            return 'item_add_to_belt'
        else:
            return None
    except ArgumentError:
        print('[ArgumentError] No item found!')
        return False


def process_decision_inputs(option, context, player, item=None):
    if (context == 'item_found_options'):
        return process_item_found_decision(option, player, item)
    # elif (context == '')


def process_interaction_inputs(option, context, player, bag_use_flag):
    if (context == 'item_select'):
        return get_selected_item(option, player, bag_use_flag)


def filter_inputs(input, player, enemy=None, item=None):
    input_response, context = input
    option, option_type, bag_use_flag = input_response

    if (option_type == 'decide'):
        return process_decision_inputs(option, context, player, item)
    elif (option_type == 'interact'):
        return process_interaction_inputs(option, context, player, bag_use_flag)


# Level functions


def get_player_level_from_save(player_info_loaded):
    return player_info_loaded[-1]


def open_level_file(level_code):
    level_file_path = './src/levels/' + level_code + '.txt'

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
        player.belt.append('Lança Hereditária')
        player.bag.push('')

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


# Change level functions

def get_next_level(level_info):
    level_code_text = level_info.level_code[:4]
    level_code_number = int(level_info.level_code[-1])

    return level_code_text + str(level_code_number+1)


def change_level_info_object(level_info, new_level_code):
    new_level_info = deepcopy(level_info)

    full_level_content = open_level_file(new_level_code)
    level_info_as_array = pop_level_info_from_file(full_level_content)

    new_level_info.level_code = level_info_as_array[0]
    new_level_info.level_number = level_info_as_array[1]
    new_level_info.chapter_name = level_info_as_array[2]

    return new_level_info


def change_level_info_procedure(level_info, player):
    new_level_code = get_next_level(level_info)
    new_level_info = change_level_info_object(level_info, new_level_code)

    player.screens = 1
    return new_level_info


# Save functions


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
        if (line == '/start'):
            flags_count += 1
        if (flags_count == flags_to_reach):
            return index
