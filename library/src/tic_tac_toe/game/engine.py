# tic_tac_toe/game/engine.py

from dataclasses import dataclass, replace
from typing import Callable, TypeAlias
import time

from tic_tac_toe.game.players import Player, ComputerPlayer, DumbComputerPlayer
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.validators import validate_players, validate_grid

ErrorHandler: TypeAlias = Callable[[Exception], None]
        

class TicTacToe:
    def __init__(self, player1 = DumbComputerPlayer, 
                 player2 = DumbComputerPlayer, 
                 rend=Renderer, 
                 gamestate=None, 
                 start_mark = Mark.CROSS, 
                 error_handler = None):
        self.p1 = player1
        self.p2 = player2
        self.renderer=rend
        self.state=GameState(Grid())
        self.starting_mark=start_mark
        self.error_handler = error_handler
        validate_players(self.p1, self.p2)
        validate_grid(self.state.grid)
        self.current_player = self.p1
        self.current_mark = self.current_player.mark



    def switch_current_player(self) -> Mark:
        if self.current_player == self.p1:
            self.current_player = self.p2
        else: 
            self.current_player = self.p1
        return self.current_player
    
    def who_is_current_player(self) -> Player:
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1
        return self.current_player
    
    def switch_players(self) -> Mark:
        if self.current_mark == Mark.CROSS:
            return Mark.NOUGHT
        else: 
            return Mark.CROSS
        
        if self.state.current_mark is self.player1.mark:
        #if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
    
    def set_game_status(self) -> GameState:
        replace(self)
        return self.state

    def play(self) -> None:
        stat = self.state
        player = self.current_player
        print(self.state, "TER")
        while not self.state.game_over:
            if self.state.game_over or self.state.win:
                break
            try:
                #status = player.make_move(status)
                stat = self.current_player.make_move(stat)
                print(stat, "RONN")
                if stat==False:
                    self.state.game_over = True
                self.state = self.renderer.render(self, stat)
                
                winner = self.state.winner
                
                if winner:
                    self.state.win= True
                    self.state.game_over = True
                self.current_mark = self.switch_players()
                #game_state = self.set_game_status(game_state)
                self.current_player = self.switch_current_player()
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)
            return self.state.winner

'''
@dataclass(frozen=True)
class TicTacToe:
    grid = Grid()
    player1: DumbComputerPlayer
    player2: DumbComputerPlayer
    renderer: Renderer
    renderer = Renderer
    state = GameState(grid)
    current_player = str
    error_handler: ErrorHandler | None = None


    def __post_init__(self, starting_mark: Mark = Mark("X")):
        validate_players(self.player1, self.player2)
        

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        #grid = Grid()
        #game_state = GameState(grid)
        while True:
            
            game_state = self.renderer.render(self.state)
            if self.state.game_over:
                break
            
            try:
                player = self.get_current_player()
                #status = player.make_move(status)
                game_state = player.make_move(self.state)
                self.state = game_state
                #game_state = self.set_game_status(game_state)
                print(f"{player=} {game_state=}")
                #print(game_state.get_counts)
                #time.sleep(.5)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)
        return player.mark

    def get_current_player(self) -> Player:
        if self.state.current_mark is self.player1.mark:
        #if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
    
    def set_game_status(self, game_state: GameState) -> GameState:
        replace(self)
        return self.state
'''