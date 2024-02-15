from __future__ import annotations

import enum 
import re
from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.validators import validate_game_state, validate_grid

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

@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post__init(self) -> None:
        if not re.match(r"^[\sX0]{9}$", self.cells):
            raise ValueError("Must contain 9 cells (chars) of X, O, or space")
    
    @cached_property
    def total_count(self) -> int:
        return len(self.cells)
        
    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")
        
    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")
        
    @cached_property
    def sp_count(self) -> int:
        return self.cells.count(" ")
        
@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    # There are 6 unique game states 
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self) -> None:
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other
    
    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.sp_count == 9

    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        # Cells are all filled and no winner
        return self.winner is None and self.grid.sp_count == 0
    
    @cached_property
    def winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None
    
    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start() for match in re.finditer(r"\?", pattern)
                    ]
        return []

    @cached_property
    def possible_moves(self) -> list[Move]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves
    
    def make_move_to(self, index: int) -> Move:
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(# Uses slicing to produce after_state grid
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1 :]
                ),
                self.starting_mark,
            ),
        )

                



