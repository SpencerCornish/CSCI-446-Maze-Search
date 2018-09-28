class Maze:
    data = []
    start = ()
    end = ()

    def __init__(self, maze_file):
        with open(maze_file, 'r') as file:
            for x, line in enumerate(file):
                line_list = list(line.strip('\n'))
                self.data.append(list(line.strip('\n')))
                if 'P' in line:
                    self.start = (x, line_list.index('P'))
                if '*' in line:
                    self.end = (x, line_list.index('*'))
