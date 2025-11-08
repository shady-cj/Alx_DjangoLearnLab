from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=64)

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=64)
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField(max_length=64)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL,null=True, blank=True)

    