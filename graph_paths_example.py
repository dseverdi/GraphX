
from graph_ADT.graph import DirectedGraph
from graph_paths.paths import SS_SP

def test_sssp():
    """test funkcija koja ucitava graf iz ntorke parova"""

     """ glavna test funkcija """
    DG = DirectedGraph()

    verts = ('s','t','x','y','z')
    edges= (
        ('s','t',10), ('s','y',5),
        ('t','x',2), ('t','y',1),
        ('x','z',4),
        ('y','t',3), ('y','x',9), ('y','z',2),
        ('z','s',7), ('z','x',6)
           )

    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v,w = e[0],e[1],e[2]
        G.insert_edge(u,v,w)



    sp_DG = SS_SP(DG,'s','BF')
    print 'duljina najkraceg puta od vrha 0 do 3:{0}'.format(str(sp_DG.distance(3)))






if __name__ == "__main__":
    test_sssp()