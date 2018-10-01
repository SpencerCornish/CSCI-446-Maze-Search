class Algorithm:
    num_steps = 0
    num_expanded = 0
    visited = []

    def search(self, maze):
        pass

    # get manhattan distance between two positions
    def get_distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    # returns true if position is in maze, not a '%' and not visited
    def is_valid(self, maze, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= maze.height or pos[1] >= maze.width:
            return False
        if maze.data[pos[0]][pos[1]] == '%':
            return False
        if pos in self.visited:
            return False
        return True

    # return all valid neighbors around a position
    def get_neighbors(self, maze, pos):
        neighbors = [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]-1], [pos[0], pos[1]+1]]
        valid_neighbors = []
        for neighbor in neighbors:
            if self.is_valid(maze, neighbor):
                valid_neighbors.append(neighbor)
        return valid_neighbors
