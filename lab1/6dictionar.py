
#ne
#problema 6 cu dictionar

#pb6
#Pentru un sir cu n elementele, a.i. sa se afiseze elementul majoritar, care apare mai mult de n/2
#O(n)


def functie(sir):
    frecv={}
    for x in sir:
        frecv[x]=0

    for x in sir:
            frecv[x]=frecv[x]+1
  
    for x in sir:
        if frecv[x]>len(sir)/2:
            return x  
        


def test():
    x=[2,8,7,2,2,5,2,3,1,2,2]
    assert functie(x) == 2
    x=[10,10,4,3,10]
    assert functie(x) == 10
test()





