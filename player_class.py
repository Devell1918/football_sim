class Player:

    def __init__(self, name: str, number : int = 0):
        self.name = name
        self.number = number

class QuarterBack(Player):
    def __init__(self, name:str, number : int, pass_yards_average: float):
        super().__init__(name, number)

class RunningBack(Player):
    def __init__(self, name:str, number : int, run_yards_average: float):
        super().__init__(name, number)

class WideReceiver(Player):
    def __init__(self, name:str, number : int, receiving_yards_average: float):
        super().__init__(name, number)
