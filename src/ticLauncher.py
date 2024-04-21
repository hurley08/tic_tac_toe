from tic_tac_toe.logic import models
from tic_tac_toe.game import players, engine
from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as CR
import time

"""
gep = ge.play
gcp = ge.get_current_player
"""

"""
gr = models.Grid
grtc = gr.total_count
grX = gr.x_count
grO = gr.o_count
grsp = gr.sp_count
cells = gr.cells

im = models.InvalidMove
ws = models.WINNING_PATTERNS
move = models.Move

mark = models.Mark
CR = mark.CROSS
NO = mark.NOUGHT
mwo = mark.whois
mo = mark.other

gs = models.GameState
tie = gs.tie
win = gs.winner
go = gs.game_over
gns = gs.game_not_started
pm = gs.possible_moves
mm = gs.make_move_to

cr = ren.ConsoleRenderer
cs = ren.clear_screen
bl = ren.blink
pbl = ren.print_blinking
prs = ren.print_solid

player = players.Player


vgs = validators.validate_game_state
vg = validators.validate_grid
vnm = validators.validate_number_of_marks
vsm =validators.validate_starting_mark
vw = validators.validate_winner
vw2 = validators.validate_winner_refactor

igs = exceptions.InvalidGameState
im = exceptions.InvalidMove

cp = players.ComputerPlayer
dcp = players.DumbComputerPlayer
p = players.Player

def create_random_cells():
    t = ""
    for i in range(9):
        t+=random.choice(["X","O", " "])
    return t
"""


# Assign player types
# Create a gamee
player_dumb = players.DumbComputerPlayer
player_smart = players.ComputerPlayer
mark = models.Mark

repeat = input("Replay how many times? \n")
tally = {}
tally["X"] = 0
tally["O"] = 0
tally["-"] = 0
history = []


def init_game():
    ge = engine.TicTacToe
    p1 = player_dumb(mark.CROSS, currentPlayer=True)
    p2 = player_dumb(mark.NOUGHT, currentPlayer=False)
    gss = models.GameState(models.Grid())
    ren = CR(gss)
    GAME = ge(player1=p1, player2=p2, rend=ren, gamestate=gss)
    return GAME


session_start = time.time()
try:
    repeat = int(repeat)
except:
    repeat = 1
finally:
    for i in range(repeat):
        game_start = time.time()
        game = init_game()
        time.sleep(0.01)
        if win := game.play():
            tally[win.value] += 1
        else:
            tally["-"] += 1
            pass
        game_end = time.time()
        print(f"{game_start-game_end}s to complete this game")
        history.append((i, GAME.state, game_end - game_start))

session_end = time.time()
print(f"This series took {session_end-session_start}s to complete")
print(history)
print(tally)
