
#ne
#complexitate O(nlogn)
def function(sir):
    nr=0
    for i in range(len(sir)):
        if sir[i]==" ":
            nr=nr+1
    sir=sir.split(" ")
    sir.sort(reverse=False)
    k=0
    final=""
    for i in range(nr+1):
        if i!=nr:
            if sir[i]==sir[i+1]:
                k=1
            else:
                if k==0:
                    final=final+" "+sir[i]
                k=0

    if sir[nr]!=sir[nr-1]:
        final=final+" "+ sir[nr]        
    return final



def test():

    assert function("ana are ana are mere rosii")==" mere rosii"
    assert function("ana are ana are mere rosii rosii")==" mere"
    assert function("ana are ana are mere pere")==" mere pere"
    
test()

