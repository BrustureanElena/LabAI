from random import randint
from utils import reprez, generateNewValue

#solutie candidat
#cromozomul are mai multe gene, adica noduri
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = reprez(problParam['retea'])
        self.__fitness = 0.0
    
    def getRepres(self):
        return self.__repres
    @property
    def repres(self):
        return self.__repres


#cat de buna e solutia mea
    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l = []):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit = 0.0):
        self.__fitness = fit




    # def crossover(self, c):
    #     offspring = Chromosome(self.__problParam)
    #     position = randint(0, c.__problParam['retea']['noNodes'] - 1)
    #     value = c.__repres[position]
    #     offspring.__repres = [self.__repres[index] if c.__repres[index] != value else value for index in
    #                           range(self.__problParam['retea']['noNodes'])]
    #     return offspring

# operatorul de incrucisare, care combina 2 potentiale solutii, adica 2 cromozomi
    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1) 
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i]) #prima parte de la primu cromozom
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])#a doua  de la al doilea
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring


    def mutation(self):
        position = randint(0, self.__problParam['retea']['noNodes']-1) # iau o gena la intamplare si pun
                                                                        # o alta valoare acolo
        self.__repres[position] = self.__repres[generateNewValue(0, self.__problParam['retea']['noNodes'] - 1)]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness