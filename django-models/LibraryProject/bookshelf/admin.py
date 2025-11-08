from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by (adds sidebar filters)
    list_filter = ('author', 'publication_year')

    # Fields to search by (adds search bar)
    search_fields = ('title', 'author')

    # Optional: ordering in the admin list
    ordering = ('title',)