from math import *

class Circle():
    def __init__(self, r):
        self.x = r

    def area(self):
        return (self.x**2)*3.14

    def perimeter(self):
        return 2*self.x*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def area(self):
        return float(self.w * self.l)

    def perimeter(self):
        return float(2 * self.w) + (2 * self.l)

    def __str__(self):
        return "Rectangle has an area of %.2f, and a perimeter of %.2f" % (self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, s):
        self.w = s
        self.l = s

class RtTriangle():
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def hyp(self):
        g = self.b ** 2
        k = self.h ** 2
        x = g + k
        return float(sqrt(x))

    def area(self):
        return float((self.b * self.h)/2)

    def perimeter(self):
        return float(self.hyp() + self.h + self.b)

    def __str__(self):
        return "Triangle has a hypotenuse of %.2f an area of %.2f, and a perimeter of %.2f" % (self.hyp(), self.area(), self.perimeter())

class IsoRtTriangle(RtTriangle):
    def __init__(self, s):
        self.b = s
        self.h = s

class RecPrism(Rectangle):
    def __init__(self, w, l, z):
        self.w = w
        self.l = l
        self.z = z

    def area(self):
        return float(self.w * self.l * self.z)

    def perimeter(self):
        return float(2*(self.w * self.l + self.w * self.z + self.l * self.z))

    def __str__(self):
        return "Rectangular prism has an area of %.2f and a perimeter %.2f." % (self.area(), self.perimeter())

class TriPrism(RtTriangle):
    def __init__(self, b, h, z):
        self.b = b
        self.h = h
        self.z = z

    def ar
