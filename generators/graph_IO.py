class GraphIO:
    """ implementacija ucitavanja i ispisivanj grafa """
    def __init__(self,G):
        """ inicijalizator klase """
        self._G = G

    def read_from_edges(self,edges):
        """ ucitaj graf iz parova vrhova """

        for e in edges[0:2]:
            u,v = e[0],e[1]
            print "u,v: ", u, v
            self._G.insert_vertex(u)
            self._G.insert_vertex(v)
            self._G.insert_edge(u,v)
            self._G.show()


    def show(self):
         for u in self._G._outgoing.keys():
            print "\n%s: " % str(u.key()),
            for v in self._G._outgoing[u].keys():
               print " %s" % str(v.key()),
         print "\n"