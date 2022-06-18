from utils import clear_screen


def draw_top_level_bar(level_info, player):
    clear_screen()
    print('X', '-'*50, 'X')
    print(
        ' '*2, f'Level {level_info.level_number}: {level_info.chapter_name}')
    print(
        ' '*2, f'| {player.name} | HP: {player.hp} | ATK: {player.atk} | DEF: {player.dfs}')
    print('X', '-'*50, 'X', '\n')


def init_level_interface(level_info, player):
    draw_top_level_bar(level_info, player)
    input()


# TODO: Fazer função quebra nos 54 caracteres e caso a quebra for numa palavra, voltar até um espaço
