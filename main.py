import pygame
import heapq

import cell
from grid import Grid
from maze import Mazes
from config import Colors, Settings

pygame.init()
screen = pygame.display.set_mode((Settings.window_width, Settings.window_width))
pygame.display.set_caption("Maze Solver")
#icon = pygame.image.load('maze.png')
            

queue = []
closed_set = []
path = []


def main():
    gameboard = Grid(Settings.rows, Settings.window_width)

    end_selected = False
    end_cell = None

    
    terrain_generated = False
    search_started = False
    searching = True
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
                if event.key == pygame.constants.K_f and end_selected:
                    search_started = True
        
        if search_started:
            if len(queue) > 0 and searching:
                current_cell = queue.pop(0)
                current_cell.visited = True
                if current_cell == end_cell:
                    searching = False
                    while current_cell.prior != gameboard.start_cell:
                        path.append(current_cell.prior)
                        current_cell = current_cell.prior
                else:
                    for neighbour in current_cell.neighbours:
                        if not neighbour.queued and not neighbour.blocked:
                            neighbour.queued = True
                            neighbour.prior = current_cell
                            queue.append(neighbour)
            else:
                if searching:
                    print("No path found")
                    searching = False
                    
        screen.fill(Colors.black)
        for i in range(Settings.cols):
            for j in range(Settings.rows):
                cell = gameboard.grid[i][j]
                cell.draw(screen, (Colors.white))    

                if cell in path:
                    cell.draw(screen, (Colors.green))
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