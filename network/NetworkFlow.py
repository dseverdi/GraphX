# Ford Fulkerson and Edmonds-Karp implementation

class MaxFlow:
    """implementacija problem maksimalnog mreznog toka."""
    def __init__(self,G,s,t):
        self._G = G
        self._source, self._sink = s, t


    def _EdmondsKarp(self):
        """Edmonds-Karp algoritam koji koristi BFS verziju Ford-Fulkerson algoritma"""
        pass

    def check_feasiblity(self):
        """metoda provjerava dopustivost toka u mrezi"""
        pass

    def flow(self,u,v):
        """provjeri tok na bridu (u,v)"""
        pass

    def total_flow(self):
        """ukupan tok iz s do t"""
        pass


