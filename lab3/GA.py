from random import randint
from Chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = [] #tine minte solutiile potentiale

    @property
    def population(self): #generam populatiade 300 de cromozomi
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']): # 
            c = Chromosome(self.__problParam) #generam 300 de cromozomi cu problParam
            self.__population.append(c)       #ii adaugam in populatie

    def evaluation(self):
        for c in self.__population: #face fitnessul la fiecare chromozom
            c.fitness = self.__problParam['function'](c.repres,self.__param["network"])
                            #se apeleaza modularity ()

    def bestChromosome(self): #cea mai buna solutie din populatie
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def worstChromosome(self): #cea mai rea solutie din populatie
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):# procedeu de selectie, iau 2 solutii avute in populatie, la intamplare si o aleg pe cea mai buna
                        # prin intermediul fitnessului
        pos1 = randint(0, self.__param["popSize"] - 1)
        pos2 = randint(0, self.__param["popSize"] - 1)
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param["popSize"]): #pana am 300 de noi cromozomi
            #doua potentiale solutii
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2) # amestesc  cromozomii pe p1 si p2, combina informatia genetica
            off.mutation()   #fac mutatia pun si niste pete
            newPop.append(off) #in populatia noua adaug solutia nou generata
            #cand mi s o umplut populatia noua, fac switchul
        self.__population = newPop  
        self.evaluation() #fac evolutia sa vad cat de buni sunt acesti noi indivizi