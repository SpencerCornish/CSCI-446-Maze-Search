from maze import Maze
from a_star import AStar
from breadth_first import BreadthFirst
from depth_first import DepthFirst
from greedy import Greedy


class Main:
    maze = None
    algorithm = None

    def run(self):
        # get maze and algorithm selection from user
        self.maze = self.get_maze()
        self.algorithm = self.get_algorithm()

        # run selected algorithm on selected maze
        self.algorithm.search(self.maze)

        # write path to maze data as '.'
        for pos in self.algorithm.path:
            if (self.maze.data[pos[0]][pos[1]] != 'P' and
                    self.maze.data[pos[0]][pos[1]] != '*'):
                self.maze.data[pos[0]][pos[1]] = '.'

        # write path to output.txt
        with open('output.txt', 'w') as file:
            for line in self.maze.data:
                file.write(''.join(line) + '\n')

        # print number of nodes in path and number visited
        print('Steps to get to goal:     ' + str(len(self.algorithm.path)))
        print('Number of nodes expanded: ' + str(len(self.algorithm.visited)))

        # wait until user presses a key to end
        input("Press Enter to close...")

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
