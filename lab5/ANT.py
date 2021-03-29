from random import *
from params import *
from ACO import *

#furnica
class Ant:
    def __init__(self, params: Params):
   
        self.params = params
        self.cost = 0
        randomVal=randint(0, self.params.nrTowns - 1)
        self.representation = [randomVal] 
        self.vizitat = [[0 for _ in range(self.params.nrTowns)] for _ in range(self.params.nrTowns)]
        
        

#fiecare furnica alege  urmatorul oras pe care il viziteaza 
    def alegeOrasulUrmator(self):
        suma = 0
        vector = []
        index=0
        q = random()
        while index!=self.params.nrTowns:
            vector.append(0)
            self.formulaAlfaBeta(index,vector)
            suma += vector[-1]
            index=index+1

        maximum = 0
        #regula pseudo proportionala
        # q< q0
        if q < self.params.q0:
            maximum = 0
            orasNext = 0
            index=0
            while index!=self.params.nrTowns:
                if  maximum < vector[index] :   #probabilitatea cea mai mare
                    maximum = vector[index]
                    orasNext = index    #pastrez orasul
                index=index+1
        else:
            orasNext = self.sumOfProbabilities(vector, suma)

        # marcam orasul ca vizitat si facem modificarile necesare
        self.representation.append(orasNext)
        self.vizitat[self.representation[-2]][self.representation[-1]] = 1
        self.vizitat[self.representation[-1]][self.representation[-2]] = 1
        self.cost=self.cost+ self.params.network[self.representation[-2]][self.representation[-1]] # creste costu

    def sumOfProbabilities(self, vector, suma):
 
        cities = []
        distante = []
        for j in range(self.params.nrTowns):
            if vector[j] != 0:  #daca are probabilitate,
               
                cities.append(j)
                a=vector[j] / suma
                distante.append(a)

        return choices(cities, weights=distante)[0]

    def formulaAlfaBeta(self, index, vector):
        if index not in self.representation:
            #daca nu este feromon intre ultimu oras vizitat si index
            lastTown=self.representation[-1]
            if self.params.matriceFeromon[lastTown][index] != 0:
                pi = self.params.matriceFeromon[lastTown][index] ** self.params.alpha

            else:
                pi = 1

            vector[-1] = pi*(  (1 / self.params.network[lastTown][index])**self.params.beta  )

    def revineLaStart(self):
        # ne intoarcem la primul oras (de unde am plecat)
        a=self.representation[0]
        self.representation.append(a)
        b=self.representation[-2]
        c=self.representation[-1]
        self.vizitat[b][c] = 1
        self.vizitat[c][b] = 1
    
        self.cost += self.params.network[b][c]

    def __str__(self):
        # return "Ant: " + str(self.representation) + ".cost: " + str(self.cost)
        return ".cost: " + str(self.cost)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.representation == other.representation