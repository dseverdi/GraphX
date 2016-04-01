#   Graph ADT
#

from __future__ import print_function
class graph:
    """Reprezentacija jednostavnog grafa"""

    #------------------------- nested Vertex class -------------------------
    class Vertex:
        """Vertex objekt sa satelitskim podacima."""
        __slots__ = '_element', '_key'

        def __init__(self,k,x):
            """Konstruktor ne pozivamo eksplicitno, vec metodom unosa."""
            self._key = k
            self._element = x
                        
            
        def key(self):
            """ vrati oznaku vrha."""
            return self._key

        def element(self):
            """vrati podatak pridruzen tom vrhu."""
            return self._element

        def __hash__(self):         # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return "(%s,%s)" % (str(self._key),str(self._element))

    #------------------------- nested Edge class -------------------------
    class Edge:
        """Objekt za spremanje brida."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Ne pozivaj konstruktor ekplicitno vec preko metode unosa brida."""
            self._origin = u            
            self._destination = v
            self._element = x

        def endpoints(self):
            """Vrati par vrhova (u,v) za dani brid."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Vrati vrh koji je nasuprotan vrh ovog Edge objekta."""
            if not isinstance(v, graph.Vertex):
                raise TypeError('v mora biti vertex objekt.')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v nije incidentan tom bridu.')

        def element(self):
            """Vrati podatak koji je pridruzen tom bridu."""
            return self._element

        def __hash__(self):         # objekt je hashable
            return hash( (self._origin, self._destination) )

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin,self._destination,self._element)

        def __cmp__(self,e):
            if not isinstance(e,graph.Edge): raise ValueError('Nije valjan brid za usporedbu')
            elif self._element > e._element : return 1
            elif self._element == e._element : return 0
            else: return 0


    #------------------------- Graph methods -------------------------
    def __init__(self, directed=False):
        """Stvori neumsjeren graf, po pretpostavljenom. Graf je usmjeren ukoliko je parametar True. """
        self._vertex_map = {} # rjecnik s kljucevima (v,Vertex)
        self._outgoing = {}
        # koristi jos jedan rijecnik za ulazne bridove, ukoliko je graf usmjeren, inace koristi kao alias
        self._incoming = {} if directed else self._outgoing
    
    

    def _getVertex(self,v):
        if isinstance(v,graph.Vertex):
            return v
        elif v in self._vertex_map : return self._vertex_map[v]
        else: return None


    def _validate_vertex(self, v):
        """Utvrdi je li v vrh grafa."""
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex objekt ocekivan')
        if v not in self._outgoing:
            raise ValueError('Vrh ne pripada ovom grafu.')

    def is_directed(self):
        """Vrati je li graf usmjeren ili ne. """
        return self._incoming is not self._outgoing # directed if maps are distinct

    def vertex_count(self):
        """Vrati broj vrhova."""
        return len(self._vertex_map)

    def vertices(self):
        """Vrati oznake vrhova."""
        return list(self._vertex_map.keys())

    def edge_count(self):
        """Vrati broj bridova."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Vrati skup bridova."""
        result = set()       # koristi skup da izbjegnes iste bridove
        for secondary_map in self._outgoing.values():
            result.update(list(secondary_map.values()))    # dodaj bridove u skup
        return result

    def get_edge(self, u, v):
        """Vrati edge objekt ukoliko vrhovi u,v cine brid."""
        U,V = self._getVertex(u), self._getVertex(v)
        self._validate_vertex(U)
        self._validate_vertex(V)
        return self._outgoing[U].get(V)        # vrati None ukoliko u i v ne cini brid



    def degree(self, v, outgoing=True):
        """Vrati broj (izlaznog) stupnja vrha, inace, broj izlaznog stupnja. """
        V = self._getVertex(v)
        self._validate_vertex(V)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[V])

    def incident_edges(self, v, outgoing=True):
        """vrati sve bridove koji su incidentni s vrhom u oznaci v. """
        V = self._getVertex(v)
        self._validate_vertex(V)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[V].values():
            yield edge

    def neighbourhood(self,v):
        """ Metoda vraca vrhove s kojima je v incidentan."""
        V = self._getVertex(v)
        return [e.opposite(V).key() for e in self.incident_edges(v)]

    def insert_vertex(self,v,x=None):
        """Ubaci novi brid. """
        V = self._getVertex(v)
        if V in list(self._outgoing.values()) : raise ValueError('Vrh je vec u grafu')
        elif not V: V = self.Vertex(v,x)
        self._vertex_map[v] = V
        self._outgoing[V] = {}
        if self.is_directed():
            self._incoming[V] = {}        # jos jedan rijecnik za dolazne bridove
        return V

    def insert_edge(self, u, v, x=None):
        """Dodaj i vrati novi brid iz vrhova u oznakama u i v. """
        U,V = self._getVertex(u), self._getVertex(v)  # U,V su pridruzeni Vertex objekti kljucevima u,v
        # print "vrhovi: ", U, V, hex(id(U)), hex(id(V))
        if self.get_edge(U, V) is not None:      # includes error checking
            raise ValueError('u i v su vec incidentni')
        e = self.Edge(U, V, x)
        (self._outgoing[U])[V] = e
        (self._incoming[V])[U] = e
        # print self._outgoing

    # graph output
    def show(self):
        """ metoda ispise graf prema v: Adj[v] """
        print("|V|=",self.vertex_count(), " |E|=", self.edge_count())
        for u in self._outgoing.keys():
            print(("\n(%s): " % str(u.key())), end=' ')
            for v in self._outgoing[u].keys():
                if self._outgoing[u][v].element(): print(("-[%2.0d]-" % (self._outgoing[u][v].element())), end=' ')
                print(("(%s) " % str(v.key())), end=' ')

        print("\n")


# sucelje prema grafu/digrafu
class UndirectedGraph(graph):
    """Implementacija usmjerenog grafa kao izvedena klasa"""
    def __init__(self):
        """derived constructor """
        graph.__init__(self,directed=False)

class DirectedGraph(graph):
    """klasa usmjerenog grafa kao izvedena klasa"""
    def __init__(self):
        """izvedeni konstruktor za usmjereni graf"""
        graph.__init__(self,directed=True)
        
        
        
if __name__=="__main__":
    g = UndirectedGraph()
    g.insert_vertex('a')
    g.insert_vertex('b')
    g.insert_vertex('c')
    g.insert_edge('a','b')
    g.insert_edge('a','c')

    # print g.get_edge('a','c')
    g.show()