from algorithm import Algorithm


class BreadthFirst(Algorithm):

    def search(self, maze):
        q = []  # the queue
        current_node = maze.start
        q.append(current_node)

        while len(q) > 0:
            # set current node to next node in queue
            current_node = q.pop(0)
            # update path to current_node and draw
            self.update_path(current_node)
            maze.draw(self.visited, self.path)

            # check for end
            if maze.data[current_node.x][current_node.y] == '*':
                return

            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to queue
                if node not in q:
                    q.append(node)

            self.visited.append([current_node.x, current_node.y])

