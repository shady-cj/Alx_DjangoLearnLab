from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from .models import Book, Author
from django_filters.rest_framework import DjangoFilterBackend

# from django_filters import rest_framework
# from rest_framework import generics

from .serializers import BookSerializer, AuthorSerializer


class BookListView(ListAPIView): 
    """
        List all books in the database
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    filterset_fields = ['publication_year', 'author__name']
    # This will ensure that only authenticated users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    """
        Create a new book in the database
    """
    permission_classes = [IsAuthenticated]
    # This will ensure that only authenticated users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):
    """
        Retrieve a book from the database
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    # This will ensure that only authenticated users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    """
        Update a book in the database
    """
    permission_classes = [IsAuthenticated]
    # This will ensure that only authenticated users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
    """
        Delete a book from the database
    """
    permission_classes = [IsAuthenticated]
    # This will ensure that only authenticated users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer




