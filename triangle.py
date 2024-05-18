from math import sqrt
from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getPerimeter(self):
        return self.a+self.b+self.c
    def getArea(self):
        p=(self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
a=Triangle(2,3,4)
print(a.getArea())