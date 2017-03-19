NORTH = 'N'
SOUTH = 'S'
WEST = 'W'
EAST = 'E'


L_COORDS = [NORTH, EAST, SOUTH, WEST]


class Robot(object):
    def __init__(self, bearing=NORTH, base_x=0, base_y=0):
        self.bearing = bearing
        self.coordinates = (base_x, base_y)
        self.D_ORDERS = {
                'L': self.turn_left,
                'A': self.advance,
                'R': self.turn_right
                }

    def turn_right(self):
        wanted = L_COORDS.index(self.bearing) + 1
        self.bearing = L_COORDS[wanted % len(L_COORDS)]

    def turn_left(self):
        wanted = L_COORDS.index(self.bearing) - 1
        self.bearing = L_COORDS[wanted % len(L_COORDS)]

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = self.coordinates[0], self.coordinates[1]+1
        if self.bearing == SOUTH:
            self.coordinates = self.coordinates[0], self.coordinates[1]-1
        if self.bearing == EAST:
            self.coordinates = self.coordinates[0]+1, self.coordinates[1]
        if self.bearing == WEST:
            self.coordinates = self.coordinates[0]-1, self.coordinates[1]

    def simulate(self, orders):
        for order in orders:
            self.D_ORDERS[order]()
