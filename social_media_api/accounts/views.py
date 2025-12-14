from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import User, RegisterSerializer, ProfileSerializer
# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer