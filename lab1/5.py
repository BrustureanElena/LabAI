
#pb5
#Pentru un sir cu n elementele, a.i. o singura valoare se repeta de doua ori, sa se identifice valoarea care se repeta

def valoare_repeta(x):
    frecv=[]
    for i in range(len(x)):
        frecv.append(int(0))

    for i in range(len(x)):
        frecv[x[i]]=frecv[x[i]]+1
        if frecv[x[i]]>1:
            return x[i]
    
    
    

def test():
    x=[1,2,1,3]
    assert valoare_repeta(x) == 1
    y=[2,2,4,3]
    assert valoare_repeta(y) == 2
test()





