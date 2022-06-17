import menu
import interface as interf
import animations as anm


def main():
    menu.draw_home_screen()

    while True:
        menu.draw_menu_options()
        user_option = str(input('Digite sua opção: '))
        process_return = menu.process_option(user_option)

        if(process_return is False):  # quit game
            break

        if (user_option == '1' and process_return == 'create_game'):  # create new game
            pass
        elif (user_option == '2' and process_return != None):  # load game
            interf.open_level_file(
                interf.get_player_level_from_save(process_return))


if __name__ == '__main__':
    main()
