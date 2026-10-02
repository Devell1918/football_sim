from state_machine import *


class Game:

    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2

        print("Game Started")

        self.state = Kickoff()
        self.state.process(self)


    def switch_state(self, new_state: State):
        print("State switched")
        self.state = new_state