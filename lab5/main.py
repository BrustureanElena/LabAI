from utils import *
from random import *
from ACO import *
from ANT import *
from params import *

def main():
    
    
    graph = readFromFile('fisiereInput/easy2.txt' )  # cititre normala
    lungimeGraf=len(graph)
    params = Params(70, 800, 1, 11, 0.3, 0.7, graph, lungimeGraf , [[0] *  lungimeGraf] *  lungimeGraf)


    
    aco = ACO(params)
   
   

    for gen in range(params.noGen):
        aco.initialize(params)
        i=0
        while i!=params.nrTowns - 1:
  
            # fiecare furnica face o mutare/un pas
            aco.realizeazaFurnicileMutare()
            i=i+1

        aco.revinFurnicileStart()
        params.matriceFeromon = aco.actualizeazaCantitateFeromon()
        bestFurnica = aco.furnicaCuDrumulMinim()

        print('Generatia: ' + str(gen) + ' cu reprezentarea ' + str(bestFurnica.representation) + ' si costul ' + str(
            bestFurnica.cost))

      

main()
