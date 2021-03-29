from ANT import *
from params import *


class ACO:
    def __init__(self, params: Params):
        self.params = params
        self.population = []

    def initialize(self, problemParam):
        self.population = []

        index=0
        while index!=self.params.noOfAnts:
            self.population.append(Ant(self.params))
            index+=1

#fiecare furnica face o mutare
    def realizeazaFurnicileMutare(self):
        for f in self.population:
            f.alegeOrasulUrmator()



    def actualizeazaCantitateFeromon(self):
        # pentru fiecare oras actualizam feromonii (tinand cont si de drumul furnicilor si de evaporare)
        index=0
        while index!=self.params.nrTowns:
            for j in range(self.params.nrTowns):
                newPhero = 0
                self.updateLocalferomon(index, j, newPhero)
            index+=1
        return self.params.matriceFeromon

    def updateLocalferomon(self, index, j, newPhero):
        for ant in self.population:
            if ant.pheromoneLevel[index][j] == 1:   
                a=1 / ant.cost
                newPhero =newPhero+a
        t1= (1 - self.params.evaporation)
        t2= self.params.matriceFeromon[index][j]
        self.params.matriceFeromon[index][j] = t1*t2 
        self.params.matriceFeromon[index][j] +=newPhero


    def furnicaCuDrumulMinim(self):
        fBest = self.population[0]
        for ant in self.population:
            if ant.cost < fBest.cost: 
                fBest = ant
        return fBest

    def revinFurnicileStart(self):
        for f in self.population:
         
            f.revineLaStart()    
