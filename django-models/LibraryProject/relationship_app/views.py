from django.shortcuts import render

from django.views.generic import ListView, DetailView
# from django.views.generic.detail import DetailView

from .models import Book, Library

# from .models import Library
# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryListView(ListView):
    model = Library
    # template_name = "relationship_app/library_list.html"  default
    context_object_name = "libraries"


class LibraryDetailView(DetailView):
    model = Library
    # template_name = "relationship_app/library_detail.html"  default
    context_object_name = "library"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["extra"] = "Extra data"
        return context

