# Requirements
# Use abc to make an abstract Account class.
# Two account types: SavingsAccount, CurrentAccount.
# Savings accounts have interest calculation, current accounts have overdraft limit.
# Support deposit, withdraw, and balance check.

from abc import ABC, abstractmethod
class Account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    
    
    def deposite(self,amount):
        if amount>0:
            self.balance += amount
            print("Amount {} has been added successfully..".format(amount))
        else:
            print('Insufficient amount..')
    
    @abstractmethod
    def withdraw(self,amount):
        if self.balance>=amount and amount>0:
            self.balance -= amount
            print(f"Amount {amount} has been withdraw successfully..")
        else:
            print('Insufficient amount..')
    
    def get_balance(self):
        return self.balance

class Saving_Account(Account):
    def __init__(self,acc_no,balance,intreset_charges):
        super().__init__(acc_no,balance)
        self.intreset=intreset_charges
    
    def withdraw(self,amount):
        if self.balance>=amount and amount>0:
            self.balance -= amount
            print("Amount {} has been credited successfully.".format(amount))
        else:
            print('Insufficient amount')
    
    def calculate_intreset_rate(self):
        if self.balance>0:
            total_balance = self.balance + self.intreset*self.intreset /100
            print(f"Balance {total_balance} has been total balance with intreset")
            return total_balance
        else:
            print('Insufficient balance..')
    
class Current_Account(Account):
    def __init__(self,acc_no,balance,overdarft_limit):
        super().__init__(acc_no,balance)
        self.overdraft_limit=overdarft_limit
    
    
    def withdraw(self,amount):
        if self.balance + self.overdraft_limit>=amount:
            self.balance -= amount
            print(f"{amount} has been withdraw successfully..")
        else:
            print('Insufficient Balance..')
    
if __name__=="__main__":
    saving = Saving_Account('A011',5000,2)
    saving.calculate_intreset_rate()


    current = Current_Account('B011',10000,1000)
    current.withdraw(1000)