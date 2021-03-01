
#problema 3 
#sa se determine produsul scalar a doi vectori care contin numere reale


def function(x,y):
    a=0
    for i in range(len(x)):
        if x[i]!=0 and y[i]!=0:
            a=a+x[i]*y[i]
    return a


def test():
    x=[1,0,2,0,3]
    y=[1,2,0,3,1]
    assert function(x,y) == 4
    x=[1,0,2,0,0]
    y=[1,2,0,3,1]
    assert function(x,y) == 1
    x=[1,0,2,1,1]
    y=[1,2,0,3,1]
    assert function(x,y) == 5

test()