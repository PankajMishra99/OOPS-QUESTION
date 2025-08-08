class BankAccount:
    def __init__(self,name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    
    def deposite(self,amount):
        if amount>0:
         self.balance +=amount
         print(f"{amount} has depoiste successfully")
        else:
           print('Invalid amount')
    
    def withdraw(self,amount):
       if amount<=self.balance and amount>0:
          self.balance -=amount
          print(f"{amount} has been withdraw successfully.")
       else:
          print('Invalid amount')


    def check_balance(self):
       return self.balance

    def __str__(self):
       return f"{self.name} and Account no  : {self.account_number} has balance {self.balance}"
    
if __name__=="__main__":
   system = BankAccount('bitu','A011',500)
   system.deposite(200)
   print(system.withdraw(100))
   print(system.check_balance())

   print(system)