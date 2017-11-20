from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
import copy
import matplotlib.pyplot as plt
import random

def main():

    bot_for_target_found = ProbabilisticHunting_TargetFound (10)
    bot_for_target_present = ProbabilisticHunting_TargetPresent (10)

    bot_for_target_found.Map = copy.deepcopy (bot_for_target_present.getMap ())

    iteration_count = 30

    FOUND_PERFORMANCE = []
    PRESENT_PERFORMANCE = []

    ci = 0
    cj = 0

    target_terrain = bot_for_target_found.Map[0][0]
    tf = False
    print(target_terrain.value)
    for i in range (0, iteration_count, 1):

        while(True):
            if(tf == True):
                break
            while(True):
                if(bot_for_target_found.Map[ci][cj] != target_terrain):
                    cj += 1

                    if(cj >= bot_for_target_found.dimension):
                        cj = 0
                else:
                    tf = True
                    break
            ci += 1
            if(bot_for_target_found.dimension <= ci):
                ci = 0

        bot_for_target_found.target_i = ci
        bot_for_target_found.target_j = cj
        bot_for_target_present.target_i = ci
        bot_for_target_present.target_j = cj

        time_taken = bot_for_target_found.startHunt ()
        FOUND_PERFORMANCE.append (time_taken)

        time_taken = bot_for_target_present.startHunt ()
        PRESENT_PERFORMANCE.append (time_taken)

        bot_for_target_present.reset()
        bot_for_target_found.reset()

    plt.plot (PRESENT_PERFORMANCE, FOUND_PERFORMANCE, linestyle='', marker='o', color='b')
    x1 = max(PRESENT_PERFORMANCE)
    y1 = max(FOUND_PERFORMANCE)
    xy = max(x1, y1)
    plt.plot ([0,xy], [0, xy], linestyle='-', marker='o', color='red')

    plt.xlabel ('Searches taken using Rule 1')
    plt.ylabel ('Searches taken using Rule 2')
    plt.title ('Performance measure - Rule 1 vs Rule 2')
    plt.show ()

if __name__ == '__main__':
    main()