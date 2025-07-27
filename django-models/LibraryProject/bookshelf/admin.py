from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to show in list view
    list_filter = ('author', 'publication_year')            # Filters on sidebar
    search_fields = ('title', 'author')                      # Search box fields

