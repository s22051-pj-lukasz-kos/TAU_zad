"""Test only game logic"""
from game import Game


def test_initial_position():
    """Check if player initial position is not the same as treasure position"""
    game = Game()
    assert game.player_position != game.treasure_position


def test_move_up():
    """Check if player could correctly move up"""
    game = Game(seed=1)
    initial_position = game.player_position.copy()
    x, y = initial_position
    game.move_player('w')
    assert game.player_position != initial_position and game.player_position == [x-1, y], \
        "Player should have moved up"


def test_move_down():
    """Check if player could correctly move down"""
    game = Game(seed=1)
    initial_position = game.player_position.copy()
    x, y = initial_position
    game.move_player('s')
    assert game.player_position != initial_position and game.player_position == [x+1, y], \
        "Player should have moved down"


def test_move_right():
    """Check if player could correctly move to the right"""
    game = Game(seed=1)
    initial_position = game.player_position.copy()
    x, y = initial_position
    game.move_player('d')
    assert game.player_position != initial_position and game.player_position == [x, y+1], \
        "Player should have moved to right"


def test_move_left():
    """Check if player could correctly move to the left"""
    game = Game(seed=1)
    game.move_player('d')
    initial_position = game.player_position.copy()
    x, y = initial_position
    game.move_player('a')
    assert game.player_position != initial_position and game.player_position == [x, y-1], \
        "Player should have moved to the left"


def test_left_border():
    """Checks whether the player will not cross the border on the left"""
    game = Game(seed=1)
    initial_position = game.player_position.copy()
    game.move_player('a')
    assert game.player_position == initial_position, "Player should not cross the left border"


def test_upper_border():
    """Checks whether the player will not cross the upper border"""
    game = Game(seed=1)
    game.move_player('w')
    initial_position = game.player_position.copy()
    game.move_player('w')
    assert game.player_position == initial_position, "Player should not cross the upper border"


def test_lower_border():
    """Checks whether the player will not cross the lower border"""
    game = Game(seed=1)
    for _ in range(3):
        game.move_player('s')
    initial_position = game.player_position.copy()
    game.move_player('s')
    assert game.player_position == initial_position, "Player should not cross the lower border"


def test_right_border():
    """Checks whether the player will not cross the right border"""
    game = Game(seed=1)
    for _ in range(2):
        game.move_player('d')
    game.move_player('s')
    for _ in range(2):
        game.move_player('d')
    initial_position = game.player_position.copy()
    game.move_player('d')
    assert game.player_position == initial_position, "Player should not cross the right border"


def test_obstacle():
    """Checks whether the player will not cross an obstacle"""
    game = Game(seed=1)
    for _ in range(2):
        game.move_player('d')
    initial_position = game.player_position.copy()
    game.move_player('d')
    assert game.player_position == initial_position, \
        "Player should not cross obstacle"


def test_get_treasure():
    """Checks if game ends when player gets treasure"""
    game = Game(seed=1)
    assert not game.check_win(), "Player should not win in the beginning of the game"
    for _ in range(3):
        game.move_player('s')
    for _ in range(4):
        game.move_player('d')
    assert game.check_win(), "Player should win when he gets on treasure position"
