from os import system
from time import sleep

from structures.game_constants import (DEFAULT_HERO_HP,
                                       DEFAULT_HERO_DEFENSE,
                                       DEFAULT_HERO_ATK)
from animations import (timed_writing_animation,
                        menu_transfer_animation,
                        creating_new_game_animation,
                        loading_game_animation)


def clear_screen():
    system('cls || clear')


def invalid_option():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*7, 'Opção Inválida!', '\n')
    print('X', '-'*26, 'X', '\n')
    sleep(2)

    draw_menu_options()


def ask_for_hero_name():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*11, 'pyRPG', '\n')
    print('X', '-'*26, 'X', '\n')
    return str(input('Qual é o nome do seu herói: '))


def create_save_game(hero_name):
    hash_save = str(hash(hero_name))
    save_game_file_name = './saves/save_' + \
        '(' + hero_name + ')' + hash_save + '.txt'

    with open(save_game_file_name, 'x') as save:
        save.write(
            f'{hero_name}\n{DEFAULT_HERO_HP}\n{DEFAULT_HERO_DEFENSE}\n{DEFAULT_HERO_ATK}')

    with open('./src/structures/save_games_info.txt', 'r+') as save_games_info:
        number_of_saves = int(save_games_info.read(1))

        if (number_of_saves == 0):
            save_games_info.seek(0)
            save_games_info.write('1')
            save_games_info.write(f'\n{hero_name}\n')
        else:
            number_of_saves += 1
            save_games_info.seek(0)
            save_games_info.write(str(number_of_saves))
            save_games_info.seek(0)

            saves = save_games_info.readlines()
            saves.append(f'{hero_name}\n')
            save_games_info.seek(0, 2)
            save_games_info.write(f'{hero_name}\n')


def create_new_game():
    hero_name = ask_for_hero_name()

    create_save_game(hero_name)
    creating_new_game_animation()

# TODO: finish check_saved_games function


def check_saved_games():
    with open('./src/structures/save_games_info.txt', 'r+') as save_games_info:
        number_of_saves = int(save_games_info.read(1))

        if (number_of_saves != 0):
            saves = save_games_info.readlines()
            saves.pop(0)
            save_games_info.seek(0)

            for save in saves:
                print(save)


def load_game(game_save):
    loading_game_animation()


def process_option(option):
    if (option == '1'):
        create_new_game()
    elif (option == '2'):
        check_saved_games()
        # load_game()
    elif (option == '3'):
        pass
    else:
        invalid_option()


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
    menu_transfer_animation()


def draw_menu_options():
    clear_screen()
    print('X', '-'*26, 'X', '\n')
    print(' '*10, 'Opções:', ' '*10)
    print('''
    [1] Novo Jogo
    [2] Carregar Jogo
    [3] Sair
    ''')
    print('X', '-'*26, 'X', '\n')

    process_option(str(input('Digite sua opção: ')))


draw_home_screen()
draw_menu_options()
