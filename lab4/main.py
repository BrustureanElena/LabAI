from GA import GA
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 
import warnings 
import math
from utils import citire, modularity, afisare,generateNewValue,readFromFile,readFromFileMedium,readFromFileCoordonate

from random import seed 
mat = []
nrNoduri,mat = readFromFile(mat,'easy_01_tsp.txt')

gaParam = {"popSize": 15, "noGen": 50, "network": mat}
problParam = {'function': modularity, 'retea': mat,'noNodes':nrNoduri}


def main():
    
    ga = GA(gaParam, problParam)
    ga.initialisation() # fac o initializare, generez 300 de cromozomi si ii adaug in populatie
    ga.evaluation()   
    
   
    for g in range(gaParam['noGen']):
      
        ga.oneGenerationElitism()
        
        
        bestChromo = ga.bestChromosome()
        
        #print(bestChromo.repres)
        a=[]
        for x in bestChromo.repres:
            a.append(x+1)
        print(a)
        print(bestChromo.fitness)
        
  

main()
