from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment():
        pass

class Credit_card(Payment):
    def __init__(self,card_no):
        self.__card_no=card_no
    
    def make_payment(self,amount):
        print(f"Paid {amount} using credit card {self.__card_no}")

class Paypalamount(Payment):
    def __init__(self,email_id):
        self.__email =email_id
    
    def make_payment(self,amount):
        print(f"Paid {amount} has been paid by {self.__email}")

class UpiPayment(Payment):
    def __init__(self,upi_no):
        self.upi_no=upi_no
    
    def make_payment(self,amount):
        print(f"Paid {amount} using upipayment {self.upi_no}")


if __name__=="__main__":
    payment = [Credit_card('a011'),Paypalamount('a@44'),UpiPayment('a022')]
    for method in payment:
        method.make_payment(500)