from algorithms.a_star import A_star

class Pathfinder:

    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.queue = []
        self.closed_set = []
        self.path = []
        self.searching = True
        self.search_started = False

    def heuristic(self, a, b):
        return abs(a.i - b.i) + abs(a.j - b.j)
    
    def findpath(self, algorithm):
        if algorithm == "A*":
            self.a_star()
        elif algorithm == "Dijkstra":
            self.dijkstra()
        elif algorithm == "BFS":
            self.bfs()
        elif algorithm == "DFS":
            self.dfs()
        elif algorithm == "Greedy":
            self.greedy()