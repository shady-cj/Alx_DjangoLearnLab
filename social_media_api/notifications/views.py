from django.shortcuts import render

# Create your views here.
from .models import Notification 
from .serializers import NotificationSerializer


from rest_framework.generics import ListAPIView


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer