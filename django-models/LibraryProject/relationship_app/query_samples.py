

from .models import Book, Author, Librarian, Library


author_name = "J.K Rowling"

author = Author.objects.get(name=author_name)


#objects.filter(author=author)

all_books_by_author_1 = Book.objects.filter(author=author)

library_name = "new library"
library_1 = Library.objects.get(name=library_name)

all_library_1_books = library_1.books.all()


library_1_librarian = library_1.librarian

