class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def neighbours(self):
        return [Cell(self.x - 1, self.y - 1), Cell(self.x, self.y - 1), Cell(self.x + 1, self.y - 1),
                Cell(self.x - 1, self.y), Cell(self.x + 1, self.y),
                Cell(self.x - 1, self.y + 1), Cell(self.x, self.y + 1), Cell(self.x + 1, self.y + 1)]

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return "<Cell (%s, %s)>" % (self.x, self.y)

    def __eq__(self, cell):
        return self.x == cell.x and self.y == cell.y

class Board:
    def __init__(self, live_cells):
        self.live_cells = live_cells

    @property
    def min_x(self):
        return min(map(lambda cell: cell.x, self.live_cells)) if self.live_cells else 0


    @property
    def min_y(self):
        return min(map(lambda cell: cell.y, self.live_cells)) if self.live_cells else 0

    @property
    def max_x(self):
        return max(map(lambda cell: cell.x, self.live_cells)) if self.live_cells else 0

    @property
    def max_y(self):
        return max(map(lambda cell: cell.y, self.live_cells)) if self.live_cells else 0

    def __str__(self):
        for cell in self.live_cells:
            print(cell)

    def is_cell_alive(self, cell):
        return cell in self.live_cells

    def live_neighbours(self, cell):
        res = []
        for c in cell.neighbours():
            if self.is_cell_alive(c):
                res.append(c)
        return res

    def next_generation(self):
        new_live_cells = []
        for x in range(self.min_x - 1, self.max_x + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                c = Cell(x,y)
                nb = self.live_neighbours(c)
                if self.is_cell_alive(c) and 2 <= len(nb) <= 3 or len(nb) == 3:
                    new_live_cells.append(c)

        return Board(new_live_cells)

    def print_ascii_representation(self):
        for x in range(self.min_x - 2, self.max_x + 3):
            for y in range(self.min_y - 2 , self.max_y + 3):
                print( '■ ' if self.is_cell_alive(Cell(x, y)) else '□ ', end='')

            print('')

    def matrix(self, width, height):
        for x in range(width):
            for y in range(height):
                yield self.is_cell_alive(Cell(x, y))


def construct_board_from_pattern(pattern):
    cells = []
    for x, line in enumerate(pattern.split('\n')):
        for y, char in enumerate(line):
            if char == '1': cells.append(Cell(x, y))

    return Board(cells)

pattern = '''0000
0000
0000
0000
'''
b = construct_board_from_pattern(pattern)
