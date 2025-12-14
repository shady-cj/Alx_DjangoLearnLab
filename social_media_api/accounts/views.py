from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import User, RegisterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class FollowUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id, *args, **kwargs):
        u = get_object_or_404(User, id=user_id)
        request.user.following.add(u)
        u.followers.add(request.user)

class UnFollowUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id, *args, **kwargs):
        u = get_object_or_404(User, id=user_id)
        request.user.following.remove(u)
        u.followers.remove(request.user)
