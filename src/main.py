import menu
import interface as interf
import utils as utl
import animations as anm


def main():
    menu.draw_home_screen()
    level_advance_status = False

    while True:
        if (level_advance_status is False):
            menu.draw_menu_options()
            user_option = str(input('Digite sua opção: '))
            process_return = menu.process_option(user_option)

        if(process_return is False):  # quit game
            break

        if (user_option == '1' and process_return != None):  # create new game
            level_info, player, level_content = utl.init_level(
                process_return, False)
            entry_point = utl.get_entry_point_to_level(level_info, player)

            anm.creating_new_game_animation()

            level_advance_status = interf.init_level_interface(
                level_info, player, level_content, entry_point)

            utl.autosave(level_info, player)

            if (level_advance_status is True):
                utl.change_level_info_procedure(level_info, player)
                utl.autosave(level_info, player)

                anm.level_advance_animation(level_info)

                user_option = '2'
                process_return = menu.load_game(player.name)
            elif (level_advance_status == 'end_game'):
                pass

        elif (user_option == '2' and process_return != None):  # load game
            level_info, player, level_content = utl.init_level(
                process_return, True)
            entry_point = utl.get_entry_point_to_level(level_info, player)

            level_advance_status = interf.init_level_interface(
                level_info, player, level_content, entry_point)

            utl.autosave(level_info, player)

            if (level_advance_status is True):
                utl.change_level_info_procedure(level_info, player)
                utl.autosave(level_info, player)

                anm.level_advance_animation(level_info)

                user_option = '2'
                process_return = menu.load_game(player.name)
            elif (level_advance_status == 'end_game'):
                break


if __name__ == '__main__':
    main()
