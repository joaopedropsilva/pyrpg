from utils import clear_screen, check_line_length


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
