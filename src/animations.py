from time import sleep
from sys import stdout

from utils import clear_screen
from structures.game_constants import DEFAULT_ANIMATION_SPEED
from interface import draw_level_advance


def timed_writing_animation(text, animation_speed=DEFAULT_ANIMATION_SPEED):
    for letter in text:
        stdout.write(letter)
        stdout.flush()

        sleep(animation_speed)


# Menu animations


def menu_transfer_animation():
    pass


def creating_new_game_animation():
    animation = [['HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHHHHHHHHHHH|||||||||HHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHHHHHH|||||||||||||||||||HHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHH||||||||||HHHHHHHHH||||||HHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHH|||||||||||HHHHHHHHHHHHHHH|||HHHHHHHHHH\n'],
                 ['HHHHHHHHHHHH|||||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHH||||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHH|||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHH||||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHH|||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHH||||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHH|||||||||||HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHH|||||||||||HHHHHHHHHHHHHHH|||HHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHH||||||||||HHHHHHHHH||||||HHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHHHHHH|||||||||||||||||||HHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHHHHHHHHH|||||||||||HHHHHHHHHHHHHHHHH\n'],
                 ['HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n'] ]
    
    for i in range(len(animation)):
        
        timed_writing_animation(animation[i], 0.1)


def level_advance_animation(level_info):
    clear_screen()
    animation = ['\\'*52, '\n', '//'*26, '\n']

    bar = ['/'*10, ' '*10, "[", '-'*10, ' '*0, "]", ' '*10, '\\'*10, '\n']
    timed_writing_animation(animation*5, 0.1)
    for i in range(len(bar)):
        if i == 3:
            timed_writing_animation(bar[i], 0.25)
        else:
            timed_writing_animation(bar[i], 0.05)

    timed_writing_animation(animation*5, 0.1)

    draw_level_advance(level_info.level_number)
