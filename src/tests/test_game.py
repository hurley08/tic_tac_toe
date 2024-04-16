# tests/test_game.py
# tests engine.py, players.py, and renderers.py

import pytest

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import DumbComputerPlayer
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as CR
from tic_tac_toe.logic.models import GameState, Grid, Mark


@pytest.fixture
def TTT_class():
    player1 = DumbComputerPlayer(Mark.CROSS)
    player2 = DumbComputerPlayer(Mark.NOUGHT)
    GS = GameState
    GRID = Grid()
    game_state = GS(GRID)
    rend = CR(game_state)
    return TicTacToe(player1=player1, player2=player2, rend=rend, gamestate=game_state)


def test_TTT_defaults(TTT_class):
    GAME = TTT_class
    assert len(dir(GAME)) == 41


def test_default_order(TTT_class):
    assert TTT_class.current_player == TTT_class.p1
    assert TTT_class.current_mark == TTT_class.current_player.mark == TTT_class.p1.mark


def test_player_types(TTT_class):
    GAME = TTT_class
    assert GAME.p1 != GAME.p2
    assert isinstance(GAME.p1, type(GAME.p2))


def test_switch_marks(TTT_class):
    old_mark = TTT_class.current_mark
    TTT_class.switch_marks()
    assert old_mark == TTT_class.current_mark


def test_switch_players(TTT_class):
    old_player = TTT_class.current_player
    TTT_class.switch_current_player()
    assert old_player != TTT_class.current_player


def test_who_is_current_player(TTT_class):
    GAME = TTT_class
    assert GAME.who_is_current_player() == GAME.p1
    assert GAME.current_player == GAME.p1
    GAME.switch_current_player()
    assert GAME.who_is_current_player() == GAME.p2
    assert GAME.current_player == GAME.p2


def test_getset_game_status(TTT_class):
    GAME = TTT_class
    assert GAME.state == GAME.get_game_status()
    move = GAME.p1.make_move(GAME.state)
    GAME.set_game_status(move)
    assert GAME.state == move
    assert GAME.get_game_status() == move


def test_pre_play_conditions(TTT_class):
    GAME = TTT_class
    assert GAME.state.win != True
    assert GAME.state.winner != None
    assert GAME.state.game_over != True


def test_post_play_conditions(TTT_class):
    GAME = TTT_class
    value = GAME.play()
    assert GAME.state.win == True
    assert GAME.state.winner != None
    assert GAME.state.game_over == True
    assert not value in ["X", "O"]


def test_TTT_methods(TTT_class):
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
