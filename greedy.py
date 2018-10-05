from algorithm import Algorithm
import heapq


class Greedy(Algorithm):

    def search(self, maze):
        current_node = maze.start
        self.visited.append([current_node.x, current_node.y])
        q = []  # the heap
        done = False

        while not done:
            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to heap in format (distance_to_end, neighbor_node)
                heapq.heappush(q, (self.get_distance(node, maze.end), node))
                self.visited.append([node.x, node.y])
                # check for end
                if maze.data[node.x][node.y] == '*':
                    print("Found finish!")
                    done = True
                    break
            # set current node to closest node to end in heap
            current_node = heapq.heappop(q)[1]
            self.update_path(current_node)
            maze.draw(self.visited, self.path)
