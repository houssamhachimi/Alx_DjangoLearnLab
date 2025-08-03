from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Required exact line for the check
    return render(request, 'relationship_app/list_books.html', {'books': books})
