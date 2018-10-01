from maze import Maze
from a_star import AStar
from breadth_first import BreadthFirst
from depth_first import DepthFirst
from greedy import Greedy


class Main:
    maze = None
    algorithm = None

    def __init__(self):
        self.maze = self.get_maze()
        self.algorithm = self.get_algorithm()

    def run(self):
        self.algorithm.search(self.maze)
        with open('output.txt', 'w') as file:
            for line in self.maze.data:
                file.write(''.join(line) + '\n')
        print('Steps to get to goal:     ' + str(self.algorithm.num_steps))
        print('Number of nodes expanded: ' + str(self.algorithm.num_expanded))

    @staticmethod
    def get_maze():
        print("Choose a maze")
        print("\t1. Open Maze")
        print("\t2. Medium Maze")
        print("\t3. Large Maze")
        selection = int(input())

        if selection == 1:
            return Maze('mazes/open_maze.txt')
        elif selection == 2:
            return Maze('mazes/medium_maze.txt')
        elif selection == 3:
            return Maze('mazes/large_maze.txt')

    def get_algorithm(self):
        print("Choose a search algorithm")
        print("\t1. Depth-first")
        print("\t2. Breadth-first")
        print("\t3. Greedy best-first")
        print("\t4. A*")
        selection = int(input())

        if selection == 1:
            return DepthFirst()
        elif selection == 2:
            return BreadthFirst()
        elif selection == 3:
            return Greedy()
        elif selection == 4:
            return AStar()

main = Main()
main.run()