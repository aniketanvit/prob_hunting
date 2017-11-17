from custom_enums import Terrain
from probabilistic_hunting import ProbabilisticHunting
import random
import numpy as np

class ProbabilisticHunting_TargetPresent (ProbabilisticHunting):

    def updateBelief (self, i, j):

        scaling_factor = 1

        if (self.Map[i][j] == Terrain.FLAT):
            scaling_factor = self.NotFound_given_Present_Flat
        elif (self.Map[i][j] == Terrain.HILLY):
            scaling_factor = self.NotFound_given_Present_Hilly
        elif (self.Map[i][j] == Terrain.FOREST):
            scaling_factor = self.NotFound_given_Present_Forest
        else:
            scaling_factor = self.NotFound_given_Present_Cave

        belief_present = self.Belief[i][j]

        belief_present = belief_present * scaling_factor

        self.Belief[i][j] = belief_present

        self.beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.beta += self.Belief[ii][jj]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief[ii][jj] /= self.beta

        self.currentTime += 1

    def getNextSearchCell(self):
        arrayBelief = np.array(self.Belief)
        minBelief = np.where(arrayBelief == arrayBelief.max())
        if(len(minBelief[0]) > 1):
            choicePos = random.randrange(len(minBelief[0]))
            return minBelief[0][choicePos], minBelief[1][choicePos]
        else:
            return minBelief[0][0], minBelief[1][0]
