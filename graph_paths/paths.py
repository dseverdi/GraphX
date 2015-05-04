from graph_mst.heapdict import heapdict
from graph_ADT.graph import DirectedGraph

class SimplePath:
    """ Jednostavna klasa koja nad grafom G nalazi put izmedju vrhova u i v"""
    def __init__(self,G,u,v):
        self._G = G
        self._start, self._end = u,v
        self._visited={}
        for s in self._G.vertices() : self._visited[s]=False
        self._found = self.path(self._start,self._end)


    def path(self,u,v):
        """ rekurzivna funkcija koja induktivno provjerava postojanje puta izmedju u i v"""
        if u==v: return True
        self._visited[u] = True

        for w in self._G.neighbourhood(u):
            if not self._visited[w]:
                if self.path(w,v) : return True
        return False

    def exists(self):
        return self._found


class HamiltonPath:
    """ Brute Force algoritam za nalazenje Hamiltonovog puta. """
    def __init__(self,G,u,v):
        self._G = G
        self._start, self._end = u,v
        self._visited={}
        for s in self._G.vertices() : self._visited[s]=False
        self._found = self.path(self._start,self._end,G.vertex_count())


    def path(self,u,v,d):
        if u==v: return (d==0)
        self._visited[u] = True

        for w in self._G.neighbourhood(u):
            if not self._visited[w]:
                if self.path(w,v,d-1) : return True
        self._visited[u] = False
        return False

    def exists(self):
        return self._found



class SS_SP:
    """ algoritmi za racunanje najkracih putova u tezinskom grafu"""
    def __init__(self,G,s,method=None):
        """konstruktor klase """
        self._G = G
        self._source = s
        self._pi = {} # predacessor list
        self._d = {}


        # init step
        for v in self._G.vertices():
            self._d[v]  = float('inf')
            self._pi[v] = None
        self._d[self._source] = 0


        if method   == 'BF':
            if self.BellmanFord(): print 'Graf nema negativnih ciklusa!'
        elif method == 'D': self.Dijkstra()


    def distance(self,v):
        """vraca duljinu puta od s do v"""
        return self._d[v]

    def print_path(self,v):
        """metoda ispisuje vrhove na najkracem putu od s do v"""
        pass

    # implementacije SSSP algoritama
    def BellmanFord(self):
        """Bellman-Ford implementacija"""
        for i in range(1,self._G.vertex_count()-1):
            for e in self._G.edges():
                self._relax(e)
        for e in self._G.edges():
            u,v = e.endpoints()[0].key(), e.endpoints()[1].key()
            if self._d[v]>self._d[u]+e.element(): return False
        return True

    def Dijkstra(self):
        """Dijkstrin algoritam"""
        Q = heapdict() # rjecnik kao binarna hrpa
        for v in self._G.vertices():
            Q[v] = self._d[v]
        while len(Q):
            u, w = Q.popitem()
            for v in self._G.neighbourhood(u):
                self._relax(self._G.get_edge(u, v))


    def _relax(self,e):
        """na temelju danog brida, metoda radi relaksaciju"""
        u,v = e.endpoints()[0].key(),e.endpoints()[1].key() # ucitaj vrhove iz brida
        if self._d[v]  > self._d[u] + e.element():   # e.element = w(u,v)
            self._d[v] = self._d[u]+e.element()
            self._pi[v] = u




class AP_SP:

    def __init__(self, G, method = None):
        """po pretpostavljenom, uzmi da je FloydWarshall osnovni algoritam"""
        self._G = G # referenca na graf
        self._D = {} # matrica D u kojoj cemo spremati najkrace putove
        self._P = {} # matrica koja ce pomoci rekonstruirati put

        if method == "FW" or method == None:
            print "pozivam Bellman-Ford algoritam."
            self._FloydWarshall()

        elif method == "J":
            print "pozivam Johnson algoritam."
            self._Johnson()

        else:
            print "druga metoda nije implementirana ..."

    def _FloydWarshall(self):
        """algoritam dinamickog programiranja za nalazenje najkracih putova iz svih parova vrhova. """
        for u in self._G.vertices():
            self._D[u] = {u : 0} # trvijalna udaljenost do samog vrha
            self._P[u] = {}      # P[u]=None

            # inicijaliziraj D^1 vrijednosti


            for v in self._G.vertices():
                edge = self._G.get_edge(u,v)
                self._D[u][v] = float('inf') if edge is None else edge.element()


            if u == v or self._D[u][v] == float('inf'): self._P[u][v] = None
            else: self._P[u][v] = u

        # rekurzivno racunanje D_k
        for u in self._G.vertices():
            for v in self._G.vertices():
                for w in self._G.vertices():
                    if self._D[v][w] > self._D[v][u] + self._D[u][w]:
                        self._D[v][w] = self._D[v][u] + self._D[u][w] # azuriraj D vrijednosti
                        self._P[v][w] = self._P[u][w] # azuriraj matricu prethodnika

    def _Johnson(self):
        """Johnson algoritam za nalazenje najkracih putove u rijetkom grafu"""
        G = DirectedGraph()

        G.insert_vertex('_S')
        for u in self._G.vertices():
            self._D[u] = {}
            G.insert_vertex(u)
            G.insert_edge('_S', u, 0) # dodaj bridove (s,v)

        for e in self._G.edges():
            u,v = e.endpoints()[0].key(), e.endpoints()[1].key()
            G.insert_edge(u, v, e.element())

        BF_G = SS_SP(G, '_S', "BF")
        if not BF_G :
            print "Graf sadrzi cikluse sa nagativnim tezinama ..."
            return False

        h = {} # spremi vrijednosti BF udaljenosti
        for u in G.vertices():
            h[u] = BF_G.distance(u)
        for e in self._G.edges():
            u,v = e.endpoints()[0].key(), e.endpoints()[1].key()
            e._element = e._element + h[u] - h[v]

        for u in self._G.vertices():
            Dijkstra_G = SS_SP(self._G, u, "D")
            for v in self._G.vertices():
                self._D[u][v] = D.distance(v) + h[v] - h[u]
            self._P[u] = Dijkstra_G._pi # spremi listu za rekonstrukciju puta

    def distance(self, u, v):
        """vrati udaljenost izmedju vrhova u i v"""
        return self._D[u][v]

    def print_path(self, u, v):
        """ispisi vrhove na najkracem (u,v)-putu."""
        p, s = v, str(v)

        while True:
            if p == u : print s
            p = self._P[u][p]
            if p == None: break
            s = str(p) + "-" + s
