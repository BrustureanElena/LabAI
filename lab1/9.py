#ne
#problema 9
#complexitate O(n^n)
def suma_submatrici(matrice,p,q,r,s):
    suma=0
    for i in range(p,r+1):
        for j in range(q,s+1):
            
            suma=suma+matrice[i][j]
          
    return suma
  

def test():

    assert suma_submatrici([[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]],2,2,4,4)==44
    assert suma_submatrici([[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]],1,1,3,3)==38
  
   
   
test()