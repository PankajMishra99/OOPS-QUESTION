from typing import Protocol
class Payment(Protocol):
    def pay(self,amount:float)->None:
        pass

class UPIPayment:
    def pay(self,amount: float)->None:
        print(f"{amount} has been paid by upipayment")

class Creditcard_Payment:
    def pay(self,amount:float)->None:
        print(f"{amount} has been paid by Creditcard")

class Paypal_Payment:
    def pay(self,amount:float)->None:
        print(f"{amount} has been paid by Paypal")

class Payment_processor:
    def process_payment(self,payment_method,amount):
        payment_method.pay(amount)

if __name__=="__main__":
    system=Payment_processor()
    system.process_payment(UPIPayment(),500)
    system.process_payment(Creditcard_Payment(),500)
    system.process_payment(Paypal_Payment(),500)