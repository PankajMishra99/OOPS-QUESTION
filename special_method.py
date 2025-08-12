import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return f"[x,y] = {self.x}, {self.y}"
    
    def __str__(self):
        return f"Vector is {self.x},{self.y}"
    
    def __add__(self,other):
        if isinstance(other,Vector):
            x=self.x+other.x
            y=self.y+ other.y
            return x, y
        else:
            print("other is not instance of Vector")
    
    def __sub__(self,other):
        if isinstance(other,Vector):
            x=self.x-other.x
            y=self.y-other.y
            return x,y
        else:
            print("Other is not instance if Vector")
    
    def __eq__(self,other):
        if isinstance(other,Vector):
            return math.isclose(self.x,other.x) and math.isclose(self.y,other.y)
        else:
            print('other is not instance of Vector')
    
    def __lt__(self,other):
        if isinstance(other,Vector):
            return abs(self)<abs(other)
        else:
            print("other is not instance of other")
    def __len__(self):
        return len(self)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __mul__(self,scaler):
        if isinstance(scaler,(int,float)):
            return scaler * self.x , scaler * self.y
        return NotImplemented
    
    def __iter__(self):
        yield self.x
        yield self.y

if __name__=="__main__":
    v1=Vector(2,5)
    v2 =Vector(4,5)
    
    print(v1+v2)
    print(v1-v2)
    print(v1==v2)
    print(v1<v2)
    print(v1,5)
    for x in v1:
        print(x)
