from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views 

router = DefaultRouter()

router.register(r'book_all', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]