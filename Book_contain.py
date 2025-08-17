class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return f"Book {self.title} with author {self.author}"

class Library:
    def __init__(self):
        self.books=[]
    
    def add_books(self,book):
        self.books.append(book)
        print(f"{book.title} has been added successfully..")
    
    def remove_book(self,book):
        self.books.remove(book)
    
    def __len__(self):
        return len(self.books)


    def __contains__(self,book):
        return book in self.books
    
    def __call__(self):
        return self


if __name__=="__main__":
    book1 = Book('Python','Mr.A')
    system=Library()
    system.add_books(Book('Python','Mr.A'))
    system.add_books(Book('SQL','Mr.B'))
  
    print(book1 in system)
