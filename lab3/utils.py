from random import randint
import networkx as nx

def generateNewValue(number1, number2):
    return randint(number1, number2)

#reprezentarea cromozomului
def reprez(ret):
    repres = [generateNewValue(0, ret['noNodes'] - 1) for _ in range(ret['noNodes'])]
    #repres=vector cu noNodes de randomuri, NOD=GENA
    for index in range(0, len(repres), 1):
        for secondIndex in range(0, len(repres)):
            if ret['mat'].item(index, secondIndex) == 1:
                repres[secondIndex] = repres[index]

    return repres


def citire(filename):
    G = nx.read_gml(filename, label='id')

    net = {}
    net['noNodes'] = G.number_of_nodes()
    net['mat'] = nx.adjacency_matrix(G).todense()
    net['noEdges'] = G.number_of_edges()
    net['degrees'] = [val for (node, val) in G.degree()]
    net['graph'] = G
    return net


 
def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for index in range(0, noNodes):
        for secondIndex in range(0, noNodes):
            if (communities[index] == communities[secondIndex]):
                Q += (mat.item(index, secondIndex) - degrees[index] * degrees[secondIndex] / M)
    return Q * 1 / M

net = citire('lesmis.gml')
problParam = {'function': modularity, 'retea': net}

def afisare(x):
    comunities = []
    for index in range(0, problParam['retea']['noNodes']+1):
        comunities.append([])
  
    for index in range(0, net['noNodes']):
        comunities[x[index]].append(index + 1)
    
    index = 0
    while index < len(comunities):
        if comunities[index] == []:
            comunities.pop(index)
        else:
            index += 1
    return comunities