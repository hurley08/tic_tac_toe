# tic_tac_toe/logic/models.py

from __future__ import annotations

# from enum import StrEnum
import enum
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


class Mark(enum.StrEnum):
    CROSS = "X"
    NOUGHT = "O"

    @property
    def other(self) -> Mark:
        return Mark.CROSS if self is Mark.NOUGHT else Mark.NOUGHT

    @property
    def whois(self) -> Mark:
        return "CROSS" if self is Mark.CROSS else "NOUGHT"


class Grid:
    def __init__(self, cells=" " * 9):
        self.cells = cells

    def check_cells(self):
        if not re.match(r"^[\sX0]{9}$", self.cells):
            raise ValueError("Must contain 9 cells (chars) of X, O, or space")
        if self.sp_count + self.x_count + self.o_count != 9:
            raise ValueError("Grid's components do not add up")
        return True

    def set_cells(self, cell):
        old_cells = self.cells
        if len(cell) == 9:
            self.cells = cell
        else:
            raise ValueError(
                "cell can only contain 9 occurences of X, O, or space"
            )  # noqa: E501
        if not self.check_cells:
            print("This is not legal")
            self.cells = old_cells

    def total_count(self) -> int:
        return len(self.cells)

    def both_counts(self) -> dict:
        counts = {}
        counts["X"] = self.cells.count("X")
        counts["O"] = self.cells.count("O")
        return counts

    def x_count(self) -> int:
        return self.cells.count("X")

    def o_count(self) -> int:
        return self.cells.count("O")

    def sp_count(self) -> int:
        return self.cells.count(" ")


@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"


@dataclass
class GameState:
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
        count_dict = {}
        count_dict["X"] = self.grid.x_count()
        count_dict["0"] = self.grid.o_count()
        return count_dict

    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count() == self.grid.o_count():
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.sp_count() == 9

    @cached_property
    def is_game_over(self) -> bool:
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        # Cells are all filled and no winner
        return self.winner is None and self.grid.sp_count() == 0

    @cached_property
    def is_winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    self.win = True
                    self.game_over = True
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start() for match in re.finditer(r"\?", pattern)
                    ]  # noqa: E501
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves

    def make_move_to(self, index: int) -> Move:
        print(f"{index=}")
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")

        grid = Grid(
            self.grid.cells[:index]
            + self.current_mark
            + self.grid.cells[index + 1 :]  # noqa: E501
        )
        after_st = GameState(grid)
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=after_st,
        )
