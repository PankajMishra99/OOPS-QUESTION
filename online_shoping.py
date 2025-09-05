import datetime
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __str__(self):
        return f"Name- {self.name}, Price {self.price}"

class Cart:
    def __init__(self):
        self.carts=[]
    
    def add_product(self,product):
            self.carts.append(product)
            self._log_transaction(f"{product.name} has been added successfully..")
            print(f"{product.name} has been added successfully..")
    
    # def remove(self,item):
    #     if self.carts:
    #         del self.carts[item]
    #     else:
    #         print('No item exists..')
    
    def _log_transaction(self,message:str):
        with open ('product.log','a') as f:
            f.write(f"{datetime.datetime.now()} - {message}")
    
    def checkout(self):
        total_price=0
        for product in self.carts:
            total_price +=product.price 
        
        return total_price

if __name__=="__main__":
    system =Cart()
    print
    system.add_product(Product('salt',200))
    system.add_product(Product('DryFruit',500))

    print(system.checkout())
    

    



    