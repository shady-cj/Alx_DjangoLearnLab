from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import CreateUpdatePermission
from rest_framework.permissions import IsAuthenticated
from .serializers import Post, PostSerializer, Comment, CommentSerializer

# Create your views here.

class PostCreateListView(ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, CreateUpdatePermission]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user)
    
class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, CreateUpdatePermission]
    serializer_class = PostSerializer 


class CommentCreateListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CreateUpdatePermission]

    def perform_create(self, serializer):
        id = self.kwargs.get('pk')
        post = get_object_or_404(Post, id=id)
        return serializer.save(post=post, author=self.request.user)
    

class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticated, CreateUpdatePermission]



