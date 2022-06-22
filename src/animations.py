from time import sleep
from sys import stdout
import keyboard as kb

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
    pass
