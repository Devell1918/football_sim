from roster import *
from team import Team
import random
from tqdm import trange




class State:
    def process(self, game):
        pass


class Game_Possession(State):
    def __init__(self, game, starting_yard_line: int):
        self.starting_yard_line = starting_yard_line
        self.process(game)

    def process(self, game):
        game.team2.start_possession(self.starting_yard_line)
        game.team2.current_possession.sim_possession()
        


class Kickoff(State):
    def process(self, game):
        print(f" kicked the ball")
        game.switch_state(Game_Possession(game, starting_yard_line=25))
