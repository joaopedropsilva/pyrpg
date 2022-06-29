import menu
import interface as interf
import utils as utl
import animations as anm


def main():
    menu.draw_home_screen()

    while True:
        menu.draw_menu_options()
        user_option = str(input('Digite sua opção: '))
        process_return = menu.process_option(user_option)

        if(process_return is False):  # quit game
            break

        if (user_option == '1' and process_return != None):  # create new game
            level_info, player, level_content = utl.init_level(process_return)
            interf.init_level_interface(level_info, player, level_content)

        elif (user_option == '2' and process_return != None):  # load game
            level_info, player, level_content = utl.init_level(process_return)
            interf.init_level_interface(level_info, player, level_content)

        utl.autosave(level_info, player)


if __name__ == '__main__':
    main()
