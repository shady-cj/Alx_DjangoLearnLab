from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

