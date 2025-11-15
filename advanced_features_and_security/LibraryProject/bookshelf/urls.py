from django.urls import path
from .views import create_book, list_books, edit_book, view_book, delete_book

urlpatterns = [

    path("shelf-list-books/", list_books, name="shelf-list-books"),
    path("shelf-view-book/<int:pk>/", view_book, name="shelf-view-book"),
    path("shelf-edit-book/<int:pk>/", edit_book, name="shelf-edit-book"),
    path("shelf-create-book/", create_book, name="shelf-create-book"),
    path("shelf-delete-book/", delete_book, name="delete-book"),
]