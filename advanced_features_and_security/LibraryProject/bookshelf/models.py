from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group

# editors = Group.objects.get_or_create(name="Editors")
# viewers = Group.objects.get_or_create(name="Viewers")
# admins = Group.objects.get_or_create(name="Admins")

# editors.permissions.set(["bookshelf.can_create", "bookshelf.can_edit", "bookshelf.can_view"])
# viewers.permissions.set(["bookshelf.can_view"])
# admins.permissions.set(["bookshelf.can_create", "bookshelf.can_edit", "bookshelf.can_view", "bookshelf.can_delete"])

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):

        if username is None:
            raise TypeError("Users should have a Username")
        if password is None:
            raise TypeError("Password is required")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if username is None:
            raise TypeError("Users should have a Username")
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(username, password, **extra_fields)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="users/photo", null=True, blank=True)
    objects = CustomUserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        permissions = (
            ("can_view", "Can view books"),
            ("can_create", "Can Create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books")
        )
    
