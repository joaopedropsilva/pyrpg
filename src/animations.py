from time import sleep
from sys import stdout
import keyboard as kb
from utils import clear_screen

from structures.game_constants import DEFAULT_ANIMATION_SPEED


def timed_writing_animation(text, animation_speed=DEFAULT_ANIMATION_SPEED):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        # if (kb.on_press('right')):
        #     animation_speed *= 2
        sleep(animation_speed)


# Menu animations


def menu_transfer_animation():
    pass


def creating_new_game_animation():
    pass


def loading_game_animation():
    clear_screen()
    animacao = ['\\'*52,'\n', '//'*26, '\n']
    
    barra = ['/'*10,' '*10, "[",'-'*10, ' '*0 , "]",' '*10, '\\'*10, '\n']
    timed_writing_animation(animacao*5, 0.2)
    for i in range(len(barra)):
            if i == 3:
                timed_writing_animation(barra[i], 0.5)
            else : timed_writing_animation(barra[i], 0.1)

    timed_writing_animation(animacao*5, 0.2)
