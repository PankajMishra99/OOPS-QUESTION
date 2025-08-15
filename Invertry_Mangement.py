class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def __str__(self):
        return f"Product name {self.name} with {self.quantity} with {self.price}"
    
    def __lt__(self,other):
        return self.price < other.price

    def update_product(self,new_price=None,new_quantity=None):
        if new_price is not None:
            self.price=new_price
        if new_quantity is not None:
            self.quanity=new_quantity




class Inventry:
    def __init__(self):
        self.products=[]
    
    def add_product(self,name,price,quantity):
        self.products.append(Product(name,price,quantity))
        print(f"Product name {name} with price {price} and quantity {quantity}")
        return self.products
    

    def remove_item(self,name):
        if self.products:
            if name in self.products:
                self.products.remove(name)
                print(f"Product name {name} has been removed successfully..")
            else:
                print('Product name {name } not avilable in the product list..')
        else:
            print('No element exist in the product..')
    
    def display_inventry(self):
        if self.products:
            for product in self.products:
                print('Product name :',product.name,'\n')
        else:
            print('No product avilable in the product list')
    
    def cheapest_product(self):
        min_price=min([product.price for product in self.products])
        for product in self.products:
            if product.price==min_price:
                return product.name
        return None
    
    def expensive_product(self):
        max_price=max([product.price for product in self.products])
        for product in self.products:
            if product.price==max_price:
                return product.name
        return None

if __name__=='__main__':
    inventry = Inventry()
    inventry.add_product('Sweet',50,2)
    inventry.add_product('Salt',40,2)

    inventry.display_inventry()

    print(inventry.cheapest_product())