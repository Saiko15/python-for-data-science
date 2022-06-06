
from ast import And
from tkinter import N
from turtle import width


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

class Editor:
    def __init__(self):
        self.rect = None
        self.circ = None

    def creat_rectangle(self, width, height):
        self.rect = Rectangle(width, height)

    def creat_circle(self,radius):
        self.circ = Circle(radius)

    def change(self, factor):
        if self.rect != None:
            self.rect.width += factor
            self.rect.height += factor
        if self.circ != None:
            self.circ.radius += factor



    def print(self):
        if self.rect:
            print("Rectangle area ", self.width * self.height)
        if self.circ:
            print("Circle area ", 22/7 * self.radius * self.radius)


r = Rectangle(2, 5)
print(r.get_area())     # 10

c = Circle(5)
print(c.get_area())     # 78.5

editor = Editor()
editor.creat_rectangle(3, 5)
editor.print()