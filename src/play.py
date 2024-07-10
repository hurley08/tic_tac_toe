from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import DumbComputerPlayer
from tic_tac_toe.logic.models import Mark

from tic_tac_toe.frontends.console.renderers import ConsoleRenderer
import time

def play_this():
    game_results = []
    p2_wins = []
    numGames = None
    while numGames is None:
        numGames = int(input("How many games to play? "))
    for i in range(numGames):
        p1 = DumbComputerPlayer(Mark.CROSS)
        p2 = DumbComputerPlayer(Mark.NOUGHT)
        game = TicTacToe(p1, p2, ConsoleRenderer())
        winner = game.play()
        time.sleep(1)
        game_results.append(winner)
    print(game_results)
    ties = 0
    p1_wins = 0
    p2_wins = 0

    for i in game_results:
        if i[0] is None and i[1] is True:
            ties += 1
        if i[1] is False:
            if i[0] == Mark.CROSS:
                p1_wins += 1
            if i[0] == Mark.NOUGHT:
                p2_wins += 1

    if ties + p1_wins + p2_wins != numGames:
        print("The number of resultant games do not match the number played")
    print(f"Results:\n{p1_wins=} {p2_wins=} {ties=}")
