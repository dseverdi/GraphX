from graph_ADT.graph import Graph
from graph_search.xFSearch import DFSearch, BFSearch
from graph_search.applications import ConnectedComponents, AllPairsSP


def test_dfs():
    """ DFS primjer """
    verts=('u','v','w','x','y','z')
    edges = (('u','v'),('u','x'),('v','y'),('w','y'),('w','z'),('x','v'),('y','x'),('z','z'))
    G = Graph(directed=True)
    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v = e[0],e[1]
        G.insert_edge(u,v)

    G.show()

    # DFS pretrazivanje grafa G
    dfs_G = DFSearch(G1)
    for v in G.vertices():
        print str(v),": ", dfs_G.ord(v)


def test_bfs():
    """test BFS"""
    # BFS primjer
    G = Graph()
    verts = ('r','s','t','u','v','w','x','y')
    edges = (('r','v'),('r','s'),('s','w'),('t','w'),('t','x'),('t','u'),('u','x'),('u','y'),('w','x'),('x','y'))
    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v = e[0],e[1]
        G.insert_edge(u,v)

    G.show()
    bfs_G = BFSearch(G2,'s')
    for u in G.vertices() : print "d[%s]=%d" % (u,bfs_G.distance(u))

    bfs_G.path('u')


def test_cc():
    """test CC algorithm """
    # CC primjer
    G = Graph()
    verts = tuple(range(13))
    edges = ((0,1),(0,2),(0,5),(0,6),(3,4),(3,5),(7,8),(9,10),(9,11),(9,12),(11,12))

    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v = e[0],e[1]
        G.insert_edge(u,v)

    G.show()

    cc_G = ConnectedComponents(G)
    print "broj povezanih komponenti ", cc_G.count()


def test_all_pair_sp():
    """ test all-pair-shortest-path """
    G = Graph()
    verts = ('r','s','t','u','v','w','x','y')
    edges = (('r','v'),('r','s'),('s','w'),('t','w'),('t','x'),('t','u'),('u','x'),('u','y'),('w','x'),('x','y'))
    for u in verts:
        G.insert_vertex(u)
    for e in edges:
        u,v = e[0],e[1]
        G.insert_edge(u,v)

    G.show()


    all_sp_G = AllPairsSP(G)

    print "Najkraci put u G od 'r' do 'w':", all_sp_G.sp('r', 'w')
    print all_sp_G.print_sp('r','w')



def main():
    test_all_pair_sp()





    # all-pairs shortest path





if __name__ == '__main__':
    main()
