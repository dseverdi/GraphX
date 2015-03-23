from graph_ADT.graph import Graph
from graph_mst.mst import MSTPrim

def main():
    """ glavna test funkcija """
    G = Graph()

    verts = ('a','b','c','d','e','f','g','h','i')
    edges= (
            ('a','b',4), ('a','h',8),
            ('b','c',8),('b','h',11),
            ('c','d',7), ('c','f',4),('c','i',2),
            ('d','e',9), ('d','f',14),
            ('f','g',2),
            ('g','i',6), ('g','h',1),
            ('h','i',7)
           )

    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v,w = e[0],e[1],e[2]
        G.insert_edge(u,v,w)

    G.show()

    # MST example
    mst_G = MSTPrim(G,'a')

    print mst_G.total_weight()


if __name__ == '__main__':
    main()