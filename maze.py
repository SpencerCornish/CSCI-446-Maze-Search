from tkinter import *
import time


class Maze:
    data = []
    start = []
    end = []
    squares = []
    width = 0
    height = 0

    display = None
    display_width = 1200
    display_height = None
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

        self.node_size = int(self.display_width / self.width)
        self.display_height = int(self.node_size * self.height)

        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=self.display_width, height=self.display_height)
        self.canvas.pack()
        for i, line in enumerate(self.data):
            self.squares.append([])
            for j, char in enumerate(line):
                color = None
                if char == ' ':
                    color = "white"
                elif char == '%':
                    color = "black"
                elif char == 'P':
                    color = "red"
                elif char == '*':
                    color = "yellow"
                elif char == '.':
                    color = "green"

                self.squares[i].append(self.canvas.create_rectangle(j * self.node_size, i * self.node_size,
                                             j * self.node_size + self.node_size,
                                             i * self.node_size + self.node_size, fill=color))
        self.tk.update()

    def draw(self, visited, path):
        color = None
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char == ' ':
                    if [i, j] in path:
                        color = "green"
                    elif [i, j] in visited:
                        color = "blue"
                    else:
                        color = "white"
                elif char == '%':
                    color = "black"
                elif char == 'P':
                    color = "red"
                elif char == '*':
                    color = "yellow"

                if color != self.canvas.itemcget(self.squares[i][j], "fill"):
                    self.canvas.itemconfig(self.squares[i][j], fill=color)
        self.tk.update()
