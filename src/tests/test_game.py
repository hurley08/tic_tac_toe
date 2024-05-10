# tests/test_game.py
# tests engine.py, players.py, and renderers.py

import pytest

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import Player, DumbComputerPlayer, ComputerPlayer
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as CR
from tic_tac_toe.logic.models import GameState, Grid, Mark


@pytest.fixture
def human_player():
    """Creates a human player instance"""
    player = Player(Mark.CROSS)
    return player


@pytest.fixture
def dumb_player():
    """Creates an automated player that chooses moves randomly"""
    player = DumbComputerPlayer(Mark.CROSS)
    return player


@pytest.fixture
def smart_player():
    """Creates an AI powered player. Not implemented currently"""
    player = ComputerPlayer(Mark.CROSS)
    return player


@pytest.fixture
def TTT_class():
    """Creates an instance of the game engine object"""
    player1 = DumbComputerPlayer(Mark.CROSS)
    player2 = DumbComputerPlayer(Mark.NOUGHT)
    GS = GameState
    GRID = Grid()
    game_state = GS(GRID)
    rend = CR(game_state)
    return TicTacToe(player1=player1, player2=player2, rend=rend, gamestate=game_state)


def test_human_player(human_player, TTT_class):
    """Tests some attributes of a human player"""
    player = human_player
    assert player.mark is Mark.CROSS
    # with mock.patch.object(__builtints__, 'input', lambda:'5'):


def test_TTT_defaults(TTT_class):
    """
    Tests that the instantiated game containes the
    specified nuumber of methods and attr
    """
    GAME = TTT_class
    assert len(dir(GAME)) == 41


def test_default_order(TTT_class):
    """Tests that the default starting player is mark.CROSS"""
    assert TTT_class.current_player is TTT_class.p1
    assert TTT_class.current_mark is TTT_class.current_player.mark
    assert TTT_class.current_player.mark is TTT_class.p1.mark


def test_match_player_types(TTT_class):
    """Tests that the default player types are the same"""
    GAME = TTT_class
    assert GAME.p1 is not GAME.p2
    assert isinstance(GAME.p1, type(GAME.p2))


def test_switch_marks(TTT_class):
    """Tests the method that switches the current Mark"""
    old_mark = TTT_class.current_mark
    TTT_class.switch_marks()
    assert old_mark is TTT_class.current_mark


def test_switch_players(TTT_class):
    """Tests the method that switches the current player"""
    old_player = TTT_class.current_player
    TTT_class.switch_current_player()
    assert old_player is not TTT_class.current_player


def test_who_is_current_player(TTT_class):
    """Tests the get who is current player method"""
    GAME = TTT_class
    assert GAME.who_is_current_player() is GAME.p1
    assert GAME.current_player is GAME.p1
    GAME.switch_current_player()
    assert GAME.who_is_current_player() is GAME.p2
    assert GAME.current_player is GAME.p2


def test_getset_game_status(TTT_class):
    """Tests the get state and set state methods of a game engine"""
    GAME = TTT_class
    assert GAME.state is GAME.get_game_status()
    move = GAME.p1.make_move(GAME.state)
    GAME.set_game_status(move)
    assert GAME.state is move
    assert GAME.get_game_status() is move


def test_pre_play_conditions(TTT_class):
    """Tests default values for game attributes following instantiation"""
    GAME = TTT_class
    assert GAME.state.win is not True
    assert GAME.state.winner is None
    assert GAME.state.tie is False
    assert GAME.state.game_over is not True


def test_post_play_conditions(TTT_class):
    """Tests that game_over is set to true when a game is complete"""
    GAME = TTT_class
    # value = GAME.play()
    assert GAME.state.game_over is True


@pytest.mark.timeout(300)
@pytest.mark.parametrize("n_games", [5, 15, 20, 50])
def test_many_games(TTT_class, n_games):
    """Tests that we can play and log results of multiple games"""
    results = []
    for i in range(n_games):
        GAME = TTT_class
        results.append(GAME.play())
    assert len(results) == n_games


@pytest.mark.timeout(240)
def test_play_until_p1_win(TTT_class):
    """Tests game state attributes after p1 wins a game"""
    marker = False
    while marker is False:
        GAME = TTT_class

        value = GAME.play()
        if value is GAME.p1.mark:
            marker = True
    assert GAME.state.win is True
    assert GAME.state.winner is GAME.p1.mark
    assert GAME.state.game_over is True
    assert GAME.state.tie is False


@pytest.mark.timeout(240)
def test_play_until_p2_win(TTT_class):
    """Tests game state attributes after p2 wins a game"""
    marker = False
    while marker is False:
        GAME = TTT_class
        value = GAME.play()
        if value is GAME.p2.mark:
            marker = True
    assert GAME.state.win is True
    assert GAME.state.winner is GAME.p2.mark
    assert GAME.state.game_over is True
    assert GAME.state.tie is False


@pytest.mark.timeout(240)
def test_play_until_tie(TTT_class):
    """Tests game state attributes after neither player wins"""
    marker = False
    while marker is False:
        GAME = TTT_class
        value = GAME.play()
        if value is None:
            marker = True
    assert GAME.state.win is False
    assert GAME.state.winner is None
    assert GAME.state.game_over is True
    assert GAME.state.tie is not True


@pytest.mark.skip
def test_setting_board_pieces():
    """There is a set method in logic that allows custom input"""
    print("This needs to be implemented")


@pytest.mark.skip
def test_setting_p1_win():
    """Uses the set board method to set up p1 for win and detect win"""
    print("This needs to be implemented")


@pytest.mark.skip
def test_setting_p2_win():
    """Same as the above case but with p2"""
    print("This needs to be implemented")


@pytest.mark.skip
def test_setting_tie():
    """Same as the above case but for a tie"""
    print("This needs to be implemented")


@pytest.mark.skip
def detect_all_win_combos():
    """Parametrize and set all possible winning combos (8) for both players and check detection"""
    print("This needs to be implemented")


def test_TTT_methods(TTT_class):
    """Tests the presence of the following methods in the engine class"""
    methods = [
        "switch_current_player",
        "who_is_current_player",
        "switch_players",
        "set_game_status",
        "play",
    ]
    for i in methods:
        if i not in dir(TTT_class):
            assert i


if __name__ == "__main__":
    pytest.main()
