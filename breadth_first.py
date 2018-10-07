from algorithm import Algorithm


class BreadthFirst(Algorithm):

    def search(self, maze):
        q = []  # the queue
        current_node = maze.start
        self.visited.append([current_node.x, current_node.y])
        q.append(current_node)

        while len(q) > 0:
            # set current node to next node in queue
            current_node = q.pop(0)
            # update path to current_node and draw
            self.update_path(current_node)
            maze.draw(self.visited, self.path)

            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to queue
                q.append(node)
                self.visited.append([node.x, node.y])
                # check for end
                if maze.data[node.x][node.y] == '*':
                    self.update_path(node)
                    maze.draw(self.visited, self.path)
                    return
