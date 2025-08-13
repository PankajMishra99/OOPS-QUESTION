import math
class Product:
    def __init__(self,name,price,rating):
        self.name=name
        self.price=price
        self.rating=rating
    
    def __str__(self):
        return f"Product Name {self.name} with rating {self.rating} and price {self.price}"

class Product_comparing:
    def __init__(self):
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)
        print (f"Product Name is {product} has been added successfully..")
    
    def get_product_price(self,name):
        for product in self.products:
            if product.name==name:
                return product.price
        return 0
    
    def __eq__(self,other):
        if self.products:
            for product in self.products:
                if isinstance(other,Product_comparing):
                    return self.get_product_price(product.name)==other.get_product_price(product.name)
              
        else:
            print('No any Item is presented here..')
    

    def __lt__(self,other):
        if self.products:
            for product in self.products:
                if isinstance(other,Product_comparing):
                    return self.get_product_price(product.name)< other.get_product_price(product.name)
               
        else:
            print ('No any product avilable in the list')
    
    def __add__(self,other):
        if self.products:
            for product in self.products:
                if isinstance(other,Product_comparing):
                    return self.get_product_price(product.name) + other.get_product_price(product.name)
                
        else:
            print('No any item present in the List')


if __name__=="__main__":
    t1=Product_comparing()
    t2= Product_comparing()
    t1.get_product_price('Horlicks')
    t1.get_product_price('Boost')
    t1.add_product(Product('Horlicks',500,4.5))
    t1.add_product(Product('Boost',550,4.8))
    # ===========================================================================================
    t2.add_product(Product('Boost',550,4.8))
    t2.add_product(Product('Horlicks',500,4.5))


    print(t1==t2)
    # print(t1<t2)
    print(t1+t2)