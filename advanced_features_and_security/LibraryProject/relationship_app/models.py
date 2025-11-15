from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager

# User = get_user_model()


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


class UserProfile(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(choices=ROLES, default='Member')
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book {self.title} by {self.author.name}"

    class Meta:
        permissions = (
            ('can_add_book', 'Can add books'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        )


class Library(models.Model):
    name = models.CharField(max_length=64)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name



class Librarian(models.Model):
    name = models.CharField(max_length=64)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL,null=True, blank=True)

    