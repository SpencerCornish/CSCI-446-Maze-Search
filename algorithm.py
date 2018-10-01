class Algorithm:
    num_steps = 0
    num_expanded = 0

    def search(self, maze):
        pass

    # get manhattan distance between two positions
    def get_distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
