from  graph_ADT.graph                 import DirectedGraph
from  generators.graph_IO             import GraphIO
from  graph_paths.TransitiveClosure   import TransitiveClosure
from graph_search.applications        import TopologicalSort


def test_digraph():
    """test funkcija koja ucitava graf iz ntorke parova"""

    edges = ((2,3), (2,4), (3,2), (4,3), (4,1))

    DG  = DirectedGraph()
    IO = GraphIO(DG)
    IO.read_from_edges(edges)
    IO.show('digraf') # Skica grafa sprema se u direktorij .
    DG.show()

    # ispitati tranzitivni zatvarac
    tc = TransitiveClosure(DG)
    if tc.reachable(4,1):
        print 'Vrh 1 je dohvatljiv iz 4'

    ts = TopologicalSort(DG)
    print "Polozaj u topoloskom sortiranju: ", ts.ts_id(4)





if __name__ == "__main__":
    test_digraph()