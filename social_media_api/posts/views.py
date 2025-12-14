from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CreateUpdatePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import Post, PostSerializer, Comment, CommentSerializer
from .models import Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
# we could use "viewsets", "viewsets.ModelViewSet"
#generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"
# Create your views here.

class PostCreateListView(ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, CreateUpdatePermission]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "content", "author"]

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["content", "post", "author"]

    def perform_create(self, serializer):
        id = self.kwargs.get('pk')
        post = get_object_or_404(Post, id=id)
        instance = serializer.save(post=post, author=self.request.user)
        Notification.objects.create(
            recipient = post.author,
            actor = self.request.user,
            object_id=post.id,
            verb="New comment on your post",
            target=ContentType.objects.get_for_model(post)
        )
        return instance
    

class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticated, CreateUpdatePermission]



class PostFeedListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["content", "post", "author"]
    permission_classes = [IsAuthenticated]
# ["permissions.IsAuthenticated"]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
   


class LikePost(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer 
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        Like.objects.get_or_create(post=post, user=request.user)
        Notification.objects.create(
            recipient = post.author,
            actor = self.request.user,
            object_id=post.id,
            verb="Your post was liked",
            target=ContentType.objects.get_for_model(post)
        )
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
class UnLikePost(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer 
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like = get_object_or_404(Like, post=post, user=request.user)
        like.delete()
        Notification.objects.create(
            recipient = post.author,
            actor = self.request.user,
            object_id=post.id,
            verb="Your post was disliked",
            target=ContentType.objects.get_for_model(post)
        )
        serializer = self.get_serializer(post)
        return Response(serializer.data)


