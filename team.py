from possession import Possession

class Team:

    def __init__(self, third_down_percent, pass_completion_percent, name):
        self.third_down_percent = third_down_percent
        self.pass_completion_percent = pass_completion_percent
        self.name = name

        self.current_possesion = None

    def start_possession(self, yardline):
        possesion = Possession(self, yardline)
        self._current_possesion = possesion

