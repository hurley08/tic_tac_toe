from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.game.player import Player
    from tic_tac_toe.logic.models import GameState, Grid, Mark

import re

from tic_tac_toe.logic.exceptions import InvalidGameState

def validate_grid(grid: Grid) -> None:
    if not re.match(r"^XO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")
    
def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)

def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Abnormal proportion of X's to O's detected")
    
def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Skipped turn detected")
    elif grid.o_count > grid.x_count:
        if starting_mark != "O":
            raise InvalidGameState("Skipped turn detected")

def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:
    """ 
    The winner will always have an equal number or more marks
    than the starting player. 

    if winner is the same as starting player, their number of pieces > opponents
    if winner is not the same as starting player, their number of pieces <= opponents
    """
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong number of Os")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Wrong number of Os")

def validate_players(player1: Player, player2: Player) -> None:
    if player1.mark is player2.mark:
        raise ValueError("Players must use different marks")