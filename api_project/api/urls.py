from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'book_all', BookViewSet)

urlpatterns = [
   path('', include(router.urls)),
  path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]