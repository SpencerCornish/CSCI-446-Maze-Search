from algorithm import Algorithm
import heapq


class AStar(Algorithm):

    def search(self, maze):
        q = []  # the heap
        current_node = maze.start
        heapq.heappush(q, (self.get_heuristic(
            maze, current_node), current_node))

        while len(q) > 0:
            # set current node to closest node to end in heap
            current_node = heapq.heappop(q)[1]
            # update path to current_node and draw
            self.update_path(current_node)
            maze.draw(self.visited, self.path)

            # check for end
            if maze.data[current_node.x][current_node.y] == '*':
                return

            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to heap in format (distance_to_end, neighbor_node)
                if (self.get_heuristic(maze, node), node) not in q:
                    heapq.heappush(
                        q, (self.get_heuristic(maze, node), node))

            self.visited.append([current_node.x, current_node.y])

    def get_heuristic(self, maze, current_node):
        return self.get_distance(maze.start, current_node) + self.get_distance(current_node, maze.end)
