from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
# generics.ListAPIView

from .serializers import BookSerializer
from .models import Book


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookViewSet(ModelViewSet):
    queryset = Book
    serializer_class = BookSerializer 
