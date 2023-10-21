import pygame

pygame.init()
width = 800
# Create the screen
screen = pygame.display.set_mode((width, width))

# Title and Icon
pygame.display.set_caption("Maze Solver")
#icon = pygame.image.load('maze.png')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREEN = (0, 255, 0)


class Cell:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def is_start(self):
        return self.colour == ORANGE
    
    def is_end(self):
        return self.colour == PURPLE
    
    def reset(self):
        self.colour = WHITE

    def make_start(self):
        self.colour = ORANGE

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN
    
    def make_barrier(self):
        self.colour = BLACK
    
    def make_end(self):
        self.colour = PURPLE
    
    def make_path(self):
        self.colour = YELLOW
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        pass

    def __lt__(self, other):
        return False



