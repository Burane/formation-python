from Book import Book
from Member import Member


class PremiumMember(Member):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.borrowed_books: list[Book] = []
        self.borrow_limit = 5
    
        
    def borrow_book(self, book: Book) -> None:
        if len(self.borrowed_books) <= self.borrow_limit:
            super().borrow_book(book)