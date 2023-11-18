from pathfinding import Pathfinder

class A_star(Pathfinder):

    def __init__(self, grid, start, end):
        super().__init__(grid, start, end)
        self.queue = []
        self.closed_set = []
        self.path = []
        self.searching = True
        self.search_started = False


