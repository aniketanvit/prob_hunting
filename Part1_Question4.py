from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
import numpy as np
import random
from custom_enums import Terrain

class ProbabilisticHunting_WithMoveCost(ProbabilisticHunting_TargetPresent):

    def __init__(self, dimension):
        super(ProbabilisticHunting_WithMoveCost, self).__init__(dimension)
        self.Utility = []

    def _initializeUtility(self, i, j):

        scaling_factor = (2 * self.dimension) - 1

        for i in range(0, self.dimension):
            self.Utility.append([])
            for j in range(0, self.dimension):
                self.Utility[i].append(self.Belief[i][j] * scaling_factor)

    def updateBelief(self, i, j):
        super(ProbabilisticHunting_WithMoveCost, self).updateBelief(i, j)


    def getNextSearchCell (self):
        arrayBelief = np.array (self.Utility)
        minBelief = np.where (arrayBelief == arrayBelief.max ())
        if (len (minBelief[0]) > 1):
            choicePos = random.randrange (len (minBelief[0]))
            return minBelief[0][choicePos], minBelief[1][choicePos]
        else:
            return minBelief[0][0], minBelief[1][0]

