#ne
#problema 8
def binary_list(n):
    z=[]
    for x in range(n):
        z.append(bin(x))
    return z




def test():

    assert binary_list(4)==['0b0', '0b1', '0b10', '0b11']
    assert binary_list(7)==['0b0', '0b1', '0b10', '0b11', '0b100', '0b101', '0b110']
    
test()
