from django.db import models

# Create your models here.


class Author(models.Model):
    """
        To Store authors in the database
    """
    name = models.CharField(max_length=64)


class Book(models.Model):

    """
        Books in the database.. each book will be associated to an Author
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

