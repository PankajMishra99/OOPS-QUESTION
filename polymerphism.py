import math
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius
    
    def area(self):
        return math.pi*self.radius **2

if __name__=="__main__":
    Area=[Rectangle(4,5),Circle(5)]
    for shape in Area:
        print(f"Area for : {shape.area()}")
