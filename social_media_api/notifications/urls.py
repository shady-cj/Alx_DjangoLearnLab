from django.urls import path
from .views import NotificationListView 



urlpatterns = [
    path("notfications/", NotificationListView.as_view())
]