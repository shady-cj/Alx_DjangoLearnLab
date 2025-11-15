from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from bookshelf.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


