from .views import AdminView, LibrarianView, MemberView,  list_books, LibraryListView, LibraryDetailView,ViewBook, register,create_book, update_book,delete_book #views.register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path("book-list/", list_books, name="books"),
    path('book-create/', create_book, name="book-create"),
    path('book-update/', update_book, name='book-update'),
    path('book-delete', delete_book, name='book-delete'),
    path('book-detail/<int:pk>/', ViewBook.as_view(), name='book-detail'),
    path("library-list/", LibraryListView.as_view(), name="libraries"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("admin-view/", AdminView.as_view(), name="admin-view"),
    path("librarian-view/", LibrarianView.as_view(), name="librarian-view"),
    path("member-view/", MemberView.as_view(), name="member-view"),
    path('register/', register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout")

]