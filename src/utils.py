from os import system


def clear_screen():
    system('cls || clear')


def remove_newline(name):
    correct_name = ''

    for letter in name:
        if letter != '\n':
            correct_name += letter
        else:
            break

    return correct_name
