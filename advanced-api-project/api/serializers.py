from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # def validate_publication_year(self, instance):
    #     pass

    def validate_publication_year(self, value):
        now = datetime.now()
        if value > now.year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
        



    
class Author(serializers.ModelSerializer):
    books = BookSerializers(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

