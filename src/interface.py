from utils import clear_screen


def open_save_info_as_array(save_info_loaded):
    pass


def open_level_file():
    pass


def draw_top_level_bar():
    clear_screen()
    print('X', '-'*50, 'X')
    print(' '*2, f'Level {level_number}: {chapter_name}')
    print(
        ' '*2, f'| {hero_name} | HP: {hero_hp} | ATK: {hero_atk} | DEF: {hero_def}')
    print('X', '-'*50, 'X', '\n')
