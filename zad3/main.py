"""Terminal game for testing edge cases and checking GitHub Actions"""
import random
import os
import sys
import msvcrt  # pylint: disable=import-error
import termios  # pylint: disable=import-error
import tty  # pylint: disable=import-error
import contextlib  # pylint: disable=import-error

class Game:
    """
    Game in terminal on 5x5 grid. It draws player, treasure and obstacles position.
    You move a player using w, s, a, d keys.
    To quit press q.
    Game ends when player finds a treasure.
    """
    BOARD_SIZE = 5
    OBSTACLE = 'x'
    PLAYER = 'o'
    TREASURE = 'T'
    EMPTY = ' '

    def __init__(self):
        self.player_position = self.place_player_position()
        self.treasure_position = self.place_treasure_position()
        self.board = self.create_board()

    def place_player_position(self):
        """Draws player position"""
        x = random.randint(0, self.BOARD_SIZE - 1)
        return [x, 0]

    def place_treasure_position(self):
        """Draws treasure position"""
        x = random.randint(0, self.BOARD_SIZE - 1)
        return [x, self.BOARD_SIZE - 1]

    def create_board(self):
        """Creates array for board with obstacles"""
        board = [[self.EMPTY for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.place_obstacles(board)
        return board

    def place_obstacles(self, board):
        """Draws field where obstacles will be"""
        for i in range(1, 4):  # Number of obstacles
            x1, y = random.randint(0, self.BOARD_SIZE-1), i
            board[x1][y] = self.OBSTACLE
            x2, y = random.randint(0, self.BOARD_SIZE - 1), i
            while board[x2][y] != self.EMPTY:
                x2, y = random.randint(0, self.BOARD_SIZE - 1), i
            board[x2][y] = self.OBSTACLE

    def print_board(self):
        """Prints board with player and treasure position in terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print('_' * (self.BOARD_SIZE + 2))
        for i in range(self.BOARD_SIZE):
            print('|', end='')
            for j in range(self.BOARD_SIZE):
                if self.player_position == [i, j]:
                    print(self.PLAYER, end='')
                elif self.treasure_position == [i, j]:
                    print(self.TREASURE, end='')
                else:
                    print(self.board[i][j], end='')
            print('|')
        print('_' * (self.BOARD_SIZE + 2))

    def move_player(self, move):
        """Logic for handling player's move"""
        x, y = self.player_position
        if move == 'w' and x > 0 and self.board[x-1][y] != self.OBSTACLE:
            self.player_position = [x-1, y]
        elif move == 's' and x < self.BOARD_SIZE-1 and self.board[x+1][y] != self.OBSTACLE:
            self.player_position = [x+1, y]
        elif move == 'a' and y > 0 and self.board[x][y-1] != self.OBSTACLE:
            self.player_position = [x, y-1]
        elif move == 'd' and y < self.BOARD_SIZE-1 and self.board[x][y+1] != self.OBSTACLE:
            self.player_position = [x, y+1]


def get_keypress_linux():
    """Handles keypress in terminal for Linux"""
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

    return msvcrt.getch().decode().lower()


def main():
    """Main function"""
    game = Game()
    while True:
        game.print_board()
        if game.player_position == game.treasure_position:
            print('You win')
            break
        move = get_keypress_windows() if os.name == 'nt' else get_keypress_linux()
        if move in ['w', 's', 'a', 'd']:
            game.move_player(move)
        elif move == 'q':
            break


if __name__ == "__main__":
    main()
