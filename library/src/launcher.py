from tic_tac_toe.frontends.console.renderers import ConsoleRenderer as Cr
from tic_tac_toe.frontends.console.renderers import clear_screen, blink, print_blinking, print_solid
from tic_tac_toe.frontends.console import renderers as REN
from tic_tac_toe.logic import validators, models, exceptions
from tic_tac_toe.game import players, engine,
from tic_tac_toe.game.renderers import Renderer as ren 

ge = engine.TicTacToe
gep = ge.play
gcp = ge.get_current_player

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

Cr = Cr(gr())
cs = clear_screen
bl = blink
pbl = print_blinking
prs = print_solid

player = players.Player
player_dumb = players.DumbComputerPlayer
player_smart = players.ComputerPlayer

vgs = validators.validate_game_state
vg = validators.validate_grid
vnm = validators.validate_number_of_marks
vsm =validators.validate_starting_mark
vw = validators.validate_winner

igs = exceptions.InvalidGameState
im = exceptions.InvalidMove

cp = players.ComputerPlayer

def create_random_cells():
    t = ""
    for i in range(9):
        t+=random.choice(["X","O", " "])
    return t





p1 = player_dumb(mark.CROSS)
p2 = player_dumb(mark.NOUGHT)
try:
    e = ge(p1, p2, Cr)
    print(f"TicTacToe class instantiated")
except:
    print(f"Failed to instantiate engine")
try:
    GR = gr()
    print(f"grid created")
    GS = gs(GR)
    print(f"game_state created")
except:
    print(f"failed to create grid or game_state")
finally:
    print(f"int completed")

while not GS.game_over:
    mv1 = p1.get_computer_move(GS)
    GS = mv1.after_state
    GS = GS.make_move_to(mv1.cell_index)
    GS = GS.after_state
    mv2 = p2.get_computer_move(GS)
    GS = GS.make_move_to(mv2.cell_index)
    GS = GS.after_state





