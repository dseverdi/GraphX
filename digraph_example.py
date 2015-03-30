from  graph_ADT.graph                 import Graph
from  generators.graph_IO             import GraphIO
from  graph_paths.TransitiveClosure   import TransitiveClosure


def test_digraph():
    """test funkcija koja ucitava graf iz ntorke parova"""

    edges = ((2,3), (2,4), (3,2), (4,3), (4,1))

    DG  = Graph(directed = True)
    IO = GraphIO(DG)
    IO.read_from_edges(edges)
    IO.show('digraf') # Skica grafa sprema se u direktorij .
    DG.show()

    # ispitati tranzitivni zatvarac
    tc = TransitiveClosure(DG)
    if tc.reachable(4,1):
        print 'Vrh 1 je dohvatljiv iz 4'





if __name__ == "__main__":
    test_digraph()