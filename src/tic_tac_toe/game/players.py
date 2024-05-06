import time
import random
import abc

from tic_tac_toe.logic.models import Mark, Move, GameState
from tic_tac_toe.logic.exceptions import InvalidMove


class Player(metaclass=abc.ABCMeta):
    """This class should be used to assign a human player"""

    def __init__(self, mark: Mark, current_player: bool = None) -> None:
        self.mark = mark
        self.current_player = None

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other players turn")

    def get_move(self, game_state: GameState) -> Move | None:
        options = {}

        for i in game_state.possible_moves:
            options[i.cell_index] = i

        choice = None
        while choice not in list(options.keys()):
            choice = int(input(f"Choose from the following: {list(options.keys())}: "))
        return options[choice]


class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    """This class assigns a player that will use minimax in play but is not currently implemented"""

    def __init__(self, mark: Mark, delay_seconds: float = 0.15) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    def get_computer_move(self, game_state: GameState) -> Move | None:
        print("Minimax needs to be implemented")
        """
        Return computer move in the given game_state
        """


class DumbComputerPlayer(ComputerPlayer):
    """This class assigns a computer player that selects moves randomly"""

    def __init__(
        self, mark: Mark, currentPlayer: bool = False, delay_seconds: float = 0.15
    ) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            elif move == None:
                return False
                # raise InvalidMove("No more possible moves")
            # if move := self.get_move(game_state):
            #    return move.after_state

        else:
            raise InvalidMove("It's the other players turn")
        return move.after_state

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    def get_computer_move(self, game_state: GameState) -> Move | None:
        try:
            choice = random.choice(game_state.possible_moves)
            return choice
        except IndexError:
            return None
