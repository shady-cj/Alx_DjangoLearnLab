from .views import list_books, LibraryListView, LibraryDetailView
from django.urls import path


urlpatterns = [
    path("book-list", list_books, name="books"),
    path("library-list", LibraryListView.as_view(), name="libraries"),
    path("library/<int:pk>", LibraryDetailView.as_view(), name="library-detail")

]