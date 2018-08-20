import math


class Unit:
    """
    Unit is used to convert coefficient conveniently.
    Since `rad` is more common than `deg` in math
    I will always use `rad` as the default coefficient
    E.g. deg = math
    """
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.value = None

    def __mul__(self, value):
        return self.coefficient * value

    def __rmul__(self, value):
        return self.coefficient * value

    def __call__(self, value):
        return self.coefficient * value


deg = Unit(1/180*math.pi)
rad = Unit(1)
