# tic_tac_toe/logic/validators.py

from __future__ import annotations

from typing import TYPE_CHECKING
from tic_tac_toe.logic.exceptions import InvalidGameState
from tic_tac_toe.game.models import Player

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import GameState, Grid, Mark


def validate_grid(grid: Grid) -> None:
    # if not re.match(r"^XO]{9}$", grid.cells):
    #  raise ValueError("Must contain 9 cells of: X, O, or space")
    if len(grid.cells) != 9:
        raise ValueError("This attribute should be 9 characters long")
    for i in set(grid.cells):
        if i not in ("O", "X", " "):
            raise ValueError("Illegal characters ")
    return True

    # if not re.match("^(?=(OX ){9})", grid.cells):
    #   raise ValueError("Must contain 9 cells of: X, O, or space")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    if game_state.win not in (None, False):
        validate_winner(
            grid=game_state.grid,
            starting_mark=game_state.starting_mark,
            winner=game_state.win,
        )
        validate_winner_refactor(
            grid=game_state.grid,
            starting_mark=game_state.starting_mark,
            winner=game_state.win,
        )


def validate_number_of_marks(game_state: GameState) -> None:
    if abs(game_state.grid.x_count - game_state.grid.o_count) > 1:
        raise InvalidGameState("Abnormal proportion of X's to O's detected")


def validate_starting_mark(game_state: GameState, starting_mark: Mark) -> None:
    if game_state.grid.x_count > game_state.grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Skipped turn detected")
    elif game_state.grid.o_count > game_state.grid.x_count:
        if starting_mark != "O":
            raise InvalidGameState("Skipped turn detected")


def validate_winner_refactor(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:
    """
    The winner will always have an equal number or more marks
    than the starting player.

    if winner is the same as starting player,
    their number of pieces > opponents
    if winner is not the same as starting player,
    their number of pieces <= opponents
    """

    if winner is not None or False:
        counts = grid.both_counts
        winner_count = counts[winner]
        opponent_count = counts[winner.other]

        if winner == starting_mark:
            if not winner_count > opponent_count:
                raise InvalidGameState(
                    "Winner started, number of"
                    "pieces must be greater than"
                    "opponent's"
                )
        if winner.other == starting_mark:
            if not winner_count <= opponent_count:
                raise InvalidGameState(
                    "Winner did not start and"
                    "cannot have more pieces"
                    "opponent"  # noqa: E501
                )


def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:  # noqa: E501
    """
    The winner will always have an equal number or more marks
    than the starting player.

    if winner is the same as starting player,
    their number of pieces > opponents
    if winner is not the same as starting player,
    their number of pieces <= opponents
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
