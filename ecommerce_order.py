from abc import ABC, abstractmethod
class Payment:

    @abstractmethod
    def process_payment(self,amount):
        pass

class Creditcard_Payment(Payment):
    def __init__(self,card_no):
        self.card_no=card_no
    
    def process_payment(self,amount):
        return f"Payment method by creadicard {self.card_no} with amount {amount}"

class PaypalMethod(Payment):
    def __init__(self,email_no):
        self.email_no=email_no
    
    def process_payment(self,amount):
        return f"Payment method by paypal method {self.email_no} with {amount}"

class item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
     
    def __str__(self):
        return f"Item name {self.name} with price {self.price}"

class Order:
    def __init__(self,payment_method:Payment):
        self.items=[]
        self.payment=payment_method
    
    def add_item(self,item):
        self.items.append(item)
        print(f"Item {item.name} has been added successfully.")
    
    def calculate_total(self):
        return sum(product.price for product in self.items)

    def process_payments(self):
        total_price=self.calculate_total()
        return self.payment.process_payment(total_price)

if __name__=="__main__":
    order=Order(Creditcard_Payment('124578'))
    order.add_item(item('clothes',1000))
    order.add_item(item('Dry-Fruit',500))

    print(order.calculate_total())
    print(order.process_payments())
