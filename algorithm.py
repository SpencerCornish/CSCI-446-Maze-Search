from node import Node


class Algorithm:
    visited = []        # list of lists of x,y coords - not a node
    path = []           # list of lists of x,y coords - not a node
    # update by calling update_path

    # function to be overwritten
    def search(self, maze):
        pass

    # get manhattan distance between two nodes
    def get_distance(self, node1, node2):
        return abs(node1.x-node2.x) + abs(node1.y-node2.y)

    # returns true if node is in maze, not a '%', and not visited
    def is_valid(self, maze, node):
        if node.x < 0 or node.y < 0 or node.x >= maze.height or node.y >= maze.width:
            return False
        if maze.data[node.x][node.y] == '%':
            return False
        if [node.x, node.y] in self.visited:
            return False
        return True

    # return all valid nodes around a node
    # set prev of each neighbor to node
    def get_neighbors(self, maze, node):
        neighbors = [Node(node.x - 1, node.y, node), Node(node.x + 1, node.y, node),
                     Node(node.x, node.y - 1, node), Node(node.x, node.y + 1, node)]
        valid_neighbors = []
        for neighbor in neighbors:
            if self.is_valid(maze, neighbor):
                valid_neighbors.append(neighbor)
        return valid_neighbors

    # update path list by going backwards from node
    def update_path(self, node):
        self.path = [[node.x, node.y]]
        while node.prev is not None:
            self.path.append([node.prev.x, node.prev.y])
            node = node.prev
