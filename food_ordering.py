from abc import ABC, abstractmethod
class Menuitem:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    
    def __str__(self):
        return f"Menuitem {self.name} - {self.price} with category {self.category}"

class Order:
    def __init__(self):
        self.items=[]
        self.__total=0
    def add_item(self,menuitem):
        self.items.append(menuitem)
        self.__total += menuitem.price
        print(f"{menuitem.name} has been added in order list.. with Total Bill {self.__total}")

    
    def remove_item(self,menuitem):
        self.items.remove(menuitem)
        self.__total -= menuitem.price
        print(f"Menuitem {menuitem.name} has been removed from order list updated price {self.__total}")
    
    def calculate_total(self):
        return self.__total

    def __len__(self):
        return len(self.items)

class Payment(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self,card_number):
        self.card_number=card_number
    
    def pay(self,amount):
        print (f"Payment {amount} has been done with credit card {self.card_number[-4:]}")

class CashPayment(Payment):
    def pay(self,amount):
        print(f"Payment {amount} has been done with Cash..")

# --------------------------------------
class Customer:
    def __init__(self,name):
        self.name=name
        self.orders=[]
    
    def place_order(self,order):
        self.orders.append(order)
        print(f"Order  successfully added..")
    
    def Make_payment(self,payment_method,order):
        total_payment = order.calculate_total()
        payment_method.pay(total_payment)


if __name__=="__main__":

    order=Order()
    order.add_item(Menuitem('Chilli Potato',100,'food'))
    order.add_item(Menuitem('Rice',50,'food'))

    order.calculate_total()

    customer=Customer('Amit')
    customer.place_order(order)

    customer.Make_payment(CashPayment(),order)




