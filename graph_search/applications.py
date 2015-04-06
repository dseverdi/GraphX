from graph_ADT.graph       import DirectedGraph
from generators.graph_IO   import GraphIO
from graph_search.xFSearch import DFSearch


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





class AllPairsSP:
    """ racunanje svih najkracih putova u (netezinskom) neusmjerenom grafu."""

    def __init__(self,G):
        """ inicijalizator klase """
        self._G = G
        self._sp_pairs = {v:{} for v in self._G.vertices()}
        self._sp_paths = {v:{} for v in self._G.vertices()}

        # inicijaliziriaj matricu s sp udaljenostima
        for u in self._G.vertices():
            for v in self._G.vertices():
                self._sp_pairs[u][v] = float('inf')
                self._sp_paths[u][v] = None


        from xFSearch import BFSearch

        for u in self._G.vertices():
            bfs_G = BFSearch(self._G,u)
            for v in self._G.vertices():
                if bfs_G.distance(v)< self._sp_pairs[u][v]:
                    self._sp_pairs[u][v] =  bfs_G.distance(v)
                    # dodati rekonstrukciju puta
                    self._sp_paths[u][v] = bfs_G.pi(v)



    def sp(self,u,v):
        """ metoda vraca duljinu najkraceg puta"""
        return self._sp_pairs[u][v]


    def print_sp(self,u,v):
        """ metoda vraca vrhove na (u,v)-putu"""
        if not self.sp(u,v)<float('inf'): print "(%s,%s)-put ne postoji" % (s,v)
        if u == v: print u,
        else:
            self.print_sp(u,self._sp_paths[u][v])
            print "-", v,


class TopologicalSort:
    """
    algoritam definira topoloski uredjaj vrhova grafa,
    pretpostavka: G je DAG
    """
    def __init__(self,G):
        """inicijalizacija algoritma"""
        # lista vrhova u toploskom sortiranju
        self._ts = {}
        if isinstance(G,DirectedGraph):
            self._G = G
            self.TS()
        else:
            # self._G = GraphIO.dag(G)
            pass


    def TS(self):
        """algoritam topoloskog sortiranja"""
        dfs = DFSearch(self._G)
        ts_pairs = sorted([(u,dfs.ord(u)[1]) for u in self._G.vertices()],key = lambda element: element[1],reverse=True)
        ts = [x[0] for x in ts_pairs]
        self._ts = {x[0]:ts_pairs.index(x) for x in ts_pairs}
        print "TS:" ,ts

    def ts_id(self,u):
        """vrati polozaj vrha u topolskom sortiranju"""
        return self._ts[u]







class SCC:
    def __init__(self,G):
        """ konstruktor klase"""
        pass

    def calculateSCC(self):
        """implementacija prema opisanom algoritmu"""
        pass

    def count(self):
        """ metoda vraca broj SCC-a"""

    def scc_id(self,v):
        """ metoda vraca identifikator SCC-a za vrh v"""
        pass

    def strongly_reachable(self,u,v):
        """metoda koja provjerava snaznu dohvatljivost izmedju vrhova u i v"""
        pass


