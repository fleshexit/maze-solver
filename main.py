import pygame
import grid.cell as cell
from grid.grid import Grid
from mazes.maze import Mazes
from config import Colors, Settings

pygame.init()
screen = pygame.display.set_mode((Settings.window_width, Settings.window_width))
pygame.display.set_caption("Maze Solver")
            

def main():
    gameboard = Grid(Settings.rows, Settings.window_width)

    end_selected = False
    end_cell = None

    
    terrain_generated = False
    times_clicked = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
            if pygame.mouse.get_pressed()[0] and terrain_generated: 
                pos = pygame.mouse.get_pos()
                i, j = gameboard.get_clicked_pos(pos)
                gameboard.grid[i][j].blocked = True

            elif pygame.mouse.get_pressed()[2] and terrain_generated:
                pos = pygame.mouse.get_pos()
                i, j = gameboard.get_clicked_pos(pos)
                if cell.start or cell.end:
                    continue
                if not end_selected:
                    end_cell = gameboard.grid[i][j]
                    end_cell.end = True
                    end_selected = True
                else:
                    gameboard.grid[i][j].blocked = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    terrain_generated = True
                    times_clicked += 1
                    if times_clicked == 1:
                        gameboard.place_mines()
                if event.key == pygame.constants.K_r:
                    gameboard.reset()
                #if event.key == pygame.constants.K_f and end_selected:
                #    logic...
                    
        screen.fill(Colors.black)
        for i in range(Settings.cols):
            for j in range(Settings.rows):
                cell = gameboard.grid[i][j]
                cell.draw(screen, (Colors.white))    

                #if cell in path:
                #    cell.draw(screen, (Colors.green))
                if cell.queued:
                    cell.draw(screen, (255, 200, 0))
                    cell.draw(screen, (255, 175, 0), 1)
                if cell.visited:
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
