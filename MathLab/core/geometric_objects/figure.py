from core.geometric_objects.geom_obj import *
from core.exception.exception import CustomException
import sympy as sp


class Circle(Shape):
    def __init__(self, x, y, radius, color="black"):
        try:
            if radius < 0:
                raise CustomException("Radius less than zero")
        except CustomException as e:
            print(f"Произошла ошибка: {e.message}")
        else:
            super().__init__(color)
            self.x = sp.symbols('x')
            self.y = sp.symbols('y')
            self.center = (x, y)
            self.radius = radius

    def area(self):
        return sp.pi * self.radius**2

    def perimeter(self):
        return 2 * sp.pi * self.radius


class Square(Shape):
    def __init__(self, x1_, y1_, x2_, y2_, color="black"):
        try:
            if x1_ == x2_ and y1_ == y2_:
                raise CustomException("The vertices of the square coincide")
        except CustomException as e:
            print(f"Произошла ошибка: {e.message}")
        else:
            super().__init__(color)
            self.x1 = x1_
            self.y1 = y1_
            self.x2 = x2_
            self.y2 = y2_
            self.side = sp.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, x1_, y1_, x2_, y2_, x3_, y3_, color="black"):
        try:
            if (x1_ == x2_ and y1_ == y2_) or (x1_ == x3_ and y1_ == y3_) or (x3_ == x2_ and y3_ == y2_):
                raise CustomException("The vertices of the triangle coincide")
        except CustomException as e:
            print(f"Произошла ошибка: {e.message}")
        else:
            super().__init__(color)
            self.x1 = x1_
            self.y1 = y1_
            self.x2 = x2_
            self.y2 = y2_
            self.x3 = x3_
            self.y3 = y3_
            self.a = sp.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
            self.b = sp.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
            self.c = sp.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = sp.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def perimeter(self):
        return self.a + self.b + self.c
