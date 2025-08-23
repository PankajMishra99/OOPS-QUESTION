from typing import Protocol,List
class Shape(Protocol):
    def shape(self)->None: ...

class Circle:
    def shape(self)->None:
        print('Draw the circle shape')

class Rectangle:
    def shape(self)->None:
        print('Draw the Rectangle shape')

class Triangle:
    def shape(self)->None:
        print('Draw the Triangle shape')

class Canvas:
    def __init__(self,shape:List[Shape]):
        self.shape=shape
    
    def process(self):
        for shap in self.shape:
            shap.shape()

if __name__=="__main__":
    system = Canvas([Circle(),Rectangle(),Triangle()])
    system.process()