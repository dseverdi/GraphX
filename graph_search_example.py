from graph_ADT.graph import Graph
from graph_search.xFSearch import DFSearch,BFSearch
from graph_search.applications import ConnectedComponents


def main():
    # DFS primjer
    verts1=('u','v','w','x','y','z')
    edges1 = (('u','v'),('u','x'),('v','y'),('w','y'),('w','z'),('x','v'),('y','x'),('z','z'))
    G1 = Graph(directed=True)
    for u in verts1:
        G1.insert_vertex(u)
    for e in edges1:
        u,v = e[0],e[1]
        G1.insert_edge(u,v)

    G1.show()

    # DFS pretrazivanje grafa G
    dfs_G1 = DFSearch(G1)
    for v in G1.vertices():
        print str(v),": ", dfs_G1.ord(v)


    # BFS primjer
    G2 = Graph()
    verts2 = ('r','s','t','u','v','w','x','y')
    edges2 = (('r','v'),('r','s'),('s','w'),('t','w'),('t','x'),('t','u'),('u','x'),('u','y'),('w','x'),('x','y'))
    for u in verts2:
        G2.insert_vertex(u)
    for e in edges2:
        u,v = e[0],e[1]
        G2.insert_edge(u,v)

    G2.show()
    bfs_G2 = BFSearch(G2,'s')
    for u in G2.vertices() : print "d[%s]=%d" % (u,bfs_G2.distance(u))

    bfs_G2.path('u')

   # CC primjer
    G3 = Graph()
    verts3 = tuple(range(13))
    edges3 = ((0,1),(0,2),(0,5),(0,6),(3,4),(3,5),(7,8),(9,10),(9,11),(9,12),(11,12))

    for u in verts3:
        G3.insert_vertex(u)
    for e in edges3:
        u,v = e[0],e[1]
        G3.insert_edge(u,v)

    G3.show()

    cc_G3 = ConnectedComponents(G3)
    print "broj povezanih komponenti ", cc_G3.count()


if __name__ == '__main__':
    main()
