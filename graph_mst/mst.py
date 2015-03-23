# Python implementacija MST algoritma
from  heapdict import heapdict # koristi implementaciju prioritetnog reda preko hrpe

class MSTPrim:
    """Primov algoritam za racunanje MST-a"""
    def __init__(self,G,r):
        """ inicijalizator algoritma"""
        self._G = G
        self._r  = r
        self._key = {}
        self._pi =  {}
        self._weight = 0.0

        # start Prim algorithm
        self.prim()




    def prim(self):
        """ Primov algoritam """
        # inicijalizacija
        Q = heapdict()  # prioritetni red kao rjecnik
        for u in self._G.vertices():
            self._key[u] = float('inf')
            self._pi[u]  = None

        self._key[self._r] = 0 # incijalna vrijednost za pocetni vrh
        for v in self._G.vertices():
            Q[v] = self._key[v]


        # nalazenje sigurnog brida
        while len(Q):
            item = Q.popitem() # skini element s vrha
            u,wt = item[0], item[1]
            self._weight += wt  # racunaj ukupnu tezinu
            for v in self._G.neighbourhood(u):
                w = self._G.get_edge(u,v).element()
                if v in Q and w<self._key[v]:
                    self._pi[v]  = u
                    Q[v] = self._key[v] = w

    def total_weight(self):
        """ metoda vraca tezinu bridova u MST"""
        return self._weight

    def MSTree(self):
        """ metoda ispisuje MST stablo s korijenom r """
        pass












# Implementacija kruskalovog algoritma


class MSTKruskal:
    """ Nalazenje minimalnog razapinjujuceg stabla tezinskog grafa """
    def __init__(self,G):
        """ inicijaliziraj MST algoritam """
        self._G = G
        self._mst_forrest = []
        self._disjoint_set = DisjointSet()

    def kruskal(self):
        """ implementacija Kruskalovog algoritma """
        for e in self._G.edges().sort():
            u,v = e.origin(), e.destination()
            if self._disjoint_set.find_set(u)==self._disjoint_set.find_set(v):
                self._mst_forrest.append(e)
                self._disjoint_set.union(u,v)

    def total_weight():
        """ metoda vraca ukupnu tezinu MST-a"""
        pass

    def MSTree():
        """ metoda vraca bridove koji tvore stablo """
        pass


