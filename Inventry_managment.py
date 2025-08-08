class Item:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity = quantity
        self.price=price
    
    def update_quantity(self,qnty:int)-> int:
        self.quantity += qnty
    
    def calculate_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name} and {self.quantity} has total price {self.calculate_price()}"
    
class Inventry:
    def __init__(self):
        self.items=[]
    
    def add_item(self,name,quantity,price):
        for item in self.items:
            if item.name==name:
                item.update_quantity(quantity)
                return 
        self.items.append(Item(name,quantity,price))
    
    def remove_item(self,name):
        self.items=[item for item in self.items if item.name != name]
    
    def display_item(self):
        if not self.items:
            print('No item available..')
        for item in self.items:
            print('Item :', item , '\n')
    
    def calculate_total_inventry(self):
        return sum(item.calculate_price()  for item in self.items)
    


if __name__=="__main__":
    system = Inventry()
    system.add_item('a',10,20)
    system.add_item('b',5,10)
    system.display_item()
    system.remove_item('b')
    print(system.calculate_total_inventry())

