from algorithm import Algorithm
import heapq


class Greedy(Algorithm):

    def search(self, maze):
        pos = maze.start
        self.visited.append(pos)
        q = []
        done = False
        while not done:
            neighbors = self.get_neighbors(maze, pos)
            for node in neighbors:
                heapq.heappush(q, (self.get_distance(node, maze.end), node))
                self.visited.append(node)
                if maze.data[node[0]][node[1]] == '*':
                    print("Found finish!")
                    done = True
                    break
            if not done:
                pos = heapq.heappop(q)[1]
                self.num_expanded += 1
            maze.draw(self.visited)
