from django.urls import path
from .views import RegisterUserView, UserProfileView, FollowUser, UnFollowUser
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', views.obtain_auth_token), 
    path('register/', RegisterUserView.as_view()),
    path('profile/<int:pk>', UserProfileView.as_view()),
    path('follow/<int:user_id>/', FollowUser.as_view()),
    path('unfollow/<int:user_id>/', UnFollowUser.as_view()),

]