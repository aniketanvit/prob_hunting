import random
import numpy as np
from enum import Enum

class Terrain(Enum):
    FLAT = 0,
    HILLY = 1,
    FOREST = 2,
    CAVE = 3

class ProbabilisticHunting:

    def __init__(self, dimension):
        self.Map = []
        self.Belief = []
        self.dimension = dimension

        self.currentTime = 0
        self.beta = 1

        self.NotFound_given_Present_Flat = 0.1
        self.NotFound_given_Present_Hilly = 0.3
        self.NotFound_given_Present_Forest = 0.7
        self.NotFound_given_Present_Cave = 0.9

        self.target_i = 1
        self.target_j = 1

        self._initialiseMap()
        self.initialiseBelief()

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
            for j in range(0, self.dimension):
                self.Belief[i].append(1/(self.dimension * self.dimension))

    def updateBelief(self, i, j):

        scaling_factor = 1

        if(self.Map[i][j] == Terrain.FLAT):
            scaling_factor = self.NotFound_given_Present_Flat
        elif(self.Map[i][j] == Terrain.HILLY):
            scaling_factor = self.NotFound_given_Present_Hilly
        elif(self.Map[i][j] == Terrain.FOREST):
            scaling_factor = self.NotFound_given_Present_Forest
        else:
            scaling_factor = self.NotFound_given_Present_Cave

        old_belief_i = self.Belief[i][j]
        belief_present = self.Belief[i][j]
        belief_not_present = 1 - self.Belief[i][j]

        belief_present = belief_present * scaling_factor

        self.Belief[i][j] = belief_present

        self.beta = 0
        for ii in range(0, self.dimension):
            for jj in range(0, self.dimension):
                self.beta += self.Belief[ii][jj]

        for ii in range(0, self.dimension):
            for jj in range(0, self.dimension):
                self.Belief[ii][jj] /= self.beta

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
    def getNextSearchCell(self):
        arrayBelief = np.array(self.Belief)
        maxBelief = np.where(arrayBelief == arrayBelief.max())
        print('Len of maxBelief: ' + str(len(maxBelief)))
        if(len(maxBelief[0]) > 1):
            choicePos = random.randrange(len(maxBelief[0]))
            return maxBelief[0][choicePos], maxBelief[1][choicePos]
        else:
            return maxBelief[0][0], maxBelief[1][0]

    def moveTarget(self):
        # generate a random move to next cell
        # print(self.Map[self.target_i][self.target_j])
        if(self.target_i == 0):
            if(self.target_j == 0):
                options = [[self.target_i + 1, self.target_j], [self.target_i, self.target_j + 1]]
            elif(self.target_j == self.dimension - 1):
                options = [[self.target_i + 1, self.target_j], [self.target_i, self.target_j - 1]]
            else:
                options = [[self.target_i + 1, self.target_j], [self.target_i, self.target_j - 1], [self.target_i, self.target_j + 1]]
        elif(self.target_j == 0):
            if(self.target_i == 0):
                options = [[self.target_i + 1, self.target_j], [self.target_i, self.target_j + 1]]
            elif(self.target_i == self.dimension - 1):
                options = [[self.target_i - 1, self.target_j], [self.target_i, self.target_j + 1]]
            else:
                options = [[self.target_i - 1, self.target_j], [self.target_i + 1, self.target_j], [self.target_i, self.target_j + 1]]
        elif(self.target_i == self.dimension - 1):
            if(self.target_j == 0):
                options = [[self.target_i - 1, self.target_j], [self.target_i, self.target_j + 1]]
            elif(self.target_j == self.dimension - 1):
                options = [[self.target_i - 1, self.target_j], [self.target_i, self.target_j - 1]]
            else:
                options = [[self.target_i - 1, self.target_j], [self.target_i, self.target_j - 1], [self.target_i, self.target_j + 1]]
        elif(self.target_j == self.dimension - 1):
            if(self.target_i == 0):
                options = [[self.target_i + 1, self.target_j], [self.target_i, self.target_j - 1]]
            elif(self.target_i == self.dimension - 1):
                options = [[self.target_i - 1, self.target_j], [self.target_i, self.target_j - 1]]
            else:
                options = [[self.target_i - 1, self.target_j], [self.target_i + 1, self.target_j], [self.target_i, self.target_j - 1]]
        else:
            options = [[self.target_i - 1, self.target_j], [self.target_i + 1, self.target_j], [self.target_i, self.target_j - 1], [self.target_i, self.target_j + 1]]
        move = random.choice(options)
        self.target_i = move[0]
        self.target_j = move[1]
        # print(move)
        # print(self.Map[self.target_i][self.target_j])

    def getTerrain(self):
        return str(self.Map[self.target_i][self.target_j])


    def startHunt(self):
        print('Target in: ' + str(self.target_i) + ', ' + str(self.target_j))
        while(True):
            (i, j) = self.getNextSearchCell()
            # print(self.Map[self.target_i][self.target_j])
            print('Searching: ' + str(i) + ', ' + str(j) + '\n')
            found = self.targetFound(i, j)
            if(found):
                print("Target Found")
                print('Time: ' + str(self.currentTime))
                break
            else:
                terrain_1 = self.getTerrain()
                self.moveTarget()
                print('Target in: ' + str(self.target_i) + ', ' + str(self.target_j))
                terrain_2 = self.getTerrain()
                print(terrain_1)
                print(terrain_2)
                print(self.Belief)
                self.updateBelief(i, j)
                self.currentTime += 1

def main():
    ph = ProbabilisticHunting(5)
    ph.startHunt()
    # ph.moveTarget()


if __name__ == '__main__':
    main()
