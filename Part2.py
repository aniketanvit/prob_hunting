import matplotlib.pyplot as plt
import random
import numpy as np
from enum import Enum

class Terrain(Enum):
    FLAT = 0,
    HILLY = 1,
    FOREST = 2,
    CAVE = 3

class ProbabilisticHuntingPart2:

    def __init__(self, dimension):
        self.Map = []
        self.Belief = []
        self.tempBelief = []
        self.Belief_Found = []
        self.dimension = dimension

        self.NotFound_given_Present_Flat = 0.1
        self.NotFound_given_Present_Hilly = 0.3
        self.NotFound_given_Present_Forest = 0.7
        self.NotFound_given_Present_Cave = 0.9

        self._initialiseMap()
        self._reset()

    def _reset(self):
        self.Belief = []
        self.tempBelief = []
        self.Belief_Found = []
        self.initialiseBelief()
        self._initializeBeliefFound()
        self.target_i = 1
        self.target_j = 1
        self.previousTerrain1 = ''
        self.previousTerrain2 = ''
        self.currentTime = 0
        self.beta = 1

    def getMap(self):
        return self.Map

    def _initialiseMap(self):

        self.beta = 1

        flatProbability = 0.2
        hillyProbability = 0.3
        forestProbability = 0.3
        caveProbability = 0.2

        visited = []
        for i in range(0, self.dimension):
            visited.append([])
            self.Map.append([])
            for j in range(0, self.dimension):
                visited[i].append(False)
                self.Map[i].append(Terrain.CAVE)

        totalCells = self.dimension * self.dimension
        flatCells = totalCells * flatProbability
        hillyCells = totalCells * hillyProbability
        forestcells = totalCells * forestProbability

        count = flatCells
        while(count > 0):
            i = random.randint(0, self.dimension-1)
            j = random.randint(0, self.dimension-1)
            if(visited[i][j] == False):
                self.Map[i][j] = Terrain.FLAT
                visited[i][j] = True
                count -= 1
        count = hillyCells
        while (count > 0):
            i = random.randint (0, self.dimension - 1)
            j = random.randint (0, self.dimension - 1)
            if (visited[i][j] == False):
                self.Map[i][j] = Terrain.HILLY
                visited[i][j] = True
                count -= 1
        count = forestcells
        while (count > 0):
            i = random.randint (0, self.dimension - 1)
            j = random.randint (0, self.dimension - 1)
            if (visited[i][j] == False):
                self.Map[i][j] = Terrain.FOREST
                visited[i][j] = True
                count -= 1

        self._setTarget()

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

                self.Belief_Found[i].append(self.Belief[i][j] * (1-scaling_factor))

        temp_beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                temp_beta += self.Belief_Found[ii][jj]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief_Found[ii][jj] /= temp_beta

    def _setTarget(self):
        self.target_i = random.randint(0, self.dimension - 1)
        self.target_j = random.randint(0, self.dimension - 1)

    def showMap(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.Map[i][j].name, end = " ")
            print()

    def initialiseBelief(self):
        for i in range(0, self.dimension):
            self.Belief.append([])
            self.tempBelief.append([])
            for j in range(0, self.dimension):
                self.Belief[i].append(1/(self.dimension * self.dimension))
                self.tempBelief[i].append(0)

    def updateBeliefTargetPresent (self, i, j):

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

        # self.currentTime += 1

    def updateBeliefTargetFound(self, i, j):

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

        self.Belief_Found[i][j] = self.Belief[i][j] * (1-scaling_factor)

        temp_beta = 0
        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                temp_beta += self.Belief_Found[ii][jj]

        for ii in range (0, self.dimension):
            for jj in range (0, self.dimension):
                self.Belief_Found[ii][jj] /= temp_beta

    def updateBeliefSwap (self, i, j, ter1, ter2, rule):
        repeatTer1 = False
        repeatTer2 = False
        if(self.previousTerrain1):
            if((self.previousTerrain1 == ter1) or (self.previousTerrain2 == ter1)):
                repeatTer1 = True
            if((self.previousTerrain1 == ter2) or (self.previousTerrain2 == ter2)):
                repeatTer2 = True

        for row in range(0, self.dimension):
            for cell in range(0, self.dimension):
                if(str(self.Map[row][cell]) == str(ter1)) or (str(self.Map[row][cell]) == str(ter2)):
                    # continue
                    possibleMoves12 = []
                    possibleMoves21 = []
                    options = self.findAjacent(row, cell)
                    for pos in options:
                        if(str(self.Map[row][cell]) == str(ter1)):
                            if(str(self.Map[pos[0]][pos[1]]) == str(ter2)):
                                possibleMoves12.append(pos)
                        else:
                            if(str(self.Map[pos[0]][pos[1]]) == str(ter1)):
                                possibleMoves21.append(pos)

                    if(len(possibleMoves12) > 0):
                        if(rule == 'rule1'):
                            currBelief = self.Belief[row][cell]
                        elif(rule == 'rule2'):
                            currBelief = self.Belief_Found[row][cell]
                        for x in possibleMoves12:
                            self.tempBelief[x[0]][x[1]] += currBelief / len(possibleMoves12)

                    if(len(possibleMoves21) > 0):
                        if(rule == 'rule1'):
                            currBelief = self.Belief[row][cell]
                        elif(rule == 'rule2'):
                            currBelief = self.Belief_Found[row][cell]
                        for x in possibleMoves21:
                            self.tempBelief[x[0]][x[1]] += currBelief / len(possibleMoves21)

                    # we check if a terrain has been repeated from before
                    # if so, we set it to zero, since we know for sure that the
                    # the target has moved from there to next terrain
        for row in range(0, self.dimension):
            for cell in range(0, self.dimension):
                if(str(self.Map[row][cell]) == str(ter1)) or (str(self.Map[row][cell]) == str(ter2)):
                    if((ter1 != ter2) and (repeatTer1 != repeatTer2)):
                        if(repeatTer1):
                            if(str(self.Map[row][cell]) == ter1):
                                self.tempBelief[row][cell] = 0

                        if(repeatTer2):
                            if(str(self.Map[row][cell]) == ter2):
                                self.tempBelief[row][cell] = 0
                else:
                    self.tempBelief[row][cell] = 0

        self.scaleBelief()
        if(rule == 'rule1'):
            self.Belief = self.tempBelief
        elif(rule == 'rule2'):
            self.Belief_Found = self.tempBelief
        # self.Belief = self.tempBelief
        self.previousTerrain1 = ter1
        self.previousTerrain2 = ter2

    def scaleBelief(self):
        total = 0
        for row in self.tempBelief:
            for cell in row:
                total += cell

        if(total is not 1):
            for row in range(0, self.dimension):
                for cell in range(0, self.dimension):
                    if(self.tempBelief[row][cell] > 0):
                        self.tempBelief[row][cell] /= total

    def targetFound(self, i, j):
        success_probability = 1
        if(self.target_i != i or self.target_j != j):
            return False
        if(self.Map[i][j] == Terrain.FLAT):
            success_probability = 10
        elif(self.Map[i][j] == Terrain.HILLY):
            success_probability = 30
        elif(self.Map[i][j] == Terrain.HILLY):
            success_probability = 70
        else:
            success_probability = 90

        random_number = random.randint(1, 100)
        if(random_number >= success_probability):
            return True
        return False

    # search Belief for the highest probability
    # if more than one found, select random
    def getNextSearchCell(self, rule):
        if(rule == 'rule1'):
            arrayBelief = np.array(self.Belief)
        elif(rule == 'rule2'):
            arrayBelief = np.array(self.Belief_Found)
        maxBelief = np.where(arrayBelief == arrayBelief.max())
        if(len(maxBelief[0]) > 1):
            choicePos = random.randrange(len(maxBelief[0]))
            return maxBelief[0][choicePos], maxBelief[1][choicePos]
        else:
            return maxBelief[0][0], maxBelief[1][0]

    def findAjacent(self, i, j):
        if(i == 0):
            if(j == 0):
                options = [[i + 1, j], [i, j + 1]]
            elif(j == self.dimension - 1):
                options = [[i + 1, j], [i, j - 1]]
            else:
                options = [[i + 1, j], [i, j - 1], [i, j + 1]]
        elif(j == 0):
            if(i == 0):
                options = [[i + 1, j], [i, j + 1]]
            elif(i == self.dimension - 1):
                options = [[i - 1, j], [i, j + 1]]
            else:
                options = [[i - 1, j], [i + 1, j], [i, j + 1]]
        elif(i == self.dimension - 1):
            if(j == 0):
                options = [[i - 1, j], [i, j + 1]]
            elif(j == self.dimension - 1):
                options = [[i - 1, j], [i, j - 1]]
            else:
                options = [[i - 1, j], [i, j - 1], [i, j + 1]]
        elif(j == self.dimension - 1):
            if(i == 0):
                options = [[i + 1, j], [i, j - 1]]
            elif(i == self.dimension - 1):
                options = [[i - 1, j], [i, j - 1]]
            else:
                options = [[i - 1, j], [i + 1, j], [i, j - 1]]
        else:
            options = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]

        return options

    def moveTarget(self):
        # generate a random move to next cell
        # print(self.Map[self.target_i][self.target_j])
        options = self.findAjacent(self.target_i, self.target_j)
        move = random.choice(options)
        self.target_i = move[0]
        self.target_j = move[1]

    def getTerrain(self):
        return str(self.Map[self.target_i][self.target_j])


    def startHunt(self, rule):
        # print('Target in: ' + str(self.target_i) + ', ' + str(self.target_j))

        self.currentTime = 0
        while(True):
            (i, j) = self.getNextSearchCell(rule)
            # print('\nSearching: ' + str(i) + ', ' + str(j))
            found = self.targetFound(i, j)
            if(found):
                print("Target Found")
                break
            else:
                terrain_1 = self.getTerrain()
                self.moveTarget()
                terrain_2 = self.getTerrain()
                # print('Target moves on border: ' + str(terrain_1) + ' x ' + str(terrain_2) )
                if(rule == 'rule1'):
                    self.updateBeliefTargetFound(i, j)
                if(rule == 'rule2'):
                    self.updateBeliefTargetPresent(i, j)
                self.updateBeliefSwap(i, j, terrain_1, terrain_2, rule)
                self.currentTime += 1


