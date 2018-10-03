from algorithm import Algorithm
import heapq


class Greedy(Algorithm):

    def search(self, maze):
        pos = maze.start
        prev_pos = maze.start
        self.visited.append(pos)
        self.path.append(pos)
        q = []
        done = False

        while not done:
            neighbors = self.get_neighbors(maze, pos)
            for node in neighbors:
                heapq.heappush(q, (self.get_distance(node, maze.end), node, pos))
                self.visited.append(node)
                if prev_pos in self.path:
                    self.path = self.path[:self.path.index(prev_pos)+1]
                self.path.append(pos)
                if maze.data[node[0]][node[1]] == '*':
                    print("Found finish!")
                    done = True
                    break
            if not done:
                info = heapq.heappop(q)
                pos = info[1]
                prev_pos = info[2]
                self.num_expanded += 1
            maze.draw(self.visited, self.path)
