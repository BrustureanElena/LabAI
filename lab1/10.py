#ne
#complexitate Theta(n*n)
#problema 10
# sa se identifici indexul liniei care contine cele mai multe elemente de 1
def function(matrice):
    maxim=0
    for i in range(len(matrice)):
        s=0
        for j in range(len(matrice[i])):
            if matrice[i][j]==1 :
                s=s+1
              
        if s>maxim:
            index_max=i
            maxim=s
    return index_max+1  

 


def test():
    x=[[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
    assert function(x) == 2
    a=[[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1]]
    assert function(a) == 1
    c=[[0,0,1,1,1],[0,1,1,1,1],[1,1,1,1,1]]
    assert function(c) == 3
   
test()

