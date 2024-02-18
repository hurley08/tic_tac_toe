from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import DumbComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.renderers import ConsoleRenderer


p1 = DumbComputerPlayer(mark.CROSS)
p2 = DumbComputerPlayer(mark.NOUGHT)

TicTacToe(p1, p2, ConsoleRenderer()).play()
