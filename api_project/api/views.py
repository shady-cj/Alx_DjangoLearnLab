from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import Book, BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    