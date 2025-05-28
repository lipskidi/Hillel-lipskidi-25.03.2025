class Rectangle:
    def __init__(self, width: int | float, height: int | float):

        self.width = width
        self.height = height
        self.area = width * height

    def get_square(self) -> int | float:
        return self.area

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented

    def __add__(self, other: "Rectangle") -> "Rectangle":
        new_width = (self.width + other.width + self.height + other.height) / 4
        return Rectangle(new_width, (self.area + other.area) / new_width)

    def __mul__(self, n: float) -> "Rectangle":
        if not isinstance(n, (int, float)):
            return NotImplemented
        factor = n ** 0.5
        return Rectangle(self.width * factor, self.height * factor)

    def __str__(self) -> str:
        return f"Rectangle: width - {self.width}, height - {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'