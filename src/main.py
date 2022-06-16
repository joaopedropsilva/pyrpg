import menu
import interface
import utils
import animations


def main():
    menu.draw_home_screen()

    while True:
        menu.draw_menu_options()
        process_return = menu.process_option(
            str(input('Digite sua opção: ')))

        if(process_return is False):  # quit game
            break
        # TODO: terminar o if, o que acontece com os outros processos

    print(process_return)


if __name__ == '__main__':
    main()
