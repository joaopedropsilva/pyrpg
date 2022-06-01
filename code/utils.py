from os import system

from animations import timed_writing


def clear_screen():
    system('cls || clear')


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
    timed_writing('Press any key to start...')
    input()
