
import itertools
import random
from ..graph_ADT.graph import Graph

def RandomGraph(V,E):
    """ generator generira graf s ocekivanim brojem bridova E  """
    p = 2.0*E/float(V)/float(V-1) # vjerovatnost odabira brida izmedju u,v
    g = Graph()
    vert_labels = range(V)
    for label in vert_labels:
        g.insert_vertex(label)
    for (u,v) in list(itertools.combinations(range(V),2)):
        if random.random()<p : g.insert_edge(u,v)

    return g