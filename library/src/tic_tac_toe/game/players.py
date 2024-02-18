import time
import random
import abc 

from tic_tac_toe.logic.models import Mark, Move, GameState
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.minimax import find_best_move, minimax
class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark:Mark) -> None:
        self.mark = mark 

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other players turn")
        

    def get_move(self, game_state: GameState) -> None:
        options = game_state.possible_moves
        while not choice in options:
            choice = input(f"Choose from the following: {options}")
        """
        Return computer move in the given game_state
        """
        
class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.35) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

  
    def get_computer_move(self, game_state: GameState) -> Move | None:
        return game_state.find_best_move()
        """
        Return computer move in the given game_state
        """
    
class DumbComputerPlayer(ComputerPlayer):
    # This automated player will choose a move from 
    # the list of possible moves at random
    def __init__(self, mark: Mark, delay_seconds: float = 0.35) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

 #   def get_move(self, game_state: GameState) -> Move | None:
  #      time.sleep(self.delay_seconds)
        
    def get_computer_move(self, game_state: GameState) -> Move | None:
        return game_state.make_random_move()

class SmartComputerPlayer(ComputerPlayer):
    def __init__(self, mark: Mark, delay_seconds: float = 0.35) -> None:
        super().__init__(mark)

        self.delay_seconds = delay_seconds
    def get_move(self, game_state: GameState) -> Move | None:
        return find_best_move(game_state)