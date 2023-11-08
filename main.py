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

class SearchAlgorithm:

    def __init__(self, start, end):
        self.start = start
        self.target = end
        self.path = []
        self.queue = []

    def heuristic(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (abs(x1-x2) + abs(y1-y2))

    def a_star(self):
        open_set = []
        closed_set = set()
        heapq.heappush(open_set, (0, self.start))
        came_from = {}

        g_score = {cell: float('inf') for row in self.grid for cell in row}
        g_score[self.start] = 0
        f_score = {cell: float('inf') for row in self.grid for cell in row}
        f_score[self.start] = self.heuristic(self.start, self.target)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == self.target:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                self.path = path
                return True

            closed_set.add(current)

            for neighbor in current.neighbors:
                if neighbor.blocked or neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.target)
                    if neighbor not in open_set:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return False

    def begin(self, grid):
        self.grid = grid  # Set the grid
        if self.a_star():
            for cell in self.path:
                cell.visited = True
        else:
            print("No path found")
            

def main():
    gameboard = Grid(Settings.rows, Settings.window_width)

    end_selected = False
    end_cell = None
    search = SearchAlgorithm(gameboard.start_cell, end_cell)
    
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
                if event.key == pygame.constants.K_f and end_selected:
                    search.begin(gameboard.grid)
            
                    
        screen.fill(Colors.black)
        for i in range(Settings.cols):
            for j in range(Settings.rows):
                cell = gameboard.grid[i][j]
                cell.draw(screen, (Colors.white))    

                if cell in search.path:
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