from django.shortcuts import render
from .models import Book, Library  # import Library for later

def list_books(request):
    books = Book.objects.all()  # Simple queryset, no extras
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
