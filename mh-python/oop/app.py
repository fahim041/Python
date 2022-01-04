class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Value can't be negative")
        self.__y = value

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


one = Point(10, 20)
one.draw()
