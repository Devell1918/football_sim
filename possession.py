import random

class Possession:
    """
    used to represent one football possession
    """

    def __init__(self, team, starting_yardline: int, game_clock: int = 0):
        """
        simulates a possession

        :param starting_yardline: start of possession
        :param game_clock: in minutes
        """
        self._starting_yardline = starting_yardline
        self._yardline = starting_yardline
        self._down = 1
        self._team = team

        self._yards_to_td = 0
        self.set_yards_to_td()
        

        self._yards_to_first = 10
        self._game_clock = game_clock #need to figure out how to implement clock
        self._total_plays = 0
        self._total_yards_gained = 0

        #delete all of these?
        self._touchdown = False
        self._field_goal = False
        self._punt = False
        self._turnover = False
        self._end_possession = False

        self._result = ""


        self.MEDIUM_RUN_MAX = 20
        self.SHORT_RUN_MAX = 8
        self.LOSS_MAX = -4

        self.print_play = False

        #print(f'{team.name} ball on the {starting_yardline}')

    def set_yards_to_td(self):
        self._yards_to_td = 100 - self._yardline
        if self._yards_to_td < 10:
            self._yards_to_first = self._yards_to_td

    def choose_play_type(self):
        """
        this function chooses a play type based on the possession variables such as yards to first down
        """
        rand_float = self.get_rand_float()
        match (self._down):
            case 1:
                if rand_float < .55:
                    return "run"
                else:
                    return "pass"
            case 2:
                if self._yards_to_first < 4:
                    if rand_float < 65:
                        return "run"
                    else:
                        return "pass"
                elif self._yards_to_first < 7:
                    if rand_float < .55:
                        return "run"
                    else:
                        return "pass"
                else:
                    if rand_float < .40:
                        return "run"
                    else:
                        return "pass"

            case 3:
                if self._yards_to_first < 2:
                    if rand_float < 65:
                        return "run"
                    else:
                        return "pass"
                elif self._yards_to_first < 5:
                    if rand_float < .55:
                        return "run"
                    else:
                        return "pass"
                else:
                    if rand_float < .20:
                        return "run"
                    else:
                        return "pass"
            case 4:
                if self._yardline > 65:
                    return "feild_goal"
                else:
                    return "punt"

                
    def sim_yards(self, min: int, max: int):
        return random.randint(min, max)


        self._field_goal = True

    def sim_run(self):
        big_run_chance = self.get_rand_float()
        yards_gained = 0

        yards_to_goal = 100 - self._yardline

        #check for a turnover
        if self.check_run_turnover():
            return None
        
        #TODO refactor, right now everything is based on big_run_chance. Even turnovers
        if  yards_to_goal <= 20:
            min_big_run = yards_to_goal
        else:
            min_big_run = 20
        if big_run_chance > 0.95:
            yards_gained = self.sim_yards(min_big_run, 100 - self._yardline)
        elif big_run_chance > 0.80:
            yards_gained = self.sim_yards(self.SHORT_RUN_MAX, self.MEDIUM_RUN_MAX)
        elif big_run_chance < 0.10:
            yards_gained = self.sim_yards(self.LOSS_MAX, 0)
        else:
            yards_gained = self.sim_yards(0, self.SHORT_RUN_MAX)

        return yards_gained

        
    def sim_pass(self):
        pass_comp_percent = self._team.pass_completion_percent
        pass_attempt = self.get_rand_float()

        #check if caught
        if pass_attempt < pass_comp_percent:
            if self.check_pass_turnover():
                return None
            return 8
        else:
            return 0

            

        

# region Results
    def punt(self):
        self._punt = True
        self.end_possession("punt")

    def touchdown(self):
        self._touchdown = True
        self.end_possession("touchdown")

    def turnover(self):
        self._turnover = True
        self.end_possession("turnover")

    def attempt_field_goal(self):
        self._field_goal = True
        self.end_possession("field goal")
# endregion

# region turnovers

    def check_run_turnover(self):
        fumble_chance = 0.02
        fumble_gen = self.get_rand_float()
        if fumble_chance > fumble_gen:
            print('Fumble!!!!!!!')
            return True
        return False
    def check_pass_turnover(self):
        interception_chance = 0.02
        interception_gen = self.get_rand_float()
        if interception_chance > interception_gen:
            print('Interception!!!!')
            return True
        return False

# endregion
    
    def get_rand_float(self):
        return random.random()
    
    def sim_play(self) -> str:
        self._total_plays += 1

        play_type = self.choose_play_type()
        yards_gained = 0
        match (play_type):
            case "run":
                yards_gained = self.sim_run()

            case "pass":
                yards_gained = self.sim_pass()
            case "feild_goal":
                self.attempt_field_goal()
                yards_gained = 0
            case "punt":
                self.punt()
                yards_gained = 0

        if self.print_play:
            print(f'---------------Play Results------------------')
            print(f'Play Type: {play_type}')

        # check for a turnover
        if yards_gained == None:
            self.turnover()
            return
        #check for first down
        if yards_gained >= self._yards_to_first:
            self._down = 1
            if self._starting_yardline > 90:
                self._yards_to_first = 100 - self._yardline
            else:
                self._yards_to_first = 10
        else:
            self._down += 1
            self._yards_to_first -= yards_gained

        #update feild pos
        self._yardline += yards_gained
        self._total_yards_gained += yards_gained
        self.set_yards_to_td()

        #adjust total yards if over
        if self._total_yards_gained > (100 - self._starting_yardline):
            self._total_yards_gained = (100 - self._starting_yardline)



        #check TD
        if self._yardline >= 100:
            yards_gained = abs(self._yards_to_td)
            if self.print_play:
                print(f'Yards Gained: {yards_gained}')
            self.touchdown()

        if self._touchdown or self._field_goal or self._punt:
            pass
        else:
            if(self.print_play):

                print(f'Yards Gained: {yards_gained}')
                print(f'------')
                print(f'Yards to First: {self._yards_to_first}')
                print(f'Down: {self._down}')
                print(f'Yard Line: {self._yardline}')

        if self._end_possession and self.print_play:
            print(self._result)
            print("-----------------------------End of Possession---------------------------")

    def end_possession(self, result: str):
        """
        Ends Possession

        :param result:  result of possession
        """
        self._end_possession = True
        self._result = result



    def sim_possession(self) -> str:
        """
        simulates possession after one has been created
        """
        if self.print_play:
            print("----------Start Possession----------")

        while self._end_possession != True:
            self.sim_play()
            #print(f'Total Plays: {self._total_plays}')
        return self._result


def main():
    pass

    


if __name__ == "__main__":
    main()