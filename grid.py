import pygame
from config import Colors
from cell import Cell
import random

class Grid:

    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = []
        self.create()
        self.find_neighbours()

    def create(self):
        for i in range(self.rows):
            colArray = []
            for j in range(self.rows):
                cell = Cell(i, j)
                colArray.append(cell)
            self.grid.append(colArray)
    
        self.start_cell = self.grid[1][1]
        self.start_cell.visited = True
        self.start_cell.start = True
    
    def find_neighbours(self):
        for row in self.grid:
            for cell in row:
                cell.set_neighbours(self.grid, self.rows, self.rows)
            
    def draw(self, screen):
        screen.fill(Colors.white)

        for self.row in self.grid:
            for cell in self.row:
                cell.draw(screen)

        self.draw_grid(screen)
        pygame.display.update()

    def get_clicked_pos(self, pos):
        gap = self.width // self.rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col
    
    def reset(self):
        for row in self.grid:
            for cell in row:
                cell.blocked = False
                cell.visited = False
                cell.queued = False
                cell.path = False
                cell.end = False
                
    def place_mines(self):
        self.reset()
        for row in self.grid:
            for cell in row:
                if random.randint(0, 10) < 3:
                    if not cell.start and not cell.end:
                        cell.blocked = True