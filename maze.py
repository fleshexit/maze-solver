import random

class Mazes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = self.generate_maze()

    def generate_maze(self):

        NORTH, SOUTH, EAST, WEST = 1, -1, 2, -2
        
        maze = [["#" for _ in range(self.width)] for _ in range(self.height)]

        def is_valid(x, y):
            return 0 <= x < self.width and 0 <= y < self.height

        def carve_path(x, y):
            maze[y][x] = " "
            directions = [NORTH, SOUTH, EAST, WEST]
            random.shuffle(directions)
            for dx, dy in [(0, -2), (0, 2), (2, 0), (-2, 0)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and maze[new_y][new_x] == "#":
                    maze[y + dy // 2][x + dx // 2] = " "
                    carve_path(new_x, new_y)

        start_x, start_y = random.randrange(0, self.width, 2), random.randrange(0, self.height, 2)
        carve_path(start_x, start_y)

        return maze

    def get_maze(self):
        return self.maze
