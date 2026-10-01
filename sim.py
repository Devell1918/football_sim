from roster import *
from team import Team
import random
from tqdm import trange





def main():

    totals = {"touchdown": 0, "field goal": 0, "punt": 0, "turnover": 0}
    total_sims = 100000
    Huskers = Team(50, 69, "Huskers")
    for i in trange(total_sims):
        Huskers.start_possession(25)
        result = Huskers._current_possesion.sim_possesion()
        totals[result] = totals.get(result) + 1

    percent_totals = {key: (value / total_sims) * 100 for key, value in totals.items()}
    print(percent_totals)

if __name__ == "__main__":
    main()