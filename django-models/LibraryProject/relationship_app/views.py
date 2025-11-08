from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
# from django.contrib.auth import login

# from django.views.generic.detail import DetailView

from .models import Book, Library,Author

# from .models import Library
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class ViewBook(DetailView):
    model = Book 
    context_object_name = "book"
    template_name = 'relationship_app/book_detail.html'


@permission_required("can_add_book")
@require_http_methods(["POST"])
def create_book(request):
    data = request.POST
    title = data.get("title")
    author_name = data.get("author")
    author = get_object_or_404(Author, name=author_name)
    Book.objects.create(title=title, author=author)
    return redirect("books")

@permission_required("can_change_book")
@require_http_methods(["POST"])
def update_book(request, pk=None):
    data = request.POST
        
    title = data.get("title")
    author_name = data.get("author")
    book = get_object_or_404(Book, id=pk)
    if author_name:
        author = get_object_or_404(Author, name=author_name)
        book.author = author
    if title:
        book.title = title
    book.save()

    return redirect("book-detail", pk=pk)


@permission_required("can_delete_book")
@require_http_methods(["DELETE"])
def delete_book(request, pk=None):
        
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return redirect("books")



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
    

# for functions @user_passes_test
@method_decorator(user_passes_test(lambda user: user.profile.role == 'Admin'), name="dispatch")
class AdminView(TemplateView):
    template_name = "relationship_app/admin_view.html"


@method_decorator(user_passes_test(lambda user: user.profile.role == 'Librarian'), name="dispatch")
class LibrarianView(TemplateView):
    template_name = "relationship_app/librarian_view.html"

@method_decorator(user_passes_test(lambda user: user.profile.role == 'Member'), name="dispatch")
class MemberView(TemplateView):
    template_name = "relationship_app/member_view.html"


