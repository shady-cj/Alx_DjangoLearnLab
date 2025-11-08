from .views import list_books, LibraryListView, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path("book-list/", list_books, name="books"),
    path("library-list/", LibraryListView.as_view(), name="libraries"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path('register/', register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout")

]