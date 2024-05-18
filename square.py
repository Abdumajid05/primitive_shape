from polygon import Polygon

class Square(Polygon):
    def getArea(self):
        return self.width**2
    def getPerimeter(self):
        return self.width*4
    
a=Square(5,6)
print(a.getArea())
print(a.getPerimeter())