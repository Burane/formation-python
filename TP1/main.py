from Library import Library

# Création de la bibliothèque
library = Library()
 
# Ajout de livres
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
print("=" * 40)
 
# Ajout de membres
library.add_member("regular", "Alice")
library.add_member("premium", "Bob")
 
print("=" * 40)
 
# Affichage des livres disponibles
library.list_books()
 
print("=" * 40)
 
# Emprunt de livres par Alice
alice = library.find_member("Alice")
gatsby = library.find_book("The Great Gatsby")
alice.borrow_book(gatsby)

print("=" * 40)
 
# Emprunt de livres par Bob
bob = library.find_member("Bob")
mockingbird = library.find_book("To Kill a Mockingbird")
bob.borrow_book(mockingbird)
 
print("=" * 40)
 
# Affichage des livres empruntés par chaque membre
alice.list_borrowed_books()
bob.list_borrowed_books()
 
print("=" * 40)
 
# Retour des livres
alice.return_book(gatsby)
alice.list_borrowed_books()