from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="user-profile")
    followers = models.ManyToManyField('self', symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False)
    
