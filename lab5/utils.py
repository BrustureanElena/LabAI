from math import sqrt
import math
mat=[]

def readFromFile( file):
  
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
    return mat


def distanceEuclid(xA,yA,xB,yB):


    n=(xB-xA)*(xB-xA)
    m=(yB-yA)*(yB-yA)

    a=n+m
    d=math.sqrt(a)
    return d

def readFromFileCoordonate(file):
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
            distanta = distanceEuclid(coord[firstIndex][1],coord[firstIndex][2],coord[secondIndex][1],coord[secondIndex][2])
            linie.append(distanta)
        matrice.append(linie)

    fisier.close()
    return  matrice