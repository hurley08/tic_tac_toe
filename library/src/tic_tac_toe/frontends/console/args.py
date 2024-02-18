#frontends/console/args.py
import argparse

from typing import NamedTuple
from tic_tac_toe.game.players import Player, ComputerPlayer, DumbComputerPlayer
from tic_tac_toe.logic.models import Mark

from .players import ConsolePlayer

PLAYER_CLASSES = {
        "human": ConsolePlayer,
        "random": DumbComputerPlayer,
        "ai": ComputerPlayer,
}

class Args(NamedTuple):
    player1: Player
    player2: Player
    starting_mark: Mark
    numGames: int

def parse_args() -> tuple[Player, Player, Mark, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="player_x",
        choices=PLAYER_CLASSES.keys(),
        default="random",   
    )
    parser.add_argument(
        "-O",
        dest="player_o",
        choices=PLAYER_CLASSES.keys(),
        default="ai",   
    )
    parser.add_argument(
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    parser.add_argument(
        "--n",
        dest="iterations",
        type=int,
        default=1
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES[args.player_x](Mark("X"))
    player2 = PLAYER_CLASSES[args.player_o](Mark("O"))
    numGames = args.iterations
    if args.starting_mark == "0":
        player1, player2 = player2, player1
    
    return Args(player1, player2, args.starting_mark, numGames)