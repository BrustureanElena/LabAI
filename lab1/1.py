
#neprezentata
#complexitate O(nlogn)
def function(sir):
    nr=0
    for i in range(len(sir)):
        if sir[i]==" ":
            nr=nr+1
    sir=sir.split(" ")
    sir.sort(reverse=False)
   
    return sir[nr]



def test():
     assert function("rosii si galbene")=="si"
     assert function("Ana are mere rosii si galbene")=="si"
     assert function("aaa bbb ccc aaa")=="ccc"
     assert function("para aa bbb")=="para"
     assert function("aa zz uu zy")=="zz"
    
test()

