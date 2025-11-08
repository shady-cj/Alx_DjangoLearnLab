

from .models import Book, Author, Librarian, Library


all_books_by_author_1 = Book.objects.filter(author__id=1)


library_1 = Library.objects.get(id=1)

all_library_1_books = library_1.books.all()


library_1_librarian = library_1.librarian

