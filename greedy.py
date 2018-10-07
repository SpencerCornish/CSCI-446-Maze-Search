from algorithm import Algorithm
import heapq


class Greedy(Algorithm):

    def search(self, maze):
        q = []  # the heap
        current_node = maze.start
        self.visited.append([current_node.x, current_node.y])
        heapq.heappush(q, (self.get_distance(current_node, maze.end), current_node))

        while len(q) > 0:
            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to heap in format (distance_to_end, neighbor_node)
                heapq.heappush(q, (self.get_distance(node, maze.end), node))
                self.visited.append([node.x, node.y])
                # check for end
                if maze.data[node.x][node.y] == '*':
                    self.update_path(node)
                    maze.draw(self.visited, self.path)
                    return

            # set current node to closest node to end in heap
            current_node = heapq.heappop(q)[1]
            # update path to current_node and draw
            self.update_path(current_node)
            maze.draw(self.visited, self.path)
