# Requirement: Bank Account System with Role-Based Actions
# Req
# Users have name, role (Customer, Admin).
# Admin can approve_loan.
# Customer can deposit and withdraw.
# Use a decorator to restrict access based on role.

def decorator(role):
    def wrapper(func):
        def inner_function(self,*args,**kwargs):
            if self.user.role==role:
                return func(self,*args,**kwargs)
            else:
                print(f"Access denied for {self.user.role}")
        return inner_function
    return wrapper

class User:
    def __init__(self,name,role):
        self.name=name
        self.role=role

class Banksystem:
    def __init__(self,user):
        self.user=user
        self.balance=0
    
    @decorator('Customer')
    def deposite(self,amount):
        self.balance +=amount
        print(f"{amount} has been added..")
    

    @decorator('Customer')
    def withdraw(self,amount):
        if self.balance>=amount and amount>0:
            self.balance -= amount
            print(f'{amount} has been withdraw successfully..')
        else:
            print('Insufficient balance')
    
    @decorator('Admin')
    def Approve_loan(self):
        return f"Loan approved load : {self.user.name}.."

if __name__=="__main__":
    admin = User('Mr.A','Admin')
    customer = User('Mr.B','Customer')

    system_admin = Banksystem(admin)
    system_customer = Banksystem(customer)

    system_customer.deposite(200)
    system_customer.withdraw(100)

    print(system_admin.Approve_loan())