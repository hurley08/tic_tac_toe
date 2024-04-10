from tic_tac_toe.logic import validators, models, exceptions
from tic_tac_toe.game import players, engine
import frontends.console.renderers as renderers 
from tic_tac_toe.game.renderers import Renderer as REN 

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

cr = renderers.ConsoleRenderer
cs = renderers.clear_screen
bl = renderers.blink
pbl = renderers.print_blinking
prs = renderers.print_solid

player = players.Player
player_dumb = players.DumbComputerPlayer
player_smart = players.ComputerPlayer

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

# Assign player types
# Create a game

p1 = player_dumb(mark.CROSS)
p2 = player_dumb(mark.NOUGHT)
Ren = cr()
GAME = ge(p1,p2,Ren)
GRID = gr()
GS = gs(GRID)



print(GAME.play())



