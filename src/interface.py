from structures.game_constants import ALL_ENEMIES_LIST, ALL_ITEMS_LIST
from utils import (clear_screen, check_line_length,
                   filter_inputs)
from game import all_items, all_enemies


# Input related functions


def input_attempts(filter='letter'):
    if (filter == 'decide'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 1 or option == 2):
                    return (option, 'decide', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções')
                continue
    elif (filter == 'interact'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 0):
                    return (option, 'interact', True)
                elif (option >= 1 and option <= 9):
                    return (option, 'interact', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções')
                continue
    else:
        while True:
            try:
                option = input('Sua escolha: ').upper()
                if (option == 'S' or option == 'N'):
                    return (option, 'letter', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções')
                continue


def draw_input_item_select(belt, bag):
    print('X', '-'*50, 'X')
    print('Usar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja selecionar? [1 ao 9] ou [0]')
    return (input_attempts('interact'), 'item_select')


def draw_input_choose_item_drop(belt, bag):
    print('X', '-'*50, 'X')
    print('Largar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja largar? [1 ao 9] ou [0]')
    return (input_attempts('interact'), 'item_drop')


def draw_input_item_found_options(item):
    print('X', '-'*50, 'X')
    print(
        f'''Item encontrado: {item.name}
                [Dano] -> {item.atk} DMG
                [Defesa] -> {item.dfs} DMG
                [Cura] -> {item.hlg} HP
                [Peso] -> {item.weight} kg''')
    print('O que deseja fazer? [1] Pegar [2] Ignorar')
    return (input_attempts('decide'), 'item_found_options')


# Input results functions


def show_item_add_success(item, flag):
    if (flag == 'item_add_to_bag'):
        print(f'{item.name} adicionado a mochila!')
    elif (flag == 'item_add_to_belt'):
        print(f'{item.name} adicionado ao cinto!')


# Level related functions


def draw_top_level_bar(level_info, player):
    clear_screen()
    print('X', '-'*50, 'X')
    print(
        ' '*2, f'Level {level_info.level_number}: {level_info.chapter_name}')
    print(
        ' '*2, f'| {player.name} | HP: {player.hp} | ATK: {player.atk} | DEF: {player.dfs}')
    print('X', '-'*50, 'X', '\n')


def draw_screen_counter(screen_count):
    print(f' [{screen_count}]\n')


def draw_bottom_level_bar():
    print('\n', 'X', '-'*50, 'X')
    input('Avançar >>>')


def print_level_lines(level_info, player, level_content, entry_point):
    screen_count = player.screens

    for line in level_content[entry_point:]:
        new_line, drop = check_line_length(line)

        if (new_line is not None):
            print(f'{new_line}\n{drop}')
            continue

        # line flags
        if (line == '/start'):
            draw_top_level_bar(level_info, player)
            draw_screen_counter(screen_count)
            screen_count += 1
            continue
        elif (line == '/stop'):
            draw_bottom_level_bar()
            continue
        elif (line == '/get_name'):
            print(' '*2, player.name)
            continue
        elif (line in ALL_ITEMS_LIST):
            item = all_items[line]

            user_input = draw_input_item_found_options(item)
            filter_return = filter_inputs(user_input, player, item)

            if (filter_return is False):
                exit()
            elif (filter_return == 'item_add_to_bag'):
                show_item_add_success(item, 'item_add_to_bag')
            elif (filter_return == 'item_add_to_belt'):
                show_item_add_success(item, 'item_add_to_belt')
            continue
        elif (line in ALL_ENEMIES_LIST):
            enemy = all_enemies[line]
            pass

        print(line)


# Combat related functions


def draw_enemy_skills(enemy):
    print('\n'*2, 'X='*26, 'X')

    print(' '*2, 'MODO BATALHA', '\n*2',
          'Você entrou em batalha com um inimigo, suas carateristicas são: ', '\n')
    print(' '*2, f'| {enemy.name} |')
    print(' '*2, f'| HP: {enemy.hp} | ATK: {enemy.atk} | DEF: {enemy.dfs}')

    print('X='*26, 'X', '\n')


def init_level_interface(level_info, player, level_content, entry_point):
    print_level_lines(level_info, player, level_content, entry_point)
