import random
from custom_enums import Terrain

class ProbabilisticHunting:
    """Abstract class for the probabilistic hunting bot"""
    def __init__(self, dimension):
        self.Map = []
        self.Belief = []
        self.dimension = dimension
        self.target_found = False
        self.currentTime = 0
        self.beta = 1

        self.NotFound_given_Present_Flat = 0.1
        self.NotFound_given_Present_Hilly = 0.3
        self.NotFound_given_Present_Forest = 0.7
        self.NotFound_given_Present_Cave = 0.9

        self.target_i = 1
        self.target_j = 1

        self.lastSearched_i = -1
        self.lastSearched_j = -1

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

    def getBelief(self):
        raise NotImplementedError ("getBelief not implemented. Implement Override")

    def initialiseBelief(self):
        for i in range(0, self.dimension):
            self.Belief.append([])
            for j in range(0, self.dimension):
                self.Belief[i].append(1/(self.dimension * self.dimension))

    def updateBelief(self, i, j):
        raise NotImplementedError ("updateBelief not implemented. Implement Override")

    def reset(self):
        self.Belief = []
        self.currentTime = 0
        self.target_found = False
        self.initialiseBelief()

    def isTargetFound(self, i, j):

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
        #override in the child class
        raise NotImplementedError ("getNextSearchCell not implemented. Implement Override in child class")

    def startHunt(self):
        while(True):
            (self.lastSearched_i, self.lastSearched_j) = self.getNextSearchCell()
            # print('Target in: ' + str(self.target_i) + ', ' + str(self.target_j))
            # print(self.Map[self.target_i][self.target_j])
            # print('Searching: ' + str(i) + ', ' + str(j) + '\n')
            # sameSearch = 0
            # if(self.lastSearched_i == self.target_i and self.lastSearched_j == self.target_j):
            #     sameSearch += 1
            found = self.isTargetFound(self.lastSearched_i, self.lastSearched_j)
            if(found):
                print("Target Found")
                print('Time: ' + str(self.currentTime))
                # print('Target Cell Searched: ' + str(sameSearch))
                break
            else:
                self.updateBelief(self.lastSearched_i, self.lastSearched_j)
        return self.currentTime

    def RunStep(self):
        if(self.target_found == True):
            return True

        (self.lastSearched_i, self.lastSearched_j) = self.getNextSearchCell ()
        found = self.isTargetFound(self.lastSearched_i, self.lastSearched_j)
        if(found):
            self.target_found = True
            print("Target Found")
        else:
            self.updateBelief(self.lastSearched_i, self.lastSearched_j)
        self.currentTime += 1
        return found
