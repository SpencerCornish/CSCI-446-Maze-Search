from algorithm import Algorithm

class DepthFirst(Algorithm):

    def printList(self, list):
        for i in list:
            print(i)

    def search(self, maze):
        start = maze.start                                                              # define start and end point
        stack = [start]                                                                 # define a stack that is 2D array with (node, [path])
        done = False

        while not done:
            current = stack.pop()                                                       # set node on top of stack to be current node

            if current not in self.visited:                                             # if we have not expanded current
                self.visited.extend(current)                                            # add current to explored
                self.num_expanded += 1

                neighbors = self.get_neighbors(maze, current)                           # find all neighbors
                for n in neighbors:

                    if n not in self.visited and n not in stack:
                        maze.draw(self.visited)                                         # check if neighbors have been explored

                        if maze.data[n[0]][n[1]] == '*':                                # check if n is the goal
                            self.visited.extend(n)
                            self.num_expanded += 1
                            print("found end")
                            done = True
                            break

                        else:
                            stack.append(n)

            maze.draw(self.visited)
        self.printList(self.visited)



