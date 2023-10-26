import pygame
import cell
from grid import Grid
from maze import Mazes
from config import Colors, Settings


pygame.init()
screen = pygame.display.set_mode((Settings.window_width, Settings.window_width))
pygame.display.set_caption("Maze Solver")
#icon = pygame.image.load('maze.png')


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2) + abs(y1-y2))

def main():
    gameboard = Grid(Settings.rows, Settings.window_width)

    end_selected = False
    searching = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                i, j = gameboard.get_clicked_pos(pos)
                gameboard.grid[i][j].blocked = True

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = gameboard.get_clicked_pos(pos)
                cell = gameboard.grid[row][col]
                cell.blocked = False
                if cell.start or cell.end:
                    continue
                if not end_selected:
                    end_cell = gameboard.grid[i][j]
                    end_cell.end = True
                    end_selected = True
                else:
                    gameboard.grid[i][j].blocked = False

        screen.fill(Colors.black)
        for i in range(Settings.cols):
            for j in range(Settings.rows):
                cell = gameboard.grid[i][j]
                cell.draw(screen, (Colors.silver))    

                if cell.start:
                    cell.draw(screen, (Colors.green))
                if cell.end:
                    cell.draw(screen, (Colors.red))
                if cell.blocked:
                    cell.draw(screen, (Colors.black))
        
        pygame.display.flip()

if __name__ == '__main__':

    main()