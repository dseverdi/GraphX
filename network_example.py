from graph_ADT.graph import DirectedGraph
from network.NetworkFlow import MaxFlow
from generators.graph_IO import GraphIO
from graph_ADT.graph import graph

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

    G = graph(directed = True) 
    GraphIO(G).read_from_edges(edges)

    F = MaxFlow(G, 's', 't')
    print F.total_flow()
    print F.check_feasibility()
    for e in edges:
        print e, F.flow(e[0], e[1])


if __name__ == "__main__":
    max_flow_test()