def main():
    results_rule1 = []
    results_rule2 = []
    # ph = ProbabilisticHunting(50)
    for i in range(40):
        ph = ProbabilisticHunting(50)
        print('\nNew Map Generated')
        print('Hunting on Rule1')
        ph.startHunt('rule1')
        results_rule1.append(ph.currentTime)
        ph._reset()
        print('Hunting on Rule2')
        ph.startHunt('rule2')
        results_rule2.append(ph.currentTime)
    print('Total times for Rule1: '+str(results_rule1))
    print('Average Time for Rule1: ' + str(np.mean(results_rule1)))
    print('Total times for Rule2: '+str(results_rule2))
    print('Average Time for Rule2: ' + str(np.mean(results_rule2)))
    plt.plot (results_rule1, results_rule2, linestyle='', marker='o', color='b')
    plt.ylabel ('Searches taken to search the target using Rule 2')
    plt.xlabel ('Searches taken to search the target using Rule 1')
    x1 = max(results_rule1)
    y1 = max(results_rule2)
    xy = max(x1, y1)
    plt.plot ([0,xy], [0, xy], linestyle='-', marker='o', color='red')

    # plt.gca().set_color_cycle(['red', 'blue'])
    # plt.plot(results_rule1)
    # plt.plot(results_rule2)
    # plt.xlabel ('Search Iteration')
    # plt.ylabel ('Search Count')

    plt.title ('Performance measure for Part 2 (Moving Target) - Rule 1 vs Rule 2')
    # plt.legend(['Rule 1', 'Rule 2'], loc='upper left')
    plt.show ()

if __name__ == '__main__':
    main()
