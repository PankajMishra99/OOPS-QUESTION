class Book:
    def __init__(self,title,author,isbn,avilable_copies):
        self.title=title
        self.author = author
        self.isbn=isbn
        self.avilable_copies = avilable_copies
    
    def borrow_book(self):
        self.avilable_copies -=1
    
    def return_book(self):
        self.avilable_copies +=1

class Member:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
    
    def borrow_book(self,book):
        if book.avilable_copies>0:
            self.borrowed_books.append(book)
            print("Book Title {} has been borrowed successfully.".format(book.title))
        else:
            print(f"{book.title} already have borrowed") 

    def return_books(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returened successfully..")
        else:
            print(f"{book.title} is not avilable in the borrowd_list..")
    

if __name__=="__main__":
    book1=Book('Python oops','Mr.A','isbn001',2)
    book2=Book('Python Basics','Mr.B','isbn002',1)

    m1=Member('Amit')
    m1.borrow_book(book1)
    m1.borrow_book(book2)
