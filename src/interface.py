from structures.game_constants import ALL_ENEMIES_LIST, ALL_ITEMS_LIST, DEFAULT_HERO_BELT_LENGTH
from utils import (clear_screen, check_line_length,
                   check_inventory_state,
                   filter_inputs,
                   get_selected_item)
from game import all_items, all_enemies, battle_atk


# Input functions


def input_attempts(filter, player=None, bag_state=False):
    if (filter == 'decide'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 1 or option == 2):
                    return (option, 'decide', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções válidas')
                continue
    elif (filter == 'interact'):
        while True:
            try:
                option = int(input('Sua escolha: '))
                if (option == 0 and bag_state is False):
                    raise ValueError
                elif (option == 0 and bag_state is True):
                    return (option, 'interact', True)
                elif (option >= 1 and option <= DEFAULT_HERO_BELT_LENGTH and len(player.belt) >= option):
                    return (option, 'interact', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções válidas')
                continue
    else:
        while True:
            try:
                option = input('Sua escolha: ').upper()
                if (option == 'S' or option == 'N'):
                    return (option, 'yes_or_no', False)
                else:
                    raise ValueError
            except ValueError:
                print('[!] Digite apenas alguma das opções válidas')
                continue


def draw_input_item_select(player, reason):
    print('='*54)
    print(f'Usar itens do cinto ou da mochila para {reason}')
    bag_repr, bag_state = check_inventory_state(player)
    print(f'CINTO: {player.belt} [1 ao 4]')
    print(f"MOCHILA: ['{bag_repr}'] [0]")
    print('Qual item deseja selecionar? [1 ao 4] ou [0]')
    return (input_attempts('interact', player, bag_state), 'item_select')


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


# Battle Mode input functions


def draw_input_atk(player):
    return draw_input_item_select(player, 'atacar')


# Input results functions


def show_item_add_success(item, flag):
    if (flag == 'item_add_to_bag'):
        print(f'{item.name} adicionado a mochila!')
    elif (flag == 'item_add_to_belt'):
        print(f'{item.name} adicionado ao cinto!')


def show_atk_success(entity_one, entity_two, damage):
    print('='*54)
    print(f'\n{entity_one.name} atacou {entity_two.name} com {damage} de dano!')


def show_battle_end(entity_one, entity_two):
    print('='*54)
    print(f'\n{entity_one.name} finalizou {entity_two.name}!')


# Level functions


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
    print('')
    print('X', '-'*50, 'X')
    return input('Avançar [ou "Q" para sair] >>>').upper()


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
            player.screens = screen_count
            screen_count += 1
            continue
        elif (line == '/stop'):
            action = draw_bottom_level_bar()

            if (action == 'Q'):
                break
            continue
        elif (line == '/get_name'):
            print(' '*2, player.name)
            continue
        elif (line in ALL_ITEMS_LIST):
            item = all_items[line]

            user_input = draw_input_item_found_options(item)
            filter_return = filter_inputs(user_input, player, None, item)

            if (filter_return is False):
                exit()
            elif (filter_return == 'item_add_to_bag'):
                show_item_add_success(item, 'item_add_to_bag')
            elif (filter_return == 'item_add_to_belt'):
                show_item_add_success(item, 'item_add_to_belt')

            player.screens = screen_count
            continue
        elif (line in ALL_ENEMIES_LIST):
            enemy = all_enemies[line]

            draw_battle_mode(player, enemy)
            continue
        elif (line == '/aurora_death'):
            enemy = all_enemies['/hero_daughter']

            draw_aurora_death(player, enemy)
            continue
        elif (line == '/end'):
            return True

        print(line)

    return False

# Combat functions


def draw_battle_mode(player, enemy):
    print('')
    print('X='*26 + 'X\n')

    print(' '*4, 'MODO BATALHA\n')
    print(' '*2, 'Você entrou em batalha com um inimigo:')
    print(
        ' '*2, f'| {enemy.name} | HP: {enemy.hp} | ATK: {enemy.atk} | DEF: {enemy.dfs}\n')

    entity_one = player
    entity_two = enemy
    entity_two_default_hp = int(enemy.hp)
    winner = False
    while not (winner):
        if (entity_one == player):
            user_input = draw_input_atk(entity_one)
            atk_item = filter_inputs(user_input, entity_one)

            entity_two_new_hp, damage = battle_atk(
                entity_one, entity_two, atk_item.atk)
        else:
            entity_two_new_hp, damage = battle_atk(
                entity_one, entity_two)

        entity_two.hp = entity_two_new_hp - int(entity_two.dfs)

        if (entity_two_new_hp == 0):
            winner = True
            show_battle_end(entity_one, entity_two)
            enemy.hp = entity_two_default_hp
        else:
            show_atk_success(entity_one, entity_two, damage)

        entity_one, entity_two = entity_two, entity_one

    print('')
    print('X='*26 + 'X')


def draw_aurora_death(player, enemy):
    atk_item = get_selected_item(1, player)
    aurora_new_hp, damage = battle_atk(player, enemy, atk_item.atk)

    print('\nAcabe com o sofrimento! Aurora só tem 1 de hp,\né só um hit...')
    input('Atacar >>>')

    if (aurora_new_hp == 0):
        print('='*54)
        print(
            f'\n\t\t{player.name} mata {enemy.name}\n\tempunhando sua lança no coração da filha!\n')
        print('='*54)


def init_level_interface(level_info, player, level_content, entry_point):
    return print_level_lines(level_info, player, level_content, entry_point)
