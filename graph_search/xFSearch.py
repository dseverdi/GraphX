

from graph.graph_ADT.graph import Graph


class DFSearch:
    """ klasa koja implementira depth-first-search pretrazivanje grafa"""
    def __init__(self,G):
        """konstruktor uzima referencu na graf i na njemu radi DFS pretrazivanje"""
        self._discovered = dict() # d[v] za sve v iz V kao rjecnik
        self._finished   = dict() # f[v] za sve v iz V kao rjecnik
        self._color = dict()

        self._G = G # referenca na graf parametar

        # DFS algoritam - poziv
        self.DFS()



    def DFS(self):
        """ implementacija DFS pretrazivanja """
        for u in self._G.vertices() : self._color[u]='white'
        self._time = 0
        for u in self._G.vertices():
            if self._color[u] == 'white':
                self._DFS_visit(u)

    def _DFS_visit(self,u):
        """ implementacija rekurzivnog DFS-algoritma"""
        self._color[u]='grey'
        self._time += 1
        self._discovered[u] = self._time
        for v in self._G.neighbourhood(u):
            if (self._color[v]=='white'): self._DFS_visit(v)
        self._color[u] = 'black'
        self._time += 1
        self._finished[u] = self._time

    def ord(self,u):
        """Metoda vraca par (d[u],f[u]) za dani vrh u"""
        return (self._discovered[u],self._finished[u])


from collections import deque
class BFSearch:
    """ Python implementacija BFS algoritma pretrazivanja iz nekog vrha"""
    def __init__(self,G,s):
        self._G = G
        self._s = s
        # rjecnii za pracenje podataka
        self._color = {}
        self._dist  = {}
        # prethodnici od vrhova
        self._pi    = {}
        self._queue = deque()  # efikasna struktura reda s dvostrukim krajem
        self.BFS()

    def BFS(self):
        """ BFS algoritam """
        # init step
        for u in self._G.vertices():
            self._color[u] = 'white'
            self._dist[u] = float('inf')# ili neki konacan broj, a dovoljno velik
            self._pi[u]    = None

        self._color[self._s] = 'gray'
        self._dist[self._s] =  0
        self._queue.append(self._s)  # enqueue

        while len(self._queue):
            u = self._queue.popleft() # dequeue
            for v in self._G.neighbourhood(u):
                if self._color[v] == 'white':
                    self._color[v] = 'gray'
                    self._dist[v] = self._dist[u]+1
                    self._pi[v]    = u
                    self._queue.append(v)
            self._color[u] = 'black'

    def path(self,v):
        """ metoda ispisuje vrhove na (s,v)-putu"""
        if v==self._s : print self._s,
        elif not self._pi[v]:
            print "(%s,%s)-put ne postoji" % (s,v)
        else:
            self.path(self._pi[v])
            print "-",v,
        print " "

    def distance(self,v):
        """ metoda vraca velicinu (s,v)-puta"""
        return self._dist[v]

    def tree(self):
        """ metoda ispisuje bridove koji cine BFS stablo u korijenu self._s """
        pass









