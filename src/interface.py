from utils import clear_screen


def get_player_level_from_save(player_info_loaded):
    return player_info_loaded[-1]


def open_level_file(level):
    level_file_path = './src/levels/' + level + '.txt'

    with open(level_file_path, 'r') as level_file:
        level_content = level_file.readlines()


def draw_top_level_bar():
    clear_screen()
    print('X', '-'*50, 'X')
    print(' '*2, f'Level {level_number}: {chapter_name}')
    print(
        ' '*2, f'| {hero_name} | HP: {hero_hp} | ATK: {hero_atk} | DEF: {hero_def}')
    print('X', '-'*50, 'X', '\n')
