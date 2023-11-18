import pygame
from config import Colors
from cell import Cell
import random

class Splash:

    letter_patterns = {
        'P': [
            "111",
            "101",
            "111",
            "100",
            "100"
        ],
        'R': [
            "111",
            "101",
            "110",
            "101",
            "101"
        ],
        'E': [
            "111",
            "100",
            "111",
            "100",
            "111"
        ],
        'S': [
            "111",
            "100",
            "111",
            "001",
            "111"
        ],
        'A': [
            "111",
            "101",
            "111",
            "101",
            "101"
        ],
        'C': [
            "111",
            "100",
            "100",
            "100",
            "111"
        ]

    }

    def draw(grid, word, start_x, start_y):
        for i, letter in enumerate(word):
            Splash.draw_letter(grid, letter, start_x, start_y + i * 4)


    def draw_letter(grid, letter, start_x, start_y):
        pattern = Splash.letter_patterns.get(letter, [])
        if not pattern:
            print(f"Letter {letter} not supported")
            return
        
        for x, row in enumerate(pattern):
            for y, char in enumerate(row):
                if char == '1':
                    grid[start_y + y][start_x + x].blocked = True

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

        Splash.draw(self.grid, "PRESS", 3, 3)
        Splash.draw(self.grid, "SPACE", 9, 3)
    
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