from abc import ABC, abstractmethod
class Payment:
    @abstractmethod
    def process_payment(self):
        pass

class Creditcardpayment(Payment):
    def process_payment(self,amount):
        return f"process_payment for credit_card {amount}"

class Paypalpayment(Payment):
    def process_payment(self,amount):
        return f"Process Payment for Pyapal Method {amount}"


if __name__=="__main__":
    Payment = [Creditcardpayment(),Paypalpayment()]
    for payment in Payment:
        print("Payment Method :",payment.process_payment(500))
