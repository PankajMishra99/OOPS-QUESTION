class Ecommerce:
    def __init__(self,platform_name,location):
        self.platform_name=platform_name
        self.location=location
    
    def display_platform_info(self):
        return f"Eommerce platform {self.platform_name} with location {self.location}"

    class Product:
        def __init__(self,product_id,product_name,price):
            self.product_id=product_id
            self.product_name=product_name
            self.price=price
        
        def display_product_info(self):
            return f"Product name {self.product_name} with price {self.price}"
    
    class Order:
        def __init__(self):
            self.products=[]
        
        def add_product(self,product):
            self.products.append(product)
            print(f"{product.product_name} has been added successfully")
            
        
        def calculate_total(self):
            total_price = 0
            for item in self.products:
                total_price +=item.price
            print('Total Price ',total_price)

system = Ecommerce('Amazone','Patna')
product1=system.Product(1,'Electronic',50000)
product2=system.Product(2,'Dryfruit',5000)

order = system.Order()
order.add_product(product1)
order.add_product(product2)
order.calculate_total()


        