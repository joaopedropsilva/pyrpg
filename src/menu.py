from time import sleep
from os import path, remove

from structures.game_constants import (DEFAULT_HERO_HP,
                                       DEFAULT_HERO_DEFENSE,
                                       DEFAULT_HERO_ATK)
from animations import timed_writing_animation

from utils import clear_screen, remove_newline


# TODO: extend function to several flows, error flows and any invalid options

def invalid_option():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*7, 'Opção Inválida!', '\n')
    print('X', '-'*26, 'X', '\n')
    sleep(2)


def ask_for_hero_name():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*11, 'pyRPG', '\n')
    print('X', '-'*26, 'X', '\n')
    return str(input('Qual é o nome do seu herói: '))


def create_save_game(hero_name):
    save_game_file_name = './saves/save_' + hero_name + '.txt'

    try:
        with open(save_game_file_name, 'x') as save:
            save.write(
                f'{hero_name}\n{DEFAULT_HERO_HP}\n{DEFAULT_HERO_ATK}\n{DEFAULT_HERO_DEFENSE}\nlvl_0')
    except FileExistsError:
        print(
            '\nUm herói com este nome já foi criado.\nPor favor escolha outro nome!')
        print('Voltando ao menu principal...')
        sleep(2)

        return None

    with open('./src/structures/save_games_info.txt', 'r+') as save_games_info:
        number_of_saves = int(save_games_info.read(1))

        if (number_of_saves == 0):
            save_games_info.seek(0)
            save_games_info.write('1\n')
            save_games_info.write(f'{hero_name}\n')
        else:
            number_of_saves += 1
            save_games_info.seek(0)
            save_games_info.write(str(number_of_saves))
            save_games_info.seek(0)

            saves = save_games_info.readlines()
            saves.append(f'{hero_name}\n')
            save_games_info.seek(0, 2)
            save_games_info.write(f'{hero_name}\n')
    return 'create_game'


def create_new_game():  # returns None if process failed or 'create_game' if it worked
    hero_name = ask_for_hero_name()

    return create_save_game(hero_name)


def get_saves_from_save_games_info(save_format='standard'):
    with open('./src/structures/save_games_info.txt', 'r') as save_games_info:
        saves = save_games_info.readlines()

        if (save_format == 'standard'):
            saves.pop(0)
        elif (save_format == 'full'):
            pass
        else:
            raise Exception('[Error] Specify argument: full or standard only!')

        saves = list(map(remove_newline, saves))
    return saves


def show_saved_games_on_screen(saves):
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*7, 'Jogos Salvos', '\n')
    print('X', '-'*26, 'X', '\n')

    count = 1
    for save in saves:
        print(f'[{count}] ' + save)
        count += 1


def show_no_saved_games_warning():
    print('\nNão há salvamentos de jogos!\nVoltando ao menu...')
    sleep(2)


def get_user_save_game_choice(saves):
    try:
        max_choice = len(saves)-1
        min_choice = 0
        save_choice = int(
            input('\nQual jogo que deseja carregar? (Digite o número apenas): ')) - 1

        if (save_choice < min_choice or save_choice > max_choice):
            invalid_option()
            return None

        return saves[save_choice]
    except ValueError:
        print('\nDigite um número apenas!\nVoltando ao menu principal...')
        sleep(2)
        return None


def check_saved_games():
    saves = get_saves_from_save_games_info('full')

    number_of_saves = int(saves[0])

    if (number_of_saves != 0):
        saves.pop(0)

        show_saved_games_on_screen(saves)
        return get_user_save_game_choice(saves)
    else:
        show_no_saved_games_warning()
        return None


def load_game(game_save):
    save_game_file_name = './saves/save_' + str(game_save) + '.txt'
    with open(save_game_file_name, 'r') as save:
        raw_save_to_load_info = save.readlines()
        save_to_load_info = list(map(remove_newline, raw_save_to_load_info))

    return save_to_load_info


def get_delete_choice():
    saves = get_saves_from_save_games_info()

    max_choice = len(saves)-1
    min_choice = 0

    try:
        delete_choice = int(
            input('\nQual jogo que deseja deletar? (Digite o número apenas): ')) - 1

        if (delete_choice < min_choice or delete_choice > max_choice):
            invalid_option()
            return None

        return saves[delete_choice]
    except ValueError:
        print('\nDigite um número apenas!\nVoltando ao menu principal...')
        sleep(2)
        return None

# FIXME: check function procedure, maybe it's doing work not needed


def delete_save_from_save_games_info(delete_choice):
    saves = get_saves_from_save_games_info('full')
    new_number_of_saves = int(saves[0]) - 1
    saves.pop(0)

    saves.insert(0, str(new_number_of_saves))

    with open('./src/structures/save_games_info.txt', 'w') as save_games_info:
        if (saves[0] == '0\n'):
            save_games_info.write('0\n')
            return

        for save in saves:
            if save != delete_choice:
                save_games_info.write(save + '\n')


def delete_save(delete_choice):
    file_path = './saves/save_' + str(delete_choice) + '.txt'

    if (path.exists(file_path)):
        delete_save_from_save_games_info(delete_choice)
        remove(file_path)
        return 'delete_complete'


def exit_message():
    print('\nSaindo do jogo!')
    sleep(1)


def process_option(option):
    if (option == '1'):
        return create_new_game()
    elif (option == '2'):
        save_to_load = check_saved_games()
        if (save_to_load is None):
            return None
        return load_game(save_to_load)
    elif (option == '3'):
        saves = get_saves_from_save_games_info('full')

        if (saves[0] == '0'):
            show_no_saved_games_warning()
            return None
        else:
            saves.pop(0)
            show_saved_games_on_screen(saves)

        delete_choice = get_delete_choice()

        return delete_save(delete_choice)
    elif (option == '4'):
        exit_message()
        return False
    else:
        invalid_option()
        return


def draw_home_screen():
    clear_screen()
    print('!'*26)
    print('!'*6, ' '*12, '!'*6)
    print('!'*3, ' '*18, '!'*3, '\n')
    print(' '*9, 'pyRPG', ' '*10, '\n')
    print('!'*3, ' '*18, '!'*3)
    print('!'*6, ' '*12, '!'*6)
    print('!'*26)
    print('!'*3, ' '*18, '!'*3, '\n')
    timed_writing_animation('Press any key to start...')
    input()


def draw_menu_options():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*10, 'Opções:', ' '*10)
    print('''
    [1] Novo Jogo
    [2] Carregar Jogo
    [3] Deletar um Jogo Salvo
    [4] Sair
    ''')
    print('X', '-'*26, 'X', '\n')
