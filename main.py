import pygame
import cell
from grid import Grid
from maze import Mazes

pygame.init()
width = 800
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Maze Solver")
#icon = pygame.image.load('maze.png')

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2) + abs(y1-y2))

def main():
    rows = 50
    gameboard = Grid(rows, width)

    start = None
    end = None

    run = True
    searching = False

    while run:
        gameboard.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if searching:
                continue
    
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                row, col = gameboard.get_clicked_pos(pos)
                cell = gameboard.grid[row][col]
                if not start and cell != end:
                    start = cell
                    start.make_start()
                elif not end and cell != start:
                    end = cell
                    end.make_end()
                elif cell != end and cell != start:
                    cell.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = gameboard.get_clicked_pos(pos)
                cell = gameboard.grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None
            



    pygame.quit()

main()