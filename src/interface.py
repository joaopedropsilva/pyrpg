from utils import clear_screen
from time import sleep  # Substitute for timed_writing_animation

from utils import check_line_length


def draw_top_level_bar(level_info, player):
    clear_screen()
    print('X', '-'*50, 'X')
    print(
        ' '*2, f'Level {level_info.level_number}: {level_info.chapter_name}')
    print(
        ' '*2, f'| {player.name} | HP: {player.hp} | ATK: {player.atk} | DEF: {player.dfs}')
    print('X', '-'*50, 'X', '\n')


def print_level_lines(level_content):
    for line in level_content:
        new_line, drop = check_line_length(line)

        if (new_line is not None):
            print(f'{new_line}\n{drop}')
            continue

        # line flags
        if (line == '\clear'):
            sleep(5)
            clear_screen()
            continue
        elif (line == '\input'):
            pass

        print(line)


def init_level_interface(level_info, player, level_content):
    draw_top_level_bar(level_info, player)
    print_level_lines(level_content)
    input()
