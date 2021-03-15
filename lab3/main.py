from GA import GA
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 
import warnings 
import math
from utils import citire, modularity, afisare,generateNewValue

from random import seed 

net = citire('lesmis.gml')

gaParam = {"popSize": 300, "noGen": 3, "network": net}
problParam = {'function': modularity, 'retea': net}

def fcEval(x):
    # sphere function 
    # val = sum(xi ** 2 for xi in x)

    # Rastrigin function 
    term1 = sum(xi ** 2 / 4000 for xi in x)
    cosinus = np.cos([xi for xi in x])
    cosinus = [cosinus[i] / math.sqrt(i + 1) for i in range(len(x))]
    term2 = np.prod([c for c in cosinus], axis = 0)
    val = term1 - term2 + 1
    val = 20 + sum(xi ** 2 - 10 * np.cos(2 * np.pi * xi) for xi in x)
    
    return val

def afisare_graf(network):
    warnings.simplefilter('ignore')

    A=np.matrix(network["mat"])
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(8, 8))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()

def afisare_comunitati(network,bestChromo):
    communities = [1,2,1,2,1, 1]

    A=np.matrix(network["mat"])
    partition=bestChromo.getRepres()
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(8, 8))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size = 600, cmap = plt.cm.RdYlBu, node_color=list(bestChromo.getRepres()))
    nx.draw_networkx_edges(G, pos, alpha = 0.3)
    plt.show()

def plotAFunction(xref, yref, x, y, xoptimal, yoptimal, message):    
    plt.plot(xref, yref, 'b-')
    plt.plot(x, y, 'ro', xoptimal, yoptimal, 'bo')
    plt.title(message)
    plt.show()
    plt.pause(0.9)
    plt.clf()


def desen(ret):
    seed(1)
# plot the function to be optimised
    noDim = 1
    xref =  [[generateNewValue(0, ret['noNodes'] - 1)  for _ in range(noDim)] for _ in range(0, 1000)]
    xref.sort()
    yref = [fcEval(xi) for xi in xref]   
    plt.ion()
    plt.plot(xref, yref, 'b-')
    plt.xlabel('x values')
    plt.ylabel('y = f(x) values')
    plt.show()

    # initialise de GA parameters
  #  gaParam = {'popSize' : 10, 'noGen' : 3, 'pc' : 0.8, 'pm' : 0.1}
    # problem parameters
   # problParam = {'min' : MIN, 'max' : MAX, 'function' : fcEval, 'noDim' : noDim, 'noBits' : 8}

    # store the best/average solution of each iteration (for a final plot used to anlyse the GA's convergence)
    allBestFitnesses = []
    allAvgFitnesses = []
    generations = []


    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
        
    for g in range(gaParam['noGen']):
        #plotting preparation
        allPotentialSolutionsX = [c.repres for c in ga.population]
        allPotentialSolutionsY = [c.fitness for c in ga.population]
        bestSolX = ga.bestChromosome().repres
        bestSolY = ga.bestChromosome().fitness
        allBestFitnesses.append(bestSolY)
        allAvgFitnesses.append(sum(allPotentialSolutionsY) / len(allPotentialSolutionsY))
        generations.append(g)
        plotAFunction(xref, yref, allPotentialSolutionsX, allPotentialSolutionsY, bestSolX, [bestSolY], 'generation: ' + str(g))

        #logic alg
        ga.oneGeneration()
        # ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()
        
        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
        
        plt.ioff()
        best, = plt.plot(generations, allBestFitnesses, 'ro', label = 'best')
        mean, = plt.plot(generations, allAvgFitnesses, 'bo', label = 'mean')
        plt.legend([best, (best, mean)], ['Best', 'Mean'])
        plt.show()
def main():
    ga = GA(gaParam, problParam)
    ga.initialisation() # fac o initializare, generez 300 de cromozomi si ii adaug in populatie
    ga.evaluation()   # evaluez fitness-ul, sa vad cat de buni sunt cu functia modularity
    
   
    for g in range(gaParam['noGen']):
      
        ga.oneGeneration()
        
        
        bestChromo = ga.bestChromosome()
        
        print('In generatia ' + str(g) + ' cel mai bun cromozom: ' + str(afisare(bestChromo.repres)) + ' f(x) = ' + str(
            bestChromo.fitness) + ' ' + 'nr. comunitati:' + str(len(afisare(bestChromo.repres))))
        
    afisare_comunitati(gaParam['network'],bestChromo)
    afisare_graf(gaParam['network'])
    
    #desen(problParam['retea'])

main()
