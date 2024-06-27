# tic_tac_toe/logic/models.py

from __future__ import annotations

import enum
import StrEnum
import re
from dataclasses import dataclass
from functools import cached_property
from tic_tac_toe.logic.exceptions import InvalidMove

# from tic_tac_toe.logic.validators import validate_game_state, validate_grid

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)

en = enum.StrEnum
class Mark(StrEnum):
    """
    Class to manage active symbols
    """

    CROSS = "X"
    NOUGHT = "O"

    @property
    def other(self) -> Mark:
        """
        To easily refer to the opposite mark
        """
        return Mark.CROSS if self is Mark.NOUGHT else Mark.NOUGHT

    @property
    def whois(self) -> Mark:
        """
        Check identity
        """
        return "CROSS" if self is Mark.CROSS else "NOUGHT"


class Grid:
    """
    Class that governs the board
    Parent of GameState
    """

    def __init__(self, cells=" " * 9):
        """
        Create a list of 9 empty spaces when instantiated
        """
        self.cells = cells

    def check_cells(self):
        """
        Validate the current board configuration
        """
        if len(self.cells) != 9:
            return ValueError("Must consist of 9 characters")
        if not re.match(r"^[\sX0]{9}$", self.cells):
            return ValueError("Must contain only X, O, or space")
        if self.sp_count + self.x_count + self.o_count != 9:
            return ValueError("Grid must have exactly 9 symbols")
        return True

    def set_cells(self, cell):
        """
        Attempts to assign a custom grid configuration
        """

        old_cells = self.cells
        self.cells = cell
        res = self.check_cells()
        if res:
            return True
        else:
            self.cells = old_cells
            return False

    def total_count(self) -> int:
        """
        counts the number of symbols in a grid
        """
        return len(self.cells)

    def both_counts(self) -> dict:
        """
        counts the non-space symbols in a grid
        """
        counts = {}
        counts["X"] = self.cells.count("X")
        counts["O"] = self.cells.count("O")
        return counts

    def x_count(self) -> int:
        """
        counts X's in a grid
        """
        return self.cells.count("X")

    def o_count(self) -> int:
        """
        counts O's in a grid
        """
        return self.cells.count("O")

    def sp_count(self) -> int:
        """
        counts spaces in a grid
        """
        return self.cells.count(" ")


@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"


@dataclass
class GameState:
    """
    Class that manages internal states of game
    instatiated with a grid object
    """

    def __init__(self, grid=Grid):
        # There are 6 unique game states
        self.grid = grid
        self.starting_mark: Mark = Mark("X")
        self.win: bool = False
        self.game_over: bool = False
        self.winner = None
        self.tie: bool = False
        # validate_game_state(self)

    @cached_property
    def get_counts(self) -> dict:
        """
        Creates a dictionary of symbol counts
        """
        count_dict = {}
        count_dict["X"] = self.grid.x_count()
        count_dict["0"] = self.grid.o_count()
        count_dict["-"] = self.grid.sp_count()
        return count_dict

    @cached_property
    def current_mark(self) -> Mark:
        """
        Returns the active mark
        """
        if self.grid.x_count() == self.grid.o_count():
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        """
        Counts number of spaces and infers if game has started
        """
        return self.grid.sp_count() == 9

    @cached_property
    def is_game_over(self) -> bool:
        """
        Returns True if game is finished
        """
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        """
        Cells are all filled and no winner
        """
        return self.winner is None and self.grid.sp_count() == 0

    @cached_property
    def is_winner(self) -> Mark | None:
        """
        Checks if winning pattern on grid
        THIS SHOULD BE CHANGED TO check_win
        """
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    self.win = True
                    self.game_over = True
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        """
        Identify the cells which triggered the win
        """
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start() for match in re.finditer(r"\?", pattern)
                    ]  # noqa: E501
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        """
        Return the available spaces for next move
        """
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves

    def make_move_to(self, index: int) -> Move:
        """
        Atttempts to place piece on specified space
        """
        print(f"{index=}")
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")

        grid = Grid(
            self.grid.cells[:index]
            + self.current_mark
            + self.grid.cells[index + 1 :]  # noqa: E501, E203
        )
        after_st = GameState(grid)
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=after_st,
        )
