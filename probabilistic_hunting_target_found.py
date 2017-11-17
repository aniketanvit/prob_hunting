from custom_enums import Terrain
from probabilistic_hunting import ProbabilisticHunting
import random
import numpy as np

class ProbabilisticHunting_TargetFound(ProbabilisticHunting):

    def __init__(self, dimension):
        super(ProbabilisticHunting_TargetFound, self).__init__(dimension)
        self.Belief_Found = []
        self._initializeBeliefFound()

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

        self.Belief_Found[i][j] = self.Belief[i][j] * scaling_factor

        temp_beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                temp_beta += self.Belief_Found[i][j]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief_Found[ii][jj] /= temp_beta

    def getNextSearchCell(self):
        arrayBelief = np.array(self.Belief_Found)
        minBelief = np.where(arrayBelief == arrayBelief.max())
        if(len(minBelief[0]) > 1):
            choicePos = random.randrange(len(minBelief[0]))
            return minBelief[0][choicePos], minBelief[1][choicePos]
        else:
            return minBelief[0][0], minBelief[1][0]

    def _initializeBeliefFound(self):

        scaling_factor = 1

        for i in range(0, self.dimension):
            self.Belief_Found.append([])
            for j in range(0, self.dimension):

                if (self.Map[i][j] == Terrain.FLAT):
                    scaling_factor = self.NotFound_given_Present_Flat
                elif (self.Map[i][j] == Terrain.HILLY):
                    scaling_factor = self.NotFound_given_Present_Hilly
                elif (self.Map[i][j] == Terrain.FOREST):
                    scaling_factor = self.NotFound_given_Present_Forest
                else:
                    scaling_factor = self.NotFound_given_Present_Cave

                self.Belief_Found[i].append(self.Belief[i][j] * scaling_factor)

        temp_beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                temp_beta += self.Belief_Found[ii][jj]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief_Found[ii][jj] /= temp_beta