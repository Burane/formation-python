class Book:
    
    def __init__(self, title: str, author: str) -> None:
        self._title_ = title
        self._author_ = author
        self._is_available_ = True
        
    def borrow(self) -> bool:
        if self._is_available_:
            self._is_available_ = False
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f"{self._title_} written by {self._author_}, available: {self._is_available_}"
  
    def __repr__(self):
        return self.__str__()
        
    def return_book(self) -> None:
        self._is_available_ = True
        
    # Getters and Setters
    def get_title(self) -> str:
        return self._title_
    
    def set_title(self, title: str) -> None:
        self._title_ = title
        
    def get_author(self) -> str:
        return self._author_
    
    def set_author(self, author: str) -> None:
        self._author_ = author
        
    def is_available(self) -> bool:
        return self._is_available_
    
    def set_is_available(self, is_available: bool) -> None:
        self._is_available_ = is_available