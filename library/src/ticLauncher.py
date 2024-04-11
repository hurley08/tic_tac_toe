from tic_tac_toe.logic import validators, models, exceptions
from tic_tac_toe.game import players, engine
import frontends.console.renderers as ren 
from tic_tac_toe.game.renderers import Renderer as REN 
import time
ge = engine.TicTacToe
'''
gep = ge.play
gcp = ge.get_current_player
'''


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
# Create a gamee





repeat = input('Replay how many times? \n')
tally = {}
tally['X'] = 0
tally['O'] = 0
try:
    repeat = int(repeat)
except:
    repeat = 1 
finally:
    for i in range(repeat):
        p1 = player_dumb(mark.CROSS, currentPlayer=True)
        p2 = player_dumb(mark.NOUGHT, currentPlayer=False)
        gss = models.GameState(models.Grid())
        Ren = cr()
        GAME = ge(player1=p1, player2=p2,rend=ren.ConsoleRenderer, gamestate=gss )
        print(GAME.state, GAME.state.winner, GAME.state.win)
        #time.sleep(4)
        print(GAME.state,"\n", gss)
        time.sleep(5)
        win = GAME.play()
        tally[win.value] += 1 
    print(tally)







