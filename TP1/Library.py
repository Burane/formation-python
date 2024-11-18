from Book import Book
from Member import Member
from PremiumMember import PremiumMember
from RegularMember import RegularMember


class Library:
    
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []
    
    def add_book(self, title: str, author: str) -> None:
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: '{book}'")
        
    def add_member(self, member_type: str, name: str) -> None:
        if member_type == "regular":
            self.members.append(RegularMember(name))
        elif member_type == "premium":
            self.members.append(PremiumMember(name))
        else:
            print(f"Cant add member '{name}', member type '{member_type}' unknown")
            return
        print(f"Added {member_type} member: '{name}'")
            
    def list_books(self):
        print(f"Books: {self.books}")
        
    def find_book(self, title: str) -> None | Book:
        for book in self.books:
            if book._title_ == title:
                return book
            
        return None
        
    def find_member(self, name: str) -> None | Member:
        for member in self.members:
            if member.name == name:
                return member
            
        return None
        
        