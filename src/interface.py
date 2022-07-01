from utils import clear_screen, check_line_length


# Input related functions


def input_attempts(filter='letter'):
    if (filter == 'binary'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 1 or option == 2):
                    return (option, 'binary')
                else:
                    raise ValueError
            except ValueError:
                print('Digite apenas alguma das opções!')
                continue
    elif (filter == 'non_binary'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option >= 0 and option <= 9):
                    return (option, 'non_binary')
                else:
                    raise ValueError
            except ValueError:
                print('Digite apenas alguma das opções!')
                continue
    else:
        while True:
            try:
                option = input('Sua escolha: ').upper()
                if (option == 'S' or option == 'N'):
                    return (option, 'letter')
                else:
                    raise ValueError
            except ValueError:
                print('Digite apenas alguma das opções!')
                continue


def draw_input_select_item(belt, bag):
    print('X', '-'*50, 'X')
    print('Usar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja selecionar? [1 ao 9] ou [0]')
    return input_attempts('non_binary')


def draw_input_choose_item_drop(belt, bag):
    print('X', '-'*50, 'X')
    print('Largar itens do cinto ou da mochila')
    print(f'CINTO: {belt} [1 ao 9]')
    print(f'MOCHILA: {bag} [0]')
    print('Qual item deseja largar? [1 ao 9] ou [0]')
    return input_attempts('non_binary')


def draw_input_item_options(item):
    print('X', '-'*50, 'X')
    print(f'O que deseja fazer com {item}')
    print('[1] Usar\n[2] Ver Informações')
    return input_attempts('binary')


def draw_input_get_item():
    print('X', '-'*50, 'X')
    print('Pegar item [S/N]')
    return input_attempts()


def draw_input_drop_item():
    print('X', '-'*50, 'X')
    print('Largar algum item [S/N]')
    return input_attempts()


def draw_input_atk():
    print('X', '-'*50, 'X')
    print('Atacar [S/N]')
    return input_attempts()


def filter_inputs(input):
    option, option_type = input
    if (option_type == 'binary'):
        pass
    elif (option_type == 'non_binary'):
        pass
    else:
        pass


# Combat related functions


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
        elif (line == '\input'):
            continue

        print(line)


def init_level_interface(level_info, player, level_content, entry_point):
    print_level_lines(level_info, player, level_content, entry_point)
