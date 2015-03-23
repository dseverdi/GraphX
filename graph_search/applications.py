class ConnectedComponents:
    """ koristeci DFS algoritam odrediti povezane komponente"""
    def __init__(self,G):
        """ uz pomoc DFS nalazi CC grafa"""
        # rjecnik koji sadrzi identifikator povezane klase za vrh
        self._G = G
        self._ccnt = 0
        self._cc = {v:-1 for v in self._G.vertices()}
        # poziv DFS za racunanje CC-a
        self.CC()


    def CCSearch(self,u):
        """ rekurzivno pretrazivanje DFS-om za identifikaciju CC-a """
        self._cc[u] = self._ccnt
        for v in self._G.neighbourhood(u):
            if self._cc[v]==-1 : self.CCSearch(v)

    def CC(self):
        """ pozovi DFS na nekom vrhu od CC-a, postupak obidje sve CC"""
        for u in self._G.vertices():
            if self._cc[u]==-1:
                self.CCSearch(u)
                self._ccnt += 1

    def count(self):
        """metoda vraca ukupni broj povezanih komponenti"""
        return self._ccnt

    def connect(self,u,v):
        """ metoda vraca True ukoliko se u i v nalaze u istoj komponenti"""
        return self._cc[u]==self._cc[v]


class GraphColorability:
    """ algoritam provjerava je li graf 2 obojiv"""
    def __init__(self,G):
        self._G = G
        self._vertex_color = {}
        self._OK = self.bipartite()


    def dfs_2_color(self,u,color):
        self._vertex_color[u]= (color+1) % 2
        for v in self._G.vertices():
            if self._vertex_color[v]==-1:
               if not self.dfs_color(v,self._vertex_color[v]):  return false
            elif self._vertex_color[v]<>color: return false
            else: return True


    def bipartite(self):
        for u in self._G.vertices():
            if self._vertex_color[u]==-1:
                if not self.dfs_2_color(v,0):
                    return False

    def color(self,v):
        """ metoda vraca  boju vrha """
        print self._vertex_color[v]


