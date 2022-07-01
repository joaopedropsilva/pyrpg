from utils import clear_screen, check_line_length, get_selected_item


# Input related functions


def input_attempts(filter='letter'):
    if (filter == 'decide'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 1 or option == 2 or option == 3):
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


def draw_input_iem_select(belt, bag):
    print('X', '-'*50, 'X')
    print('Usar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja selecionar? [1 ao 9] ou [0]')
    return (input_attempts('interact'), 'iem_select')


def draw_input_choose_item_drop(belt, bag):
    print('X', '-'*50, 'X')
    print('Largar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja largar? [1 ao 9] ou [0]')
    return (input_attempts('interact'), 'item_drop')


def draw_input_item_found_options(item):
    print('X', '-'*50, 'X')
    print(f'O que deseja fazer com {item}?')
    print('[1] Pegar [2] Ver Informações [3] Ignorar')
    return (input_attempts('decide'), 'item_options')


def draw_input_atk():
    print('X', '-'*50, 'X')
    print('Atacar [S/N]')
    return (input_attempts(), 'atk')

# Test


def draw_item_selected(item):
    print('X', '-'*50, 'X')
    print(f'{item} selecionado!')


def filter_inputs(input, player):
    input_response, context = input
    option, option_type, bag_use_flag = input_response

    if (option_type == 'decide' and context == 'item_options'):
        if (option == 1):
            pass
    elif (option_type == 'interact'):
        if (context == 'iem_select' and bag_use_flag is False):
            item = get_selected_item(option-1, player.belt)
            draw_item_selected(item)
        elif (context == 'iem_select' and bag_use_flag is True):
            item = get_selected_item(option, player.bag, bag_use_flag)
            draw_item_selected(item)
        elif (context == 'item_drop'):
            pass
    else:
        if (context == 'get_item'):
            pass
        elif (context == 'drop_item'):
            pass
        elif (context == 'atk'):
            pass

# Combat related functions


def draw_enemy_skills(enemy):

    print('\n'*2, 'X='*26, 'X')

    print(' '*2, 'MODO BATALHA', '\n*2',
          'Você entrou em batalha com um inimigo, suas carateristicas são: ', '\n')
    print(' '*2, f'| {enemy.name} |')
    print(' '*2, f'| HP: {enemy.hp} | ATK: {enemy.atk} | DEF: {enemy.dfs}')

    print('X='*26, 'X', '\n')


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
        if (line == '\start'):
            draw_top_level_bar(level_info, player)
            draw_screen_counter(screen_count)
            screen_count += 1
            continue
        if (line == '\stop'):
            draw_bottom_level_bar()
            continue
        elif (line == '\get_name'):
            print(' '*2, player.name)
            continue
        elif (line == '\input_item_found'):
            draw_input_item_found_options()
        elif (line == '\combat'):
            pass

        print(line)


def init_level_interface(level_info, player, level_content, entry_point):
    print_level_lines(level_info, player, level_content, entry_point)
