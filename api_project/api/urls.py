from django.urls import path, include
from .views import BookList, BookViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'book-viewset', BookViewset)

urlpatterns = [
   path('', include(router.urls)),
  path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]