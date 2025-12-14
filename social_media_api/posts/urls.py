from .views import (
    PostCreateListView, PostRetrieveUpdateDestroyView, 
    CommentCreateListView, CommentRetrieveUpdateDestroyView, 
    PostFeedListView, LikePost, UnLikePost
)
from django.urls import path 



urlpatterns = [
    path('post/', PostCreateListView.as_view()),
    path('post/<int:pk>', PostRetrieveUpdateDestroyView.as_view()),
    path('post/<int:pk>/comment', CommentCreateListView.as_view()),
    path('comment/<int:pk>', CommentRetrieveUpdateDestroyView.as_view()),
    path('feed/', PostFeedListView.as_view()),
    path('posts/<int:pk>/like/', LikePost.as_view() ),
    path('posts/<int:pk>/unlike/', UnLikePost.as_view())
]