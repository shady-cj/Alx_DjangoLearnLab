from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()



class Notification(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    object_id = models.PositiveIntegerField()
    verb = models.CharField()
    target = GenericForeignKey (
        "content_type", "object_id"
    )
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)