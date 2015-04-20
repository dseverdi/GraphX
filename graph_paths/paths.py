

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
        for i in range(1,G.vertex_count()-1):
            for e in self._G.edges():
                self.relax(e,w)
        for e in self._G.edges():
            u,v = e.endpoints()
            if self._d[v]>self._d[u]+e.element(): return False
        return True

    def Dijkstra(self):
        """Dijsktrin algoritam"""
        pass

    def _relax(self,e,w):
        """na temelju danog brida, metoda radi relaksaciju"""
        u,v = e.endpoints() # ucitaj vrhove iz brida
        if self._d[v]<self._d[u]+e.element():   # e.element = w(u,v)
            self._d[v] = self._d[u]+e.element()
            self._pi[v] = u



