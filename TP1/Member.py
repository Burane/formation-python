from Book import Book


class Member:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.borrowed_books: list[Book] = []
        
    def borrow_book(self, book: Book) -> None:
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"'{self.name}' has borrowed '{book}'")
            
    def return_book(self, book: Book) -> None:
        book.return_book()
        self.borrowed_books.remove(book)
        print(f"'{self.name}' has returned '{book}'")
        
    def list_borrowed_books(self) -> None:
        if len(self.borrowed_books) > 0:
            print(f"'{self.name}'s' borrowed books: {self.borrowed_books}")
        else:
            print(f"'{self.name}' hasn't borrowed any books")
