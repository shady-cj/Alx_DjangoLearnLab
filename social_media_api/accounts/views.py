from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import User, RegisterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
# Create your views here.
# generics.GenericAPIView", "permissions.IsAuthenticated", "CustomUser.objects.all()", "return Response
class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class FollowUser(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id, *args, **kwargs):
        u = get_object_or_404(User, id=user_id)
        request.user.following.add(u)
        u.followers.add(request.user)
        serializer = self.get_serializer(request.user)
        Notification.objects.create(
            recipient = u,
            actor = request.user,
            object_id=u.id,
            verb=f"{request.user.username} started following you",
            target=ContentType.objects.get_for_model(u)
        )
        return Response(serializer.data)

class UnFollowUser(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id, *args, **kwargs):
        u = get_object_or_404(User, id=user_id)
        request.user.following.remove(u)
        u.followers.remove(request.user)
        serializer = self.get_serializer(request.user)
        Notification.objects.create(
            recipient = u,
            actor = request.user,
            object_id=u.id,
            verb=f"{request.user.username} unfollowed you",
            target=ContentType.objects.get_for_model(u)
        )
        return Response(serializer.data)

