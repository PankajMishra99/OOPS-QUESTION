# Requirement:
# Create a BankAccount class with methods like deposit(), withdraw(), and check_balance().
# Only users with role = "Admin" can withdraw money.
# Use a decorator to enforce role-based access.
def role_required(role):
    def decorator(func):
        def wrapper(self,*args:any,**kwargs:any):
            if self.role==role:
                return func(self,*args,**kwargs)

            else:
                return f"Access denied for role : {role}"
        return wrapper
    return decorator

class BankSystem:
    def __init__(self,owner,balance,role):
        self.owner=owner
        self.balance=balance
        self.role=role
    
    def deposite(self,amount):
        self.balance +=amount
        print(f"{amount} has been deposite successfully")
    
    @role_required('Admin')
    def withdraw(self,amount):
        if self.balance>=amount and amount>0:
            self.balance -= amount
            print(f"{amount} has been withdraw successfully..")
        else:
            print("Insufficient balance")
    

    def check_balance(self):
        return self.balance

if __name__=='__main__':
    bank=BankSystem('Amit',1600,'Admin')
    bank.deposite(200)
    bank.withdraw(400)
    print(bank.check_balance())

