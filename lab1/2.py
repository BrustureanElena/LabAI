
import math
#problema 2 
# Sa se determine distanta euclediana intrw doua locatii identificate prin perechi de numere
#prima locatie,coordonatele  punctului A

#complexitatea e theta(1)

def distanta(xA,yA,xB,yB):
#xA=int(input("xA="))
#yA=int(input("yA="))

#a doua locatie, coordonatele punctului B
#xB=int(input("xB="))
#yB=int(input("yB="))


    n=(xB-xA)*(xB-xA)
    m=(yB-yA)*(yB-yA)

    a=n+m
    d=math.sqrt(a)
    return d

def test():
    assert distanta(1,5,4,1) == 5.0
    assert distanta(4,5,4,1) == 4.0
    assert distanta(7,5,7,1) == 4.0


test()
