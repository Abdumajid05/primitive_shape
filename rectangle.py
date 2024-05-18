from polygon import Polygon

class Rectangle(Polygon):
    def getArea1(self):
        return super().getArea()
    
    def getPerimeter1(self):
       return super().getPerimeter()
    
a=Rectangle(5,6)
print(a.getArea1())
print(a.getPerimeter1())