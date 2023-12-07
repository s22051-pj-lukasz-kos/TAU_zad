import random
import os
import sys

# Constants for the game board
BOARD_SIZE = 5
OBSTACLE = 'x'
PLAYER = 'o'
TREASURE = 'T'
EMPTY = ' '


def place_player_position():
    x = random.randint(0, BOARD_SIZE - 1)
    return [x, 0]


def place_treasure_position():
    x = random.randint(0, BOARD_SIZE - 1)
    return [x, BOARD_SIZE - 1]


def create_board():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    place_obstacles(board)
    return board


def place_obstacles(board):
    for i in range(1, 4):  # Number of obstacles
        x1, y = random.randint(0, BOARD_SIZE-1), i
        board[x1][y] = OBSTACLE
        x2, y = random.randint(0, BOARD_SIZE - 1), i
        while board[x2][y] != EMPTY:
            x2, y = random.randint(0, BOARD_SIZE - 1), i
        board[x2][y] = OBSTACLE


def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('_' * (BOARD_SIZE + 2))
    for i in range(BOARD_SIZE):
        print('|', end='')
        for j in range(BOARD_SIZE):
            if player_position == [i, j]:
                print(PLAYER, end='')
            elif treasure_position == [i, j]:
                print(TREASURE, end='')
            else:
                print(board[i][j], end='')
        print('|')
    print('_' * (BOARD_SIZE + 2))


def move_player(move, board):
    global player_position
    x, y = player_position
    if move == 'w' and x > 0 and board[x-1][y] != OBSTACLE:
        player_position = [x-1, y]
    elif move == 's' and x < BOARD_SIZE-1 and board[x+1][y] != OBSTACLE:
        player_position = [x+1, y]
    elif move == 'a' and y > 0 and board[x][y-1] != OBSTACLE:
        player_position = [x, y-1]
    elif move == 'd' and y < BOARD_SIZE-1 and board[x][y+1] != OBSTACLE:
        player_position = [x, y+1]


def get_keypress_linux():
    import termios
    import tty
    import contextlib

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
    import msvcrt
    return msvcrt.getch().decode().lower()


def main():
    board = create_board()
    while True:
        print_board(board)
        if player_position == treasure_position:
            print('You win')
            break
        move = get_keypress_windows() if os.name == 'nt' else get_keypress_linux()
        if move in ['w', 's', 'a', 'd']:
            move_player(move, board)
        elif move == 'q':
            break


if __name__ == "__main__":
    player_position = place_player_position()
    treasure_position = place_treasure_position()
    main()
