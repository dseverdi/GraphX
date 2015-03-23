# Graph client interface for generating graphs from edges
#
#

from graph.graph_ADT.graph import Graph
from graph.generators.random_generator import RandomGraph
from graph.graph_paths.paths import SimplePath, HamiltonPath



def main():
    g = Graph(False)

    g.insert_vertex('a')
    g.insert_vertex('b')
    g.insert_vertex('c')
    g.insert_edge('a','b')
    g.insert_edge('a','c')

    # print g.get_edge('a','c')
    g.show()

    random_graph = RandomGraph(5,5)
    random_graph.show()


    sp = SimplePath(random_graph,1,2)
    print sp.exists()

    hp = HamiltonPath(random_graph,1,2)
    print hp.exists()






if '__main__':
    main()




