from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Book, Library
# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

class LibraryListView(ListView):
    model = Library
    context_object_name = "libraries"


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["extra"] = "Extra data"
        return context

