from roster import *
from team import Team
import random
from tqdm import trange





def main():

    totals = {"touchdown": 0, "field goal": 0, "punt": 0, "turnover": 0}
    total_sims = 100000
    Huskers = Team(50, 69, "Huskers")

    #Huskers.start_possession(25)
    #Huskers.current_possession.sim_possession()       #run a possession

    for i in trange(total_sims):
        Huskers.start_possession(25)
        result = Huskers.current_possession.sim_possession()                           #run sim
        totals[result] = totals.get(result) + 1

    percent_totals = {key: (value / total_sims) * 100 for key, value in totals.items()}
    percent_totals_rounded = {key: f'{value: .2f}%' for key, value in percent_totals.items()}
    print(percent_totals_rounded)

if __name__ == "__main__":
    main()