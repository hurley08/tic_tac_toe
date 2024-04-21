# tic_tac_toe/src/tic_launcher.py

import time  # Provides methods to measure execution times
from tic_tac_toe.logic import models
from tic_tac_toe.game import players, engine
from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as CR

# Assign player types
PlayerDumb = players.DumbComputerPlayer
PlayerSmart = players.ComputerPlayer
Mark = models.Mark

# Ask how many cycles to play
REPEAT = input("Replay how many times? \n")

# Variables to store end-game results
tally = {}
tally["X"] = 0
tally["O"] = 0
tally["-"] = 0
history = []


def init_game():
    """Sets up a new instance of engine"""
    ge = engine.TicTacToe
    p1 = PlayerDumb(Mark.CROSS, currentPlayer=True)
    p2 = PlayerDumb(Mark.NOUGHT, currentPlayer=False)
    gss = models.GameState(models.Grid())
    ren = CR(gss)
    game_ = ge(player1=p1, player2=p2, rend=ren, gamestate=gss)
    return game_


session_start = time.time()
try:
    REPEAT = int(REPEAT)
except ValueError:
    REPEAT = 1
finally:
    for i in range(REPEAT):
        game_start = time.time()
        game = init_game()
        time.sleep(0.01)
        if win := game.play():
            tally[win.value] += 1
        else:
            tally["-"] += 1
        game_end = time.time()
        print(f"{game_start-game_end}s to complete this game")
        history.append((i, game.state, game_end - game_start))

session_end = time.time()
print(f"This series took {session_end-session_start}s to complete")
print(history)
print(tally)