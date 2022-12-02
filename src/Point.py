class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def multiplication(self, factor):
        return Point(self.x * factor, self.y * factor)
