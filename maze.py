from tkinter import *
import time

from node import Node


class Maze:
    data = []
    start = None
    end = None
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
                    self.start = Node(i, line_list.index('P'), None)
                if '*' in line:
                    self.end = Node(i, line_list.index('*'), None)
        self.width = len(self.data[0])
        self.height = len(self.data)

        self.node_size = int(self.display_width / self.width)
        self.display_height = int(self.node_size * self.height)

        print("starting tk")
        self.tk = Tk()
        print("started tk")

        print("making canvas tk")

        self.canvas = Canvas(
            self.tk, width=self.display_width, height=self.display_height)

        print("made canvas tk")
        print("packng tk")

        self.canvas.pack()
        print("packed tk")

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
