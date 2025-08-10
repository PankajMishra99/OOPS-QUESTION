from abc import ABC,abstractmethod
class Library(ABC):
    def __init__(self,title,author):
        self.title=title
        self.author = author
        self.is_avialable=True
    
    @property
    def available(self):
        return self.is_avialable
        
    @available.setter
    def avilable(self,value):
        self.is_avialable=value
    
    @abstractmethod
    def borrow(self):
        pass

class Book(Library):
    def borrow(self):
        if self.is_avialable:
            self.is_avialable=False
            print(f"Book {self.title} with {self.author} borrow successfull..")
        else:
            print(f"No any book avialable.")

class Magzine(Library):
    def borrow(self):
        if self.is_avialable:
            self.is_avialable=False
            print(f"Magzine {self.title} with {self.author} borrow successfull")


if __name__=="__main__":
    book =Book('Python','A')
    book.borrow()
    book.borrow()