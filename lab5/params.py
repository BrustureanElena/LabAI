

class Params:
    def __init__(self, noAnts, noGen, alpha, beta, evaporation, q0, network, towns, feromons):
        self.noOfAnts = noAnts
        self.noGen= noGen
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.q0 = q0
        self.network = network  #graph
        self.nrTowns = towns   #orasele
        self.matriceFeromon = feromons   #matricea cu feromoni

