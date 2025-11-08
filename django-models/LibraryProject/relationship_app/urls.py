from .views import AdminView, LibrarianView, MemberView,  list_books, LibraryListView, LibraryDetailView, register #views.register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path("book-list/", list_books, name="books"),
    path("library-list/", LibraryListView.as_view(), name="libraries"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("admin-view/", AdminView.as_view(), name="admin-view"),
    path("librarian-view/", LibrarianView.as_view(), name="librarian-view"),
    path("member-view/", MemberView.as_view(), name="member-view"),
    path('register/', register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout")

]