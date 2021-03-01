
#pb7
# al k-lea elemnt maxim din sir de numere


#complexitate O(n*log(n)
def functie(vector,k):
    
    vector.sort(reverse=True)
    return vector[k-1]
    
    
        


def test():
    x=[7,4,6,3,9,1]
    assert functie(x,2) == 7
    assert functie(x,1) == 9
    assert functie(x,3) == 6
    assert functie(x,4) == 4
test()





