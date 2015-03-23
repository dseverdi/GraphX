# klijentski program koji nutvrdjuje postojanje puta izmedju 2 vrha

from graph.graph_ADT.graph import Graph

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



