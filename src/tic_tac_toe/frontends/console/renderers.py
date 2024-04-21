# frontends/console/renderers.py

import textwrap
import time
from typing import Iterable

from tic_tac_toe.logic.models import GameState


class ConsoleRenderer(GameState):
    """
    This class accepts a gamestate object, checks the X's and O's
    placement in that object and draws a board. An embellishment is
    drawn if win state is detected in the object
    """

    def __init__(self, game_state):
        """Inherits the game_state as its own"""
        super().__init__("rndr")
        self.active = True
        self.game_state = game_state

    def update_gs(self, game_state: GameState) -> None:
        """Allows to ConsoleRenderer to modify the GameState of the object it receives"""
        self.game_state = game_state

    def render2_(self) -> None:
        """I can't recall what this is for"""
        if self.game_state.win not in (False, None):
            print_solid(self.game_state.grid.cells)

    def render(self) -> None:
        """Determines if a win has happened and prints a board that represents the game"""
        clear_screen()
        if self.game_state.win:
            if self.game_state.winner in ["X", "O"]:
                print_solid(self.game_state.grid.cells)
                # print_blinking(game_state.grid.cells, game_state.winning_cells)
                blink(f"{self.game_state.winner} wins \N{party popper}")
                time.sleep(1)
                # game_state.grid.cells, game_state.winning_cells)
                # print(f"{game_state.winner} wins \N{party popper}")
            else:
                print_solid(self.game_state.grid.cells)
                if self.game_state.game_over is True and self.game_state.win is False:
                    print("No one wins this time \N{neutral face}")
        else:
            print_solid(self.game_state.grid.cells)
        return self.game_state.winner


def clear_screen() -> None:
    """Wipe the terminal window"""
    print("\033c", end="")


def blink(text: str) -> str:
    """Blinks text on terminal. Used to embellish winner"""
    for i in range(5):
        substr1 = "\033[5m\r"
        substr2 = "\033[0m\r"
        print(substr1, text, end="", flush=True)
        print(substr2, end="", flush=True)
        time.sleep(0.25)
        print("               ", end=i)

    time.sleep(0.5)
    return substr1


def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    """
    This was intended to print a board and embellish the pieces that resulted in the win but
    this is non-functional
    """
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)


def print_solid(cells: Iterable[str]) -> None:
    """
    prints the board
    """
    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}
    """
        ).format(*cells)
    )
