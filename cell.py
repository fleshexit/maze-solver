import pygame
from config import Colors

class Cell:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = Colors.white
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == Colors.red
    
    def is_open(self):
        return self.colour == Colors.green

    def is_barrier(self):
        return self.colour == Colors.black

    def is_start(self):
        return self.colour == Colors.orange
    
    def is_end(self):
        return self.colour == Colors.purple
    
    def reset(self):
        self.colour = Colors.white

    def make_start(self):
        self.colour = Colors.orange

    def make_closed(self):
        self.colour = Colors.red

    def make_open(self):
        self.colour = Colors.green
    
    def make_barrier(self):
        self.colour = Colors.black
    
    def make_end(self):
        self.colour = Colors.purple
    
    def make_path(self):
        self.colour = Colors.yellow
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        pass

    def __lt__(self, other):
        return False