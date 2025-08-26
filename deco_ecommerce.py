# Requirements:
# Track product operations (add_product, remove_product) with a log decorator.
# Decorator prints action name and timestamp whenever a method is executed.
# Users have roles (Admin can add/remove, Viewer can only view).
from datetime import datetime
def decorator(role):
    def wrapper(func):
        def inner_function(self,*args,**kwargs):
            if self.user.role==role:
                result = func(self,*args,**kwargs)
                print(f"Date Time {datetime.now()} with action name  : {func.__name__}")
                return result
            else:
                print (f"Dont't have permission to {self.user.name} for action {func.__name__}")
        return inner_function
    return wrapper

class User:
    def __init__(self,name,role):
        self.name=name
        self.role=role
class Product:
    def __init__(self,user):
        self.user=user
        self.products=[]
    
    @decorator('Admin')
    def add_product(self,product):
        self.products.append(product)
        print(f"Product name {product} has been added to cart..")
        # return self.products
    

    @decorator('Admin')
    def remove_product(self,product):
        self.products.remove(product)
        print(f"Product name {product} has been removed successfully..")
    
    @decorator('Viwer')
    def view_product(self):
        if self.products:
            for product in self.products:
                print(product,end=' ')
        else:
            print('No any product avilable..')

if __name__=="__main__":
    admin = User('Mr.A','Admin')
    viwer = User('Mr.B','Viwer')
    store_admin = Product(admin)
    store_admin.add_product('DryFruits')
    store_admin.add_product('Fruits')

    store_viwer = Product(viwer)



