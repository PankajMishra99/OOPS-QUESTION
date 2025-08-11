class Electronics:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def get_price(self):
        return self.price

class Clothing:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def get_price(self):
        return self.price * 0.9
    
class Grocery:
    def __init__(self,name,price):
         self.name=name
         self.price=price
        
    def get_price(self):
        return self.price * 0.8
    

class Cart:
    def __init__(self):
        self.total_item=[]
    
    def add_item(self,product):
        self.total_item.append(product)
    

    def total_price(self):
        return sum(item.get_price() for item in self.total_item)

if __name__=="__main__":
    cart=Cart()
    cart.add_item(Electronics('Laptop',70000))
    cart.add_item(Electronics('TAB',20000))
    cart.add_item(Clothing('Shirt',1000))
    cart.add_item(Grocery('Rice',50))
    # print(cart)
    print(cart.total_price())