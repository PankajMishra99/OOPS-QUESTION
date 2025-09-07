class Bank:
    def __init__(self,bank_name,branch):
        self.bank_name=bank_name
        self.branch=branch
    
    def display_bank_info(self):
        return f"Bank name {self.bank_name} and branch name {self.branch}"
    
    class Account:
        def __init__(self,account_no,holder_name,balance):
            self.account_no = account_no
            self.holder_name=holder_name
            self.balance=balance
        
        def deposite(self,amount):
            if amount>0:
                self.balance +=amount
                print("Amount {amount} has been added successfully..")
            else:
                raise ValueError('amount cant be negative..')
        
        def withdraw(self,amount):
            if self.balance>=amount:
                self.balance -= amount
                print(f"{amount} has been with withdraw successfully..")
            else:
                raise ValueError("Insufficient balance")
        
        def display_account_info(self):
            return f"Account holder name {self.holder_name} and Account no {self.account_no}"
    
bank=Bank('ICICI','Renukoot')
print(bank.display_bank_info())
account = bank.Account('a011','Mr.A',500)
account.deposite(100)
account.withdraw(200)
print(account.display_account_info())