"""Main module for launching game in terminal"""
import sys
import os
from game import Game


def get_keypress_linux():
    """Handles keypress in terminal for Linux"""
    import termios  # pylint: disable=import-error
    import tty  # pylint: disable=import-error
    import contextlib  # pylint: disable=import-error

    @contextlib.contextmanager
    def raw_mode(file):
        old_attrs = termios.tcgetattr(file.fileno())
        new_attrs = old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

    with raw_mode(sys.stdin):
        tty.setcbreak(sys.stdin)
        return sys.stdin.read(1).lower()


def get_keypress_windows():
    """Handles keypress in terminal for Windows"""
    import msvcrt  # pylint: disable=import-error
    return msvcrt.getch().decode().lower()


def main():
    """Main function"""
    game = Game(seed=1)
    while True:
        game.print_board()
        if game.check_win():
            print('You win')
            break
        move = get_keypress_windows() if os.name == 'nt' else get_keypress_linux()
        if move in ['w', 's', 'a', 'd']:
            game.move_player(move)
        elif move == 'q':
            break


if __name__ == "__main__":
    main()
