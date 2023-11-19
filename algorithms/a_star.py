

class Astar:

    def __init__(self, grid):
        self.grid = grid
        self.open_set = []
        self.closed_set = []
        self.path = []
    
    def heuristic(self, a, b):
        # Manhattan distance
        return abs(a.i - b.i) + abs(a.j - b.j)
    
    def solve(self, start, end):
        self.open_set.append(start)
        while len(self.open_set) > 0:
            # Find the cell with the lowest f_cost
            current = self.open_set[0]
            for cell in self.open_set:
                if cell.f_cost < current.f_cost:
                    current = cell
            
            # If the current cell is the end cell, we're done
            if current == end:
                temp = current
                self.path.append(temp)
                while temp.previous:
                    self.path.append(temp.previous)
                    temp = temp.previous
                return self.path[::-1]
            
            self.open_set.remove(current)
            self.closed_set.append(current)
            
            # Check all neighbors
            for neighbor in current.neighbors:
                if neighbor in self.closed_set or neighbor.blocked:
                    continue
                
                temp_g_cost = current.g_cost + 1
                
                if neighbor not in self.open_set:
                    self.open_set.append(neighbor)
                elif temp_g_cost >= neighbor.g_cost:
                    continue
                
                neighbor.g_cost = temp_g_cost
                neighbor.h_cost = self.heuristic(neighbor, end)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.previous = current

        return None