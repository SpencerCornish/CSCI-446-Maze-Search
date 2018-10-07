from algorithm import Algorithm


class DepthFirst(Algorithm):

    def search(self, maze):
        stack = []  # the stack
        current_node = maze.start
        self.visited.append([current_node.x, current_node.y])
        stack.append(current_node)

        while len(stack) > 0:
            # get all valid neighbors around current position
            neighbors = self.get_neighbors(maze, current_node)
            for node in neighbors:
                # add neighbors to stack
                stack.append(node)
                self.visited.append([node.x, node.y])
                # check for end
                if maze.data[node.x][node.y] == '*':
                    self.update_path(node)
                    maze.draw(self.visited, self.path)
                    return

            # set current node to next node in stack
            current_node = stack.pop()
            self.update_path(current_node)
            maze.draw(self.visited, self.path)



