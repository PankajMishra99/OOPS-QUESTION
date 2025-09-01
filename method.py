def decorator():
    def wrapper(func):
        def inner_function(self,*args,**kwargs):
                result= func(self,*args,*kwargs)
                print(f"Function name {func.__name__} with the argument {args} and {kwargs}")
                self.logs.append(f"{func.__name__} ")
                return result
        return inner_function
    return wrapper


class Inventry_system:
    def __init__(self):
        self.items=[]
        self.logs=[]
    @decorator()
    def add_item(self,item):
        if len(item)>0:
            self.items.append(item)
            print(f"{item} has been added successfully..")
        else:
            raise  ValueError ("Please enter the correct input")
    @decorator()
    def remove_item(self,item):
        if self.items:
            self.items.remove(item)
            print(f"{item} has been removed successfully..")
        else:
            print("no item exists in the items list..")
    @decorator()
    def view_inventry(self):
        if self.items:
            for item in self.items:
                print("Item name ",item)
        else:
            print('no item exist in the list')

if __name__=="__main__":
    system=Inventry_system()
    system.add_item('dryfruit')
    system.add_item('fruit')

    system.view_inventry()

