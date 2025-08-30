import pandas as pd
class Product:
    def __init__(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity

class Inventory:
    def __init__(self):
        self.data = pd.DataFrame(columns=['id','name','price','quantity'])
    
    def add_product(self,product:Product):
        new_row={
            'id':product.id,
            'name':product.name,
            'price':product.price,
            'quantity':product.quantity
        }
        self.data=pd.concat([self.data, pd.DataFrame([new_row])],ignore_index=True)
        print(f"{product.name} has been added sucessfully..")
    
    def update_stock(self,pid,new_quantity):
        if self.data.empty:
            return 'No product avilable in the list..'
        if pid in self.data['id'].values:
            self.data["quantity"] += new_quantity
            print(f"New quantity {new_quantity} has been update successfully..")
    
    def genrate_report(self):
        if self.data.empty:
            return 'No product avilable to genrate report..'
        self.data['Total Value']=self.data['price'] * self.data['quantity']
        return self.data

if __name__=="__main__":
    system = Inventory()
    # print(system)
    system.add_product(Product(1,'DryFruits',500,1))
    system.add_product(Product(2,'Fruits',100,2))

    system.update_stock(1,2)

    print(system.genrate_report())
