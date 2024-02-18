# frontends/console/cli


from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.logic.models import Mark

from .args import parse_args
from .renderers import ConsoleRenderer

def main() -> None:
    player1, player2, starting_mark, numGames= parse_args()
    ties = 0
    p1_wins = 0
    p2_wins = 0
    totals = []
    for i in range(numGames):
        game_results = TicTacToe(player1, player2, ConsoleRenderer()). play(starting_mark)
        totals.append(game_results)



    for i in totals:
        if i[0] == None and i[1] == True:
            ties += 1
        if i[1] == False:
            if i[0] == Mark.CROSS:
                p1_wins += 1
            if i[0] == Mark.NOUGHT:
                p2_wins += 1

    if ties+p1_wins+p2_wins != numGames:
        print("The number of resultant games do not match the number played")
    print(f"Results:\n{p1_wins=} {p2_wins=} {ties=}")