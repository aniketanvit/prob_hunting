from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
import copy
import matplotlib.pyplot as plt
import random

def main():

    bot_for_target_found = ProbabilisticHunting_TargetFound (5)
    bot_for_target_present = ProbabilisticHunting_TargetPresent (5)

    bot_for_target_found.Map = copy.deepcopy (bot_for_target_present.getMap ())

    iteration_count = 30

    FOUND_PERFORMANCE = []
    PRESENT_PERFORMANCE = []

    for i in range (0, iteration_count, 1):
        r_ind = random.randint (0, bot_for_target_found.dimension - 1)
        c_ind = random.randint (0, bot_for_target_found.dimension - 1)

        bot_for_target_found.target_i = r_ind
        bot_for_target_found.target_i = c_ind
        bot_for_target_present.target_i = r_ind
        bot_for_target_present.target_i = c_ind

        time_taken = bot_for_target_found.startHunt ()
        FOUND_PERFORMANCE.append (time_taken)

        time_taken = bot_for_target_present.startHunt ()
        PRESENT_PERFORMANCE.append (time_taken)

    print(PRESENT_PERFORMANCE)
    print(FOUND_PERFORMANCE)
    plt.plot (PRESENT_PERFORMANCE, FOUND_PERFORMANCE, linestyle='--', marker='o', color='b')
    plt.ylabel ('Searches taken to search the target using Rule 1')
    plt.xlabel ('Searches taken to search the target using Rule 2')
    plt.title ('Performance measure - Rule 1 vs Rule 2')
    plt.show ()

if __name__ == '__main__':
    main()