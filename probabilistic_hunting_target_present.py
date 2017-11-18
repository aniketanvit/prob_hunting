from custom_enums import Terrain
from probabilistic_hunting import ProbabilisticHunting
import random

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

        self.Belief[i][j] *= scaling_factor

        self.beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.beta += self.Belief[ii][jj]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief[ii][jj] /= self.beta

        self.currentTime += 1

    def getBelief(self):
        return self.Belief

    def getNextSearchCell(self):
        temp_list = []
        last_i = -1
        last_j = -1
        max_val = -1
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                if(self.Belief[i][j] > max_val):
                    max_val = self.Belief[i][j]
                    last_i = i
                    last_j = j
                elif(max_val == self.Belief[i][j]):
                    temp_list.append([i, j])

        if(len(temp_list) > 1):
            random_index = random.randint(0, len(temp_list)-1)
            return (temp_list[random_index][0], temp_list[random_index][1])
        else:
            return (last_i, last_j)
