class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'point ({self.x}, {self.y})')

    def __str__(self) -> None:
        return f'({self.x}, {self.y})'


p = Point(1, 2)
print(p)
