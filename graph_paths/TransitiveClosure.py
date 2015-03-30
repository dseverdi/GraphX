class TransitiveClosure:
    """ algoritam koji racuna tranzitivni zatvarac"""
    def __init__(self,G):
        """ konstruktor algoritma """
        self._G = G
        self._tc = {v:{} for v in self._G.vertices()}
        self.TC()

    def TC(self):
        """ Warshallov algoritam dinamickog programiranja"""
        for u in self._G.vertices():
            for v in self._G.vertices():
                self._tc[u][v] = True if self._G.get_edge(u,v) or u==v else False

        tc_new = {v:{} for v in self._G.vertices()}


        for w in self._G.vertices():
            for u in self._G.vertices():
                for v in self._G.vertices():
                   tc_new[u][v] = self._tc[u][v] or (self._tc[u][w] and self._tc[w][v])

            # kad zavrsis u,v parove kreni na sljedecu iteraciju
            self._tc = tc_new



    def reachable(self,u,v):
        """provjeri je li v dohvatljiv iz u """
        return self._tc[u][v]


