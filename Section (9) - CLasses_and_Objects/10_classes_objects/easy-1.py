from msilib.schema import Class
from xml.etree.ElementTree import PI


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def get_area(self):
        return float(22 / 7 * self.radius* self.radius)



r = Rectangle(2, 5)
print(r.get_area())

c = Circle(5)
print(c.get_area())