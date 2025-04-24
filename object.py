"""Base class for objects in the game"""


class Object:
    def __init__(self, pos_y, pos_x, char):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.char = char
