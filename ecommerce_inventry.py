from abc import ABC,abstractmethod
class User:
    def __init__(self,name,email):
        self.__name=name
        self.__email= email
    
    @abstractmethod
    def get_details(self):
        return f"User name {self.__name} and email {self.__email}"

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def Update_stock(self,new_qtn):
        self.quantity -=new_qtn

class Customer(User):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.orders=[]
    
    def order_place(self,product,quantity):
        if product.quantity>=quantity:
            product.Update_stock(quantity)
            self.orders.append((product.name,quantity))
            print(f"Product {product.name} with quantity {quantity} has been placed successfully with total price {product.price * quantity}")
        else:
            print ('Product out of stock')
    
    def get_details(self):
        return super().get_details()

class Seller(User):
    def __init__(self,name,email_id):
        super().__init__(name,email_id)
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)
        print(f"Product {product.name} has been placed")
    def get_details(self):
        return super().get_details()


if __name__=="__main__":
    seller=Seller('Mr.A','ravi@gmail.com')
    p1 = Product("Laptop", 50000, 10)
    p2 = Product("Mobile", 20000, 5)

    seller.add_product(p1)
    seller.add_product(p2)

    ########################################
    customer=Customer('Mr.P','P@gmail.com')
    customer.order_place(p1,2)
    customer.order_place(p2,5)

            