from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):

        if username is None:
            raise TypeError("Users should have a Usernaname")
        if password is None:
            raise TypeError("Password is required")

        user = self.model(user=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        if username is None:
            raise TypeError("Users should have a Username")
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="users/photo")
    objects = CustomUserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
