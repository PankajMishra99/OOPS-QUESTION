def authicated(func):
    def wrapper(self,*args,**kwargs):
        if self.is_authnticated:
            return func(self,*args,**kwargs)
        else:
            return 'User must be login'
    return wrapper
    
    
class User:
    def __init__(self,name):
        self.name=name
        self.is_authnticated =False
        self.carts=[]
    
    def login(self):
        self.is_authnticated=True
        print(f"{self.name} logged in successfull..")
    
    @authicated
    def add_cart(self,item):
        self.carts.append(item)
        return f"{item} has been added successfully.."
    
    
    @authicated
    def checkout(self):
        self.is_authnticated=False
        print(f"{self.name} has been logged out..")


    def view_cart(self):
        if self.carts:
            for cart in self.carts:
                print(cart)

if __name__=="__main__":
    user=User('Amit')
    user.login()
    user.add_cart('Dry fruits')
    user.add_cart('fruits')
    user.add_cart('Rice')
    user.add_cart('Grocery')

    user.view_cart()

