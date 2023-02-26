class Shape(object):
    def __init__(self, name: str):
        self.name = name

    def whoami(self):
        print(f"I'm {self.name}")


class Rectangle(Shape):
    def __init__(self, name: str, length: int, width: int):
        super().__init__(name)
        self.length = length
        self.width = width

    def whoami(self):
        print(f"I'm {self.name}")


class Square(Shape):
    def __init__(self, name: str, side: int):
        super().__init__(name)
        self.side = side

    def whoami(self):
        print(f"I'm {self.name}")


class SomeClass(Square, Rectangle):
    pass


# todo find root cause issue once you get familiar with opps
obj = SomeClass('Hollow square', 10)
