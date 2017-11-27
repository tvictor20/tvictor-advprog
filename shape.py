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
