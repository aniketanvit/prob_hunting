from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
from probabilistic_hunting_move_cost import ProbabilisticHunting_WithCost_Rule2

import copy
import matplotlib.pyplot as plt
import random

def main():

    bot_for_moving_cost = ProbabilisticHunting_WithCost_Rule2 (20)
    bot_for_target_present = ProbabilisticHunting_TargetPresent (20)

    bot_for_moving_cost.Map = copy.deepcopy (bot_for_target_present.getMap ())

    iteration_count = 30

    MOVECOST_PERFORMANCE = []
    PRESENT_PERFORMANCE = []

    for i in range (0, iteration_count, 1):
        r_ind = random.randint (0, bot_for_moving_cost.dimension - 1)
        c_ind = random.randint (0, bot_for_target_present.dimension - 1)

        bot_for_moving_cost.target_i = r_ind
        bot_for_moving_cost.target_i = c_ind
        bot_for_target_present.target_i = r_ind
        bot_for_target_present.target_i = c_ind

        time_taken = bot_for_moving_cost.startHunt ()
        MOVECOST_PERFORMANCE.append (time_taken)

        time_taken = bot_for_target_present.startHunt ()
        PRESENT_PERFORMANCE.append (time_taken)

        bot_for_target_present.reset()
        bot_for_moving_cost.reset()

    plt.plot (PRESENT_PERFORMANCE, MOVECOST_PERFORMANCE, linestyle='', marker='o', color='b')
    plt.ylabel ('Searches taken using Rule 2')
    plt.xlabel ('Searches taken with cost for moving')
    plt.title ('Performance measure - Rule 2 vs Rule 2 with Cost for moving')
    plt.show ()

if __name__ == '__main__':
    main()