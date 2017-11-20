from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
import random
import math

class ProbabilisticHunting_WithCost_Rule1(ProbabilisticHunting_TargetPresent):

    def __init__(self, dimension):
        super(ProbabilisticHunting_WithCost_Rule1, self).__init__(dimension)
        self.Utility = []
        self._initializeUtility()

    def _initializeUtility(self):

        for i in range(0, self.dimension):
            self.Utility.append([])
            for j in range(0, self.dimension):
                self.Utility[i].append(self.Belief[i][j])

    def updateBelief(self, i, j):
        super(ProbabilisticHunting_WithCost_Rule1, self).updateBelief(i, j)
        self.updateUtility()

    def updateUtility(self):
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                self.Utility[i][j] = (self.Belief[i][j] * self.dimension * self.dimension * self.dimension) - math.fabs (self.lastSearched_i - i + self.lastSearched_j - j)

    def getNextSearchCell (self):

        if(self.lastSearched_j < 0 or self.lastSearched_i < 0):
            return (0, 0)

        temp_list = []
        last_i = -1
        last_j = -1
        max_val = -100000
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                if(self.Utility[i][j] > max_val):
                    max_val = self.Utility[i][j]
                    last_i = i
                    last_j = j
                # elif (max_val == self.Utility[i][j]):
                #     temp_list.append ([i, j])
        #
        # if(len(temp_list) > 1):
        #     random_index = random.randint(0, len(temp_list)-1)
        #     return (temp_list[random_index][0], temp_list[random_index][1])
        # else:
        print(last_i, last_j)
        return (last_i, last_j)

    def getBelief(self):
        return self.Utility

    def reset(self):
        super(ProbabilisticHunting_WithCost_Rule1, self).reset()
        self.Utility = []
        self._initializeUtility()

class ProbabilisticHunting_WithCost_Rule2 (ProbabilisticHunting_TargetFound):

    def __init__(self, dimension):
        super(ProbabilisticHunting_WithCost_Rule2, self).__init__(dimension)
        self.Utility = []
        self._initializeUtility()

    def _initializeUtility(self):

        for i in range(0, self.dimension):
            self.Utility.append([])
            for j in range(0, self.dimension):
                self.Utility[i].append(self.Belief_Found[i][j])

    def updateBelief(self, i, j):
        super(ProbabilisticHunting_WithCost_Rule2, self).updateBelief(i, j)
        self.updateUtility()

    def updateUtility(self):
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                self.Utility[i][j] = (self.Belief_Found[i][j] * self.dimension * self.dimension * self.dimension) - math.fabs (self.lastSearched_i - i + self.lastSearched_j - j)

    def getNextSearchCell (self):

        if(self.lastSearched_j < 0 or self.lastSearched_i < 0):
            return (0, 0)

        temp_list = []
        last_i = -1
        last_j = -1
        max_val = -100000
        for i in range(0, self.dimension):
            for j in range(0, self.dimension):
                if(self.Utility[i][j] > max_val):
                    max_val = self.Utility[i][j]
                    last_i = i
                    last_j = j
                # elif (max_val == self.Utility[i][j]):
                #     temp_list.append ([i, j])
        #
        # if(len(temp_list) > 1):
        #     random_index = random.randint(0, len(temp_list)-1)
        #     return (temp_list[random_index][0], temp_list[random_index][1])
        # else:
        print(last_i, last_j)
        return (last_i, last_j)

    def reset (self):
        super (ProbabilisticHunting_WithCost_Rule2, self).reset ()
        self.Utility = []
        self._initializeUtility ()

    def getBelief(self):
        return self.Utility

#Refer to the DEMO file for visualisation

