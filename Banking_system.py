from datetime import datetime
class Bank_Account:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        self.transactions=[]
    
    def deposite(self,amount):
        if amount>=0:
            self.balance += amount
            self.transactions.append(('Deposite',amount,datetime.now().strftime('%Y-%m-%d %H"%M:%S')))
            print(f"Deposite {amount} has been successfully!.")
        return 'amount can not be negative'
    
    def withdraw(self,amount):
        if amount>=0 and self.balance>=amount:
            self.balance -= amount
            self.transactions.append(("Withdraw",amount,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            print(f"Withdraw {amount} has been withdraw successfully!.")
        return 'Insufficient amount'


    def show_balance(self):
        return self.balance
    
    def show_transaction_history(self):
        for t in self.transactions:
                print(f"{t[0]} of {t[1]} on {t[2]}")
    
if __name__=="__main__":
    system=Bank_Account('01','Mr.A',500)

    system.deposite(100)
    system.withdraw(200)

    print(system.show_balance())
    print(system.show_transaction_history())
            