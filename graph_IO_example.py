from  graph_ADT.graph          import Graph
from  generators.graph_IO       import GraphIO
from  graph_search.applications import ConnectedComponents


def test_show():
    """test funkcija koja ucitava graf iz ntorke parova"""
    
    edges = ((0, 1), (0, 2), (0, 5), (0, 6), (5, 3), (5, 4), (3, 4), (6, 4), (7, 8), (9, 10), (9, 11), (9, 12), (11, 12))
    
    G  = Graph(directed = False)
    IO = GraphIO(G)
    IO.read_from_edges(edges)
    IO.show('slika_grafa') # Skica grafa sprema se u direktorij.

    C = ConnectedComponents(G)
    print "Broj povezanih komponenti: ", C.count()
    print "(", 0, ", ", 0, ") connected: ", C.connect(0, 0)
    print "(", 0, ", ", 1, ") connected: ", C.connect(0, 1)
    print "(", 8, ", ", 7, ") connected: ", C.connect(8, 7)
    print "(", 0, ", ", 7, ") connected: ", C.connect(0, 7)
    print "(", 10, ", ", 12, ") connected: ", C.connect(10, 12)
    print "(", 0, ", ", 4, ") connected: ", C.connect(0, 4)
    

    
if __name__ == "__main__":
    test_show()