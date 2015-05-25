# Ford Fulkerson and Edmonds-Karp implementation

class MaxFlow:
    """ Max-FLow implementacija u klijentskom programu """

    def _EdmondsKarp(self):

        self._c = {}

        for e in self._G.edges():
            u = e.endpoints()[0].key()
            v = e.endpoints()[1].key()
            self._f[(u, v)] = 0
            self._f[(v, u)] = 0
            self._c[(u, v)] = e.element()
            if self._G.get_edge(v, u):
                self._c[(v, u)] = self._G.get_edge(v, u).element()
            else:
                self._c[(v, u)] = 0

        while (True):

            p = self._BFS()
            if (p == {}): return
            q = p.copy()

            m = float('inf')
            w = self._sink
            while(q[w] != None):
                if m > self._c[(q[w], w)]: m = self._c[(q[w], w)]
                w = q[w]

            w = self._sink
            while (q[w] != None):
                e = (p[w], w)
                u, v = e[0], e[1]
                self._f[(u, v)] = self._f[(u, v)] + m
                self._f[(v, u)] = -self._f[(u, v)]
                self._c[(u, v)] = self._G.get_edge(u, v).element() - self._f[(u, v)]
                if self._G.get_edge(v, u):
                    self._c[(v, u)] = self._G.get_edge(v, u).element() - self._f[(v, u)]
                else:
                    self._c[(v, u)] = -self._f[(v, u)]
                w = q[w]

    """implementacija problem maksimalnog mreznog toka."""
    def __init__(self,G,s,t):
        self._G = G
        self._source = s
        self._sink = t
        self._f = {}
        self._EdmondsKarp()


    def check_feasibility(self):
        """metoda provjerava dopustivost toka u mrezi"""
        for e in self._G.edges():
            u,v = e.endpoints()[0].key(), e.endpoints()[1].key()
            if (self._f[(u,v)] > e.element()): return False
        return True

    def flow(self,u,v):
        """provjeri tok na bridu (u,v)"""
        return self._f[(u,v)]

    def total_flow(self):
        """ukupan tok iz s do t"""
        self._total = 0
        for v in self._G.vertices():
            self._x = self._G.get_edge(self._source,v)
            if self._x :
                u = self._x.endpoints()[0].key()
                v = self._x.endpoints()[1].key()
                self._total += self._f[(u, v)]
        return self._total

    def _BFS(self):
        V = {}
        p = {}
        q = []

        for u in self._G.vertices():
            V[u] = False
            p[u] = None

        V[self._source] = True
        q.append(self._source)

        while len(q):
            u = q.pop(0)
            if u == self._sink: return p
            for v in self._G.neighbourhood(u):
                b = True
                e = self._G.get_edge(u, v)
                if e: b = e.element() > self._f[(u, v)]
                if not V[v] and b:
                    V[v] = True
                    p[v] = u
                    q.append(v)
            V[u] = True

        return {}


