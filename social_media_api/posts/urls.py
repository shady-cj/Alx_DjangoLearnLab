from .views import PostCreateListView, PostRetrieveUpdateDestroyView, CommentCreateListView, CommentRetrieveUpdateDestroyView, PostFeedListView
from django.urls import path 



urlpatterns = [
    path('post/', PostCreateListView.as_view()),
    path('post/<int:pk>', PostRetrieveUpdateDestroyView.as_view()),
    path('post/<int:pk>/comment', CommentCreateListView.as_view()),
    path('comment/<int:pk>', CommentRetrieveUpdateDestroyView.as_view()),
    path('feeds/', PostFeedListView.as_view())
]