import pygame
from config import Colors
from cell import Cell

class Grid:

    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = []
        self.create()

    def create(self):
        gap = self.width // self.rows
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                cell = Cell(i, j, gap, self.rows)
                self.grid[i].append(cell)
        
        return self.grid

    def draw_grid(self, screen):
        gap = self.width // self.rows
        for i in range(self.rows):
            pygame.draw.line(screen, Colors.grey, (0, i * gap), (self.width, i * gap))
            for j in range(self.rows):
                pygame.draw.line(screen, Colors.grey, (j * gap, 0), (j * gap, self.width))
            
    
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
                
        