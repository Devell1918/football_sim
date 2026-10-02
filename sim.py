
from game import *





def main():

    totals = {"touchdown": 0, "field goal": 0, "punt": 0, "turnover": 0}
    total_sims = 100000

    #create team
    Huskers = Team(50, 69, "Huskers")
    Hawkeyes = Team(50, 68, "Hawkeyes")

    game = Game(Huskers, Hawkeyes)

    

    #Huskers.start_possession(25)
    #Huskers.current_possession.sim_possession()       #run a possession

    # for i in trange(total_sims):
    #     Huskers.start_possession(25)
    #     result = Huskers.current_possession.sim_possession()                           #run sim
    #     totals[result] = totals.get(result) + 1

    # percent_totals = {key: (value / total_sims) * 100 for key, value in totals.items()}
    # percent_totals_rounded = {key: f'{value: .2f}%' for key, value in percent_totals.items()}
    # print(percent_totals_rounded)

if __name__ == "__main__":
    main()