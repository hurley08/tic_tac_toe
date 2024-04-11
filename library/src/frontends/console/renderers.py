# frontends/console/renderers.py

import textwrap
import time
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState

class ConsoleRenderer(Renderer):
    def __init__(self, Renderer, game_state):
        self.active = True
        self.Renderer = Renderer
        self.GS = game_state
    
    def update_gs(self, game_state: GameState) -> None:
        self.GS = game_state

    def render2(self) -> None:
        if not self.GS.win in (False, None):
            print_solid(self.GS.grid.cells)
    
    def render(self) -> None:
        clear_screen()
        if self.GS.win: 
            if self.GS.winner in ["X", "O"]:
                print_solid(self.GS.grid.cells)
                #print_blinking(game_state.grid.cells, game_state.winning_cells)
                blink(f"{self.GS.winner} wins \N{party popper}")
                    #game_state.grid.cells, game_state.winning_cells)
                #print(f"{game_state.winner} wins \N{party popper}")
            else:
                print_solid(self.GS.grid.cells)
                if self.GS.game_over == True and self.GS.win == False:
                    print("No one wins this time \N{neutral face}")
            print(self.GS)

def clear_screen() -> None:
    print("\033c", end="")

def blink(text: str) -> str:
    for i in range(5):
        print("\033[5m\r", text, end="",flush=True) 
        print("\033[0m\r", end="",flush=True)
        time.sleep(.05)
        print("               ", end="")
        
    time.sleep(2)
    print("\n",text)

def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)

def print_solid(cells: Iterable[str]) -> None:
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
