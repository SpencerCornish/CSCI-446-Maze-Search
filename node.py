class Node:

    def __init__(self, x, y, prev):
        self.x = x
        self.y = y
        self.prev = prev

    def __lt__(self, other):
        return -1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
