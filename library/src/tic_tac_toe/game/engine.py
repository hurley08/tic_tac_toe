# tic_tac_toe/game/engine.py
import sys
from dataclasses import dataclass
from typing import Callable, TypeAlias, Tuple
from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as Renderer
from tic_tac_toe.game.players import Player, ComputerPlayer, DumbComputerPlayer
#from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.validators import validate_players

ErrorHandler: TypeAlias = Callable[[Exception], None]



@dataclass(frozen=True)
class TicTacToe:
    player1: ComputerPlayer
    player2: ComputerPlayer
    renderer: Renderer
    error_handler: ErrorHandler | None = None
    winner = False
    tie = False

    def __post_init__(self):
        validate_players(self.player1, self.player2)
       
    def get_winner_or_tie(self, game_state):
        return game_state.winner, game_state.tie

    def play(self, starting_mark: Mark = Mark("X")) -> Tuple[Mark|bool, bool]:
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                return self.get_winner_or_tie(game_state)
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> Player:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
    
