
#pb6
#Pentru un sir cu n elementele, a.i. sa se afiseze elementul majoritar, care apare mai mult de n/2

#O(n)

def elem_majoritar(x):
    frecv=[]
    for i in range(len(x)):
        frecv.append(int(0))

    for i in range(len(x)):
        frecv[x[i]]=frecv[x[i]]+1
        if frecv[x[i]]>len(x)/2:
            return x[i]
    
    
        


def test():
    x=[2,8,7,2,2,5,2,3,1,2,2]
    assert elem_majoritar(x) == 2
test()





