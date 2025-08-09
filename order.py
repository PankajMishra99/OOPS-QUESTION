class MenuItem:
    def __init__(self,menu,price):
        self.menu=menu
        self.price=price
    
    def __str__(self):
        return f"{self.menu} with price {self.price}"
    
    def __repr__(self):
         return f"{self.menu} with price {self.price}"


class Order:
    def __init__(self):
        self.menus=[]
    
    def add_item(self,menu):
        self.menus.append(menu)
    
    def total_bill(self):
        if self.menus:
            totalbill=0
            for menu in self.menus:
                totalbill += menu.price
            return totalbill

        else:
            print ('No menu exist..')
    def __str__(self):
        return f"Total bill - {self.total_bill()}"

if __name__=="__main__":
    # menu = MenuItem('rice',40)
    # print(menu)
    system = Order()
    system.add_item(MenuItem('rice',40))
    system.add_item(MenuItem('Bread',50))

    print(system.total_bill())
            
        
