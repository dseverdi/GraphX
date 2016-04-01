# contrib by: Luka Borozan

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random

class GraphIO:
    
    """ interface class for I/O of graph """
    @staticmethod
    def read_from_edges(G,edges):
        """metoda omogucava upis grafa preko bridova"""
        verts = set()
        
        for e in edges:
            verts.update([e[0], e[1]])
            
        for v in verts:
            G.insert_vertex(v)
            
        for e in edges:
        # ukoliko brid ima satelitske podatke dodaj ga u brid
            if len(e)==2: G.insert_edge(e[0], e[1])
            elif len(e)==3: G.insert_edge(e[0],e[1],e[2])


    @staticmethod
    def show(G,filename=None):
        """metoda ilustrira graf."""

        if not filename:
            print("|V|=",G.vertex_count(), " |E|=", G.edge_count())
            for u in G._outgoing.keys():
                print(("\n(%s): " % str(u.key())), end=' ')
                for v in G._outgoing[u].keys():
                    if G._outgoing[u][v].element(): print(("-[%2.0d]-" % (self._outgoing[u][v].element())), end=' ')
                    print(("(%s) " % str(v.key())), end=' ')

            print("\n")
            return
        else:
            fig = Figure()
            can = FigureCanvas(fig)
            obj = fig.add_subplot(111)
            pos = {}



            for v in G.vertices():
                pos[v] = (random.uniform(0.5, 4.5) * 20, random.uniform(0.5, 4.5) * 20)
                self._vert(obj, pos[v][0], pos[v][1], v)

            for e in G.edges():
                u = e.endpoints()[0].key()
                v = e.endpoints()[1].key()
                if G.is_directed():
                    self._arrow(obj, pos[u][0], pos[u][1], pos[v][0], pos[v][1])
                else:
                    self._line(obj, pos[u][0], pos[u][1], pos[v][0], pos[v][1])

            obj.axis([0, 100, 0, 100])
            can.print_figure(filename)
    
    def _line(self, obj, x1, y1, x2, y2):
        obj.plot([x1, x2], [y1, y2], 'b')
    
    def _arrow(self, obj, x1, y1, x2, y2):
        obj.annotate("", xy = (x2, y2), xytext = (x1, y1), size = 20, arrowprops = dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
    
    def _vert(self, obj, x, y, label):
        obj.plot([x], [y], 'ro', markersize = 15)
        obj.text(x, y, str(label))
        
        

