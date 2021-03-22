from random import randint
import networkx as nx
import math
mat=[]



def generateNewValue(number1, number2):
    return randint(number1, number2)

#reprezentarea cromozomului
def reprez(ret):
    repres = [generateNewValue(0, ret['noNodes']-1 ) for _ in range(ret['noNodes'])]
    #repres=vector cu noNodes de randomuri, NOD=GENA
    for index in range(0, len(repres), 1):
        for secondIndex in range(0, len(repres)):
            if ret['mat'].item(index, secondIndex) == 1:
                repres[secondIndex] = repres[index]

    return repres



    # method that reads data from file
#params : input :mat, file
#         output: number of towns-INT, town1-SourceTown -INT,town2-DestinationTown -INT
#for easy
def readFromFile(mat, file):
  
    file = open(file, 'r')
    
    numberTowns = int(file.readline())
    m=numberTowns

    while m!=0:
        lineList = []
        line = file.readline()
        valuesL = line.split(',')
        
        for val in  valuesL:
            valInt=int(val)
            lineList.append(valInt)

        mat.append(lineList)
        m=m-1
    return numberTowns,mat


#for medium
def readFromFileMedium(mat, file):
  
    file = open(file, 'r')
    
    numberTowns = int(file.readline())
    m=numberTowns

    while m!=0:
        lineList = []
        line = file.readline()
        valuesL = line.split(' ')
        
        for val in  valuesL:
            valInt=int(val)
            lineList.append(valInt)

        mat.append(lineList)
        m=m-1
    return numberTowns,mat


def distEuclid(xA,yA,xB,yB):


    n=(xB-xA)*(xB-xA)
    m=(yB-yA)*(yB-yA)

    a=n+m
    d=math.sqrt(a)
    return d
def readFromFileCoordonat(file):
    fisier = open(file, 'r')

    n = int(fisier.readline())        

    coord = []
    for i in range(0,n):
        coordonate = []
        date = fisier.readline().split(',')
        coordonate.append(float(date[0]))
        coordonate.append(float(date[1]))
        coordonate.append(float(date[2]))
        coord.append(coordonate)     

    matrice = []
    for firstIndex in range(0,n):
        linie = []
        for secondIndex in range(0,n):
            distanta = distEuclid(coord[firstIndex][1],coord[firstIndex][2],coord[secondIndex][1],coord[secondIndex][2])
            linie.append(distanta)
        matrice.append(linie)

    fisier.close()
    return n, matrice
 #communities ii cromozolmul, adica lista de orase,param e matricea de adiacenta
def modularity(communities, param):
    cost=0
    for i in range(0,len(communities)-1):
        cost=cost+param[communities[i]][communities[i+1]]
    cost=cost+param[communities[len(communities)-1]][communities[0]]
   
    return cost

nrNoduri,mat = readFromFile(mat,'easy_01_tsp.txt')
problParam = {'function': modularity, 'retea': mat}




def afisare(x):
    comunities = []
    for index in range(0, problParam['retea']['noNodes']+1):
        comunities.append([])
  
    for index in range(0, nrNoduri):
        comunities[x[index]].append(index + 1)
    
    index = 0
    while index < len(comunities):
        if comunities[index] == []:
            comunities.pop(index)
        else:
            index += 1
    return comunities