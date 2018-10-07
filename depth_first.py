from algorithm import Algorithm


class DepthFirst(Algorithm):

    def search(self, maze):
        stack = []  # the stack
        current_node = maze.start
        stack.append(current_node)

        while len(stack) > 0:
            # set current node to next node in stack
            current_node = stack.pop()
            # update path to current_node and draw
            self.update_path(current_node)
            maze.draw(self.visited, self.path)

            # check for end
            if maze.data[current_node.x][current_node.y] == '*':
                return

            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to stack
                if node not in stack:
                    stack.append(node)

            self.visited.append([current_node.x, current_node.y])
