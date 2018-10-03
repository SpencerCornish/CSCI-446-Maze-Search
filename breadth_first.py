from algorithm import Algorithm
from collections import deque


class BreadthFirst(Algorithm):
    def search(self, maze):
        start = maze.start
        end = maze.end
        queue = deque([start])
        explored = []

        while queue:
            cur = queue.popleft()
            self.num_steps += 1

            if cur not in explored:
                explored.append(cur)
                self.num_expanded += 1

                neighbors = self.get_neighbors(maze, cur)
                for n in neighbors:
                    if n not in explored:
                        if n != end:
                            queue.append(n)
                        else:
                            print("found end")
