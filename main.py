import pygame
import cell
import grid

pygame.init()
width = 800
# Create the screen
screen = pygame.display.set_mode((width, width))

# Title and Icon
pygame.display.set_caption("Maze Solver")
#icon = pygame.image.load('maze.png')

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2) + abs(y1-y2))