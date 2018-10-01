import pygame
import time


class Maze:
    data = []
    start = []
    end = []
    width = 0
    height = 0

    display = None
    display_height = 800
    display_width = None
    node_size = None

    def __init__(self, maze_file):
        with open(maze_file, 'r') as file:
            for i, line in enumerate(file):
                line_list = list(line.strip('\n'))
                self.data.append(list(line.strip('\n')))
                if 'P' in line:
                    self.start = [i, line_list.index('P')]
                if '*' in line:
                    self.end = [i, line_list.index('*')]
        self.width = len(self.data[0])
        self.height = len(self.data)

        self.node_size = int(self.display_height / self.width)
        self.display_width = int(self.node_size * self.width)

        pygame.init()
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

    def draw(self):
        self.display.fill((255, 255, 255))
        color = None
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char == ' ':
                    continue
                elif char == '%':
                    color = (0, 0, 0)
                elif char == 'P':
                    color = (255, 0, 0)
                elif char == '*':
                    color = (0, 255, 0)
                elif char == '.':
                    color = (0, 0, 255)

                pygame.draw.rect(self.display, color,
                                 (i*self.node_size, j*self.node_size, self.node_size, self.node_size))
        pygame.display.update()
        time.sleep(0.1)
