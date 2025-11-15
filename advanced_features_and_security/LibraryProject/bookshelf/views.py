from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
from django.contrib.auth.decorators import permission_required

# Create your views here.
from .models import Book


@permission_required("bookshelf.can_view", raise_exception=True)
def view_book(request, pk=None):
    if request.method == "GET":
        book = get_object_or_404(Book, pk=pk)
        return HttpResponse(f"Book detail\n {book.title} by {book.author} published {book.publication_year}")
    
@permission_required("bookshelf.can_view", raise_exception=True)
def list_books(request):
    if request.method == "GET":
        books = get_list_or_404(Book.objects.all())
        result = ""
        for book in books:
            result += f"{book.title} by {book.author}\n"
        return HttpResponse(f"List of boks\n {result}")
    
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        book_title = request.POST.get('title')
        book_author = request.POST.get('author')
        book_year = request.POST.get('publication_year')
        Book.objects.create(title=book_title, author=book_author, publication_year=book_year)

        return HttpResponse(f"Book created successfully", 201)

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk=None):
    if request.method == 'DELETE':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return HttpResponse(f"Book deleted successfully", 204)


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk=None):
    if request.method == "POST":
        book_title = request.POST.get('title')
        book_author = request.POST.get('author')
        book_year = request.POST.get('publication_year')
        book = get_object_or_404(Book, pk=pk)
        if book_title:
            book.title = book_title
        if book_author:
            book.author = book_author
        if book_year:
            book.publication_year = book_year
        book.save()
        return HttpResponse(f"Edited: {book.title} by {book.author} published {book.publication_year}")



    
