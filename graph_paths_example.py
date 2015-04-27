
from graph_ADT.graph import DirectedGraph
from graph_paths.paths import SS_SP,AP_SP

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
        DG.insert_vertex(u)
    for e in edges:
        u,v,w = e[0],e[1],e[2]
        DG.insert_edge(u,v,w)



    sp_DG = SS_SP(DG,'s','BF')
    print "duljina najkraceg puta od vrha 's' do 'z':{0}".format(str(sp_DG.distance('z')))



def test_apsp():
    # usmjereni graf
    DG = DirectedGraph()
    # definiraj vrhove i bridove
    verts = (1,2,3,4,5)
    edges= (
        (1,2,3), (1,3,8), (1,5,-4),
        (2,4,1),(2,5,7),
        (3,2,4),
        (4,1,2),(4,3,-5),
        (5,4,6)
           )

    for u in verts:
        DG.insert_vertex(u)
    for e in edges:
        u,v,w = e[0],e[1],e[2]
        DG.insert_edge(u,v,w)


    # pozovi APSP algoritme
    apsp_DG = AP_SP(DG)
    print "udaljenost vrhova 1 i 4:", apsp_DG.distance(1,4)




if __name__ == "__main__":
    test_sssp()
    test_apsp()