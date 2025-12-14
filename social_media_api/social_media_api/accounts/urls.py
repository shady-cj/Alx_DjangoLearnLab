from django.urls import path
from .views import RegisterUserView, UserProfileView
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', views.obtain_auth_token), 
    path('register/', RegisterUserView.as_view()),
    path('profile/', UserProfileView.as_view())
]