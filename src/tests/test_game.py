# tests/test_game.py
# tests engine.py, players.py, and renderers.py

import pytest

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import DumbComputerPlayer
from tic_tac_toe.game.renderers import Renderer
from frontends.console.renderers import ConsoleRenderer as CR

# from tic_tac_toe.logic.exceptions import InvalidMove, InvalidGameState
from tic_tac_toe.logic.models import GameState, Grid, Mark


@pytest.fixture
def test_TTT_class():
    player1 = DumbComputerPlayer(Mark.CROSS)
    player2 = DumbComputerPlayer(Mark.NOUGHT)
    rend = CR(Renderer())
    GS = GameState
    GRID = Grid()
    game_state = GS(GRID)
    return TicTacToe(player1=player1, player2=player2, rend=rend, gamestat=game_state)


def test_TTT_defaults(test_TTT_class):
    GAME = test_TTT_class
    assert type(GAME) == "tic_tac_toe.game.engine.TicTacToe"
    assert len(dir(GAME)) == 40


def test_default_order(test_TTT_class):
    assert TTT_class.current_player == TTT_class.p1
    assert TTT_class.current_mark == TTT_class.current_player.mark == TTT_class.p1.mark


def test_switch_marks(test_TTT_class):
    old_mark = TTT_class.current_mark
    TTT_class.switch_marks()
    assert old_mark != TTT_class.current_mark


def test_switch_players(test_TTT_class):
    old_player = TTT_class.current_player
    TTT_class.switch_current_player()
    assert old_player != TTT_class.current_player


def test_TTT_methods(test_TTT_class):
    methods = [
        "switch_current_player",
        "who_is_current_player",
        "switch_players",
        "set_game_status",
        "play",
    ]
    for i in methods:
        if i not in dir(test_TTT_class):
            assert i


if __name__ == "__main__":
    pytest.main()
