import pygame


class Cell:
    
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.f, self.g, self.h = 0, 0, 0 # f = g + h 
        self.start = False
        self.blocked = False
        self.end =  False
        self.queued = False # whether the cell is queued to be visited
        self.visited = False # whether the cell has been visited
        self.neighbours = [] # neighbours of the cell 
        self.prior = None # the cell that caused this cell to be set as a neighbour
    
    def draw(self, win, colour, shape=1):
        if shape == 1: 
            pygame.draw.rect( # draws regular square cell
                win, colour,(
                    self.x * self.width, self.y * self.width, self.width - 1, self.width - 1)) 
        else:
            pygame.draw.circle( # draws circular cell that will be contained within a square cell
                win, colour, (
                    self.x * self.width + self.width // 2, self.y * self.width + self.width // 2), self.width // 3)

    def set_neighbours(self, grid, cols, rows):

        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y]) # adds horizontal neighbouring cells to an array
        if self.x < cols - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1]) # adds horizontal neighbouring cells to an array
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])