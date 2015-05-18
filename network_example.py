from graph_ADT.graph import DirectedGraph
from network.NetworkFlow import MaxFlow
from generators.graph_IO import GraphIO

def max_flow_test():
    """testiranje problema maksimalnog toka."""
    net1 = DirectedGraph()

    # primjer 1
    edges = (
            ('s','w',3), ('s','y',2),
            ('w','x',2),
            ('x','y',1), ('x','z',2),('x','t',3),
            ('y','s',1), ('y','z',3),
            ('z','x',3), ('z','t',2)

           )

    net1_IO = GraphIO(net1)
    net1_IO.read_from_edges(edges)
    net1_IO.show()


if __name__ == "__main__":
    max_flow_test